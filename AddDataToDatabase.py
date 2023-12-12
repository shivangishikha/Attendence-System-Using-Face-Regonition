import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendanc-94909-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "20115001": {
        "Name": "Elon Musk",
        "Major": "CSE",
        "Total_Attendance": 0,
        "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
    },
    "20115002": {
            "Name": "Emily Blunt",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115003": {
            "Name": "Tom Cruise",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115014": {
            "Name": "Ankit Kumar Ray",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115023": {
            "Name": "Chirag Singhal",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115045": {
            "Name": "Kartikey Thawait",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115047": {
            "Name": "Kishan Kumar Gupta",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115058": {
            "Name": "Millind Agrawal",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115075": {
            "Name": "Pranay Vaidya",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115085": {
            "Name": "Rohit Jaiswal",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115086": {
            "Name": "Sandeep Patel",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115087": {
            "Name": "Satyam Singh",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115090": {
            "Name": "Surya Babu",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115095": {
            "Name": "Siddharth Mishra",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115103": {
            "Name": "Thamesh Chandravanshi",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "21115001": {
            "Name": "Tanmay Goyal",
            "Major": "IT",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "21115002": {
            "Name": "Utkarsh Vishwakarma",
            "Major": "IT",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "21115003": {
            "Name": "Shrajan Pandey",
            "Major": "IT",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
        },
    "20115110": {
            "Name": "Vishesh Kumar Gavel",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
    },
    "20115102": {
            "Name": "Taresh Dewangan",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
    },
    "20115092": {
            "Name": "Shivangi Shikha",
            "Major": "CSE",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
    },
    "20119048": {
            "Name": "Daivik Khona",
            "Major": "MECH",
            "Total_Attendance": 0,
            "Last_Attendance_Time": "2023-09-23 00:54:34",
            "Batch": 2020,
            "Year": 4,
            "Grade": "A"
    }
}

for key, value in data.items():
    ref.child(key).set(value)