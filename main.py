import os
import face_recognition
import cv2
import cvzone
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime
import pickle
import pandas as pd
import openpyxl

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendanc-94909-default-rtdb.firebaseio.com/",
    'storageBucket': "facerecognitionattendanc-94909.appspot.com"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# importing the mode images into a list
imgBackground = cv2.imread('resources/background.png')
folderformodepath ='resources/Modes'
modepathlist=os.listdir(folderformodepath)
imgmodelist=[]
for path in modepathlist:
    imgmodelist.append(cv2.imread(os.path.join(folderformodepath, path)))
# print(len(imgmodelist))


# Load the Encoding file




print("Loading Encode File...")
file = open("EncodeFile.p", 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode File Loaded.")

modeType = 0
counter = 0
id = -1
imgStudent = []
resized_img = []

n = len(imgmodelist)

for i in range(n):
    img = cv2.resize(imgmodelist[i], (414, 633))
    imgmodelist[i] = img


attendance_data = pd.DataFrame(columns=['StudentID', 'Name', 'AttendanceTime'])

while True:
    success, img = cap.read()

    imgSmall = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgSmall=cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(imgSmall)
    encodeCurrentFrame = face_recognition.face_encodings(imgSmall, faceCurrentFrame)

    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44+633, 808:808+414] = imgmodelist[modeType]

    if faceCurrentFrame:
        for encodeFace, faceLocation in zip(encodeCurrentFrame, faceCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print("Matches", matches)
            # print("Face dis", faceDistance)

            matchIndex = np.argmin(faceDistance)
            # print("Match Index", matchIndex)

            if faceDistance[matchIndex]>0.5:
                modeType = 4
                counter = 0
                break


            if matches[matchIndex]:
                # print("Known face detected")
                # print(studentIds[matchIndex])
                y1, x2, y2, x1 = faceLocation
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                bbox = 55+x1, 162+y1, x2-x1, y2-y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIds[matchIndex]
                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

                if id not in attendance_data['StudentID'].values:
                    # Record attendance
                    studentInfo = db.reference(f'Students/{id}').get()
                    new_entry = {
                        'StudentID': id,
                        'Name': studentInfo['Name'],
                        'AttendanceTime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    attendance_data = pd.concat([attendance_data, pd.DataFrame([new_entry])])

        if counter != 0:
            if counter == 1:
                # Getting The data
                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo)
                # Get the image from the storage
                blob = bucket.get_blob(f'images/{id}.jpeg')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                resized_img = cv2.resize(imgStudent, (216, 216))

                #  Update data of attendance
                datetimeObject = datetime.strptime(studentInfo['Last_Attendance_Time'],
                                                   "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (datetime.now()-datetimeObject).total_seconds()
                if secondsElapsed > 30:
                    ref = db.reference(f'Students/{id}')
                    studentInfo['Total_Attendance'] += 1
                    ref.child('Total_Attendance').set(studentInfo['Total_Attendance'])
                    ref.child('Last_Attendance_Time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgmodelist[modeType]


            if modeType != 3:

                if 10<counter<20:
                    modeType = 2

                imgBackground[44:44 + 633, 808:808 + 414] = imgmodelist[modeType]

                if counter<=10:
                    cv2.putText(imgBackground, str(studentInfo['Total_Attendance']), (861,125),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

                    cv2.putText(imgBackground, str(studentInfo['Major']), (1006, 558),
                                cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 1)

                    cv2.putText(imgBackground, str(id), (1006, 493),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

                    cv2.putText(imgBackground, str(studentInfo['Grade']), (910, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                    cv2.putText(imgBackground, str(studentInfo['Year']), (1025, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                    cv2.putText(imgBackground, str(studentInfo['Batch']), (1125, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                    (width, height), _ =cv2.getTextSize(studentInfo['Name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414-width)//2

                    cv2.putText(imgBackground, str(studentInfo['Name']), (808+offset, 445),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)

                    imgBackground[175:175+216, 909:909+216] = resized_img

                counter += 1

                if counter>=20:
                    counter=0
                    modeType=0
                    studentInfo = []
                    imgStudent = []
                    resized_img = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgmodelist[modeType]
    else:
        modeType = 0
        counter = 0

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)

    attendance_data.to_excel('attendance.xlsx', index=False)