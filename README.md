# 🏥 MediSense AI – Intelligent Medical Report & Prescription Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Flask](https://img.shields.io/badge/Backend-Flask-black)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green)
![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Overview

**MediSense AI** is an AI-powered healthcare assistant that helps users understand medical reports and prescriptions. It extracts text using OCR, analyzes medical reports with AI, provides personalized health recommendations, generates downloadable reports, and includes healthcare management features such as medicine reminders, health analytics, emergency profiles, and an AI chatbot.

This project was developed as a healthcare innovation project for the **Samsung Innovation Campus Hackathon**.

---

# 🚀 Features

### 📄 Medical Report Upload

* Upload medical reports (Image/PDF)
* Secure file handling
* Automatic report processing

### 🔍 OCR Text Extraction

* EasyOCR-based text extraction
* Prescription recognition
* Medical report parsing
* Image preprocessing

### 🤖 AI Report Analysis

* Google Gemini AI integration
* Medical report explanation
* Health insights
* Doctor-friendly summaries

### 💊 Prescription Analyzer

* Medicine detection
* Dosage extraction
* Medicine information
* Prescription interpretation

### 💬 AI Healthcare Chatbot

* AI-powered medical assistant
* Health-related question answering
* General wellness guidance

### 🍎 Personalized Recommendations

* BMI Calculator
* Diet Planner
* Exercise Suggestions
* Hydration Tracking
* Sleep Recommendations
* Lifestyle Improvement Tips

### 📊 Health Analytics

* Health Score
* Progress Tracking
* Trend Analysis
* Timeline Visualization
* Report Comparison
* Medical Insights Dashboard

### ⏰ Smart Medicine Reminders

* Medicine reminders
* Water reminders
* Sleep reminders
* Exercise reminders
* Notification scheduler

### 🎤 Voice Assistant

* Speech-to-Text
* Text-to-Speech
* Voice Commands
* Multi-language support (planned)

### 🚨 Emergency Features

* Emergency Profile
* Emergency Contacts
* QR Code Generation
* Emergency PDF Export

### 📄 PDF Export

* AI Medical Summary
* Doctor Report
* Emergency Card
* Downloadable Health Reports

---

# 🏗️ Project Structure

```text
MediSense-AI/
│
├── analytics/
├── backend/
├── docs/
├── emergency/
├── exports/
├── frontend/
├── models/
├── ocr/
├── pdf/
├── recommendation/
├── reminder/
├── voice/
│
├── README.md
├── requirements.txt
├── Dockerfile
├── LICENSE
├── .gitignore
└── run.py
```

---

# 🛠️ Tech Stack

### Frontend

* Streamlit
* HTML
* CSS
* Python

### Backend

* Flask
* REST API

### Database

* MongoDB Atlas

### Artificial Intelligence

* Google Gemini API
* EasyOCR

### Python Libraries

* OpenCV
* Pillow
* Pandas
* ReportLab
* FPDF
* NumPy
* PyMongo
* QRCode

---

# 📷 Application Modules

* Home
* Login & Registration
* Dashboard
* Upload Medical Report
* OCR Result
* Prescription Analyzer
* Medicine Scanner
* AI Report Analysis
* AI Chatbot
* Diet Planner
* Health Analytics
* Medicine Reminders
* Profile Management
* About

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/MediSense-AI.git

cd MediSense-AI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file inside the `backend` folder.

```env
MONGO_URI=your_mongodb_connection_string

GEMINI_API_KEY=your_google_gemini_api_key

SECRET_KEY=your_secret_key
```

---

## Run Backend

```bash
cd backend

python app.py
```

---

## Run Frontend

```bash
cd frontend

streamlit run app.py
```

---

# 📸 Screenshots

Add screenshots inside:

```text
docs/screenshots/
```

Recommended screenshots:

* Home Page
* Login
* Dashboard
* Upload Report
* OCR Result
* AI Report Analysis
* AI Chatbot
* Health Analytics
* Emergency QR
* Medicine Reminder

---

# 🔮 Future Enhancements

* AI Disease Risk Prediction
* Wearable Device Integration
* Hospital Appointment Booking
* Doctor Recommendation System
* Blood Report Trend Prediction
* Voice-Based Consultation
* Multi-language Translation
* Cloud Deployment
* Health Risk Scoring
* AI Symptom Checker

---

# 👩‍💻 Team

**Samsung Innovation Campus Hackathon Project**

Project Name:

**MediSense AI – Intelligent Medical Report & Prescription Analyzer**

---

# 🤝 Contributing

Contributions, feature suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you found this project helpful:

⭐ Star the repository

🍴 Fork the project

💡 Share your feedback

---

## Thank You ❤️

**Building AI-powered healthcare solutions for a healthier future.**
