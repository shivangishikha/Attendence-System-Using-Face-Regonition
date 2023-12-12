from flask import Flask, render_template, request, redirect
from flask_uploads import UploadSet, IMAGES, configure_uploads
import os
import firebase_admin
from firebase_admin import credentials, db, storage
from datetime import datetime

app = Flask(__name__)

# Configuration for file uploads
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "uploads"
configure_uploads(app, photos)

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendanc-94909-default-rtdb.firebaseio.com/",
    'storageBucket': "facerecognitionattendanc-94909.appspot.com"
})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student_id = request.form['student_id']
        student_data = {
            "Name": request.form['name'],
            "Major": request.form['major'],
            "Total_Attendance": 0,
            "Last_Attendance_Time": "",
            "Batch": int(request.form['batch']),
            "Year": int(request.form['year']),
            "Grade": request.form['grade']
        }

        # Handle file upload
        if "photo" in request.files:
            photo = request.files["photo"]
            if photo.filename != "":
                filename = f"{student_id}.jpg"
                photo.save(os.path.join("uploads", filename))

                # Upload the image to Firebase Storage
                bucket = storage.bucket()
                blob = bucket.blob(f"images/{filename}")
                blob.upload_from_filename(os.path.join("uploads", filename), content_type="image/jpeg")

                # Update the student data with the image URL
                student_data["Photo_URL"] = blob.public_url

        ref = db.reference('Students')
        ref.child(student_id).set(student_data)

        return redirect('/')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
