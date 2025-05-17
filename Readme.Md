# 🎓 Smart Campus Face Recognition System

A smart desktop application designed to identify students in a campus environment using face recognition. The system helps maintain discipline by allowing faculty members to register students, recognize faces in real-time using webcam, and log any misbehavior incidents with historical tracking via Excel logs.

This system was developed to address increasing incidents of student misbehavior in school and college campuses. Faculty can scan a student's face, retrieve identity details, and instantly log a complaint that is stored permanently.

---

## 📁 Project Structure


SmartCampusFaceRecognition/
│
├── main.py                      # 🔧 Main GUI application using CustomTkinter
├── database.py                  # 🔗 MongoDB operations (add, get, update, delete students and admins)
├── face_recognition.py          # 🤖 Handles face detection, training, recognition, misbehavior logging
├── auth.py                      # 🔐 Admin authentication logic
├── requirements.txt             # 📦 Required Python packages
├── main.spec                    # 🐍 PyInstaller build spec for generating EXE
├── students.db                  # 🗃 Optional local DB file (if used)
│
├── misbehaviour_log.xlsx        # 📄 Excel file storing logged complaints
├── assets/                      # 🎨 UI background images and assets
├── dataset/                     # 🧠 Trained LBPH face recognition model (trainer.yml)
├── haarcascade/                 # 👁 Face detection XML (Haar Cascade)
│   └── haarcascade_frontalface_default.xml
├── images/                      # 🖼 Captured face images of students


---

## ✨ Features

✅ Student Registration with passport-size photo, roll number & contact

✅ Face Training using OpenCV's LBPH recognizer

✅ Real-time Face Recognition from webcam

✅ Misbehavior Logging with date, time, and reason

✅ View Logs & Misbehavior History per student

✅ Admin Login & Registration System

✅ Export all student data to CSV

✅ Stylish CustomTkinter GUI interface

---

## 🧠 How It Works

1. Admin logs in to the system
2. Admin registers student by entering details and capturing face image
3. Admin trains the model using "Train Faces"
4. In recognition:

   * Face is matched using OpenCV’s LBPH recognizer
   * If recognized, details are shown
   * Admin can optionally file a complaint
5. Complaint is stored in misbehaviour_log.xlsx

---

## 🛠 Setup Instructions

### 1. Install Required Packages

bash
pip install -r requirements.txt


Make sure to install OpenCV with contrib:

bash
pip install opencv-contrib-python


### 2. Run the Application

bash
python main.py


---

## 🔁 Recognition & Logging Flow

1. 🧑 Face detected using Haar Cascade
2. 🧠 Compared with trained LBPH model
3. ✅ Student info shown if match found
4. 📝 Admin logs misbehavior (optional)
5. 📊 Logs stored in Excel with timestamp

---

## 📸 Face Recognition Logic

* Haar Cascade for face detection (frontal)
* LBPH for recognition and ID assignment
* Model trained and saved to dataset/trainer.yml

---

## 💡 Technologies Used

| Component        | Tech                |
| ---------------- | ------------------- |
| GUI              | CustomTkinter       |
| Face Detection   | OpenCV Haar Cascade |
| Face Recognition | LBPH (OpenCV)       |
| Storage          | MongoDB             |
| Admin Auth       | bcrypt (hashed pwd) |
| Logging          | Excel (openpyxl)    |

---

## 🚨 Use Case

This tool helps teachers track misbehaving students quickly and easily by:

* Scanning a student's face
* Identifying them automatically
* Logging a complaint with context
* Keeping historical records of behavior

---

## 🛡 Future Enhancements

* 🌐 Add cloud backup for logs
* 📊 Analytics dashboard (complaint trends)
* 📲 Mobile app integration with Flutter
* 👮 Role-based access (professor / principal)
* 📥 Email alerts on repeated violations

---

## 👩‍💻 Author & License

*Author*: Pooja Jain
📧 Email: [akashsharmapersonal12186@gmail.com](mailto:akashsharmapersonal12186@gmail.com)

*License*: MIT License © 2025

---

## 🙋‍♂ Support

If you find this helpful or need a custom version, feel free to contact me via email.