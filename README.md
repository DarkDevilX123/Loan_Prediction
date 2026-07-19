# 🏦 Loan Approval Prediction System

**Python | FastAPI | HTML | CSS | Scikit-learn**

An end-to-end Machine Learning project that predicts whether a loan application will be approved based on applicant details such as gender, marital status, education, income, loan amount, credit history, and property area.

The project uses a trained Machine Learning classification model served through a FastAPI backend, while an interactive HTML/CSS frontend allows users to enter applicant information and receive instant loan approval predictions.

---

## ✨ Features

- Loan approval prediction using Machine Learning
- FastAPI REST API backend
- Interactive HTML/CSS user interface
- Data preprocessing and feature engineering
- Real-time prediction with confidence score
- Model saved using Joblib

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Joblib

### Data Analysis
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Backend
- FastAPI
- Uvicorn

### Frontend
- HTML5
- CSS3

---

## 📂 Project Structure

```
Loan_Approval_Prediction/
│
├── app.py                 # FastAPI backend
├── index.html             # HTML frontend
├── loan_model.pkl         # Trained ML model
├── train.csv              # Training dataset
├── test.csv               # Testing dataset
├── loan_prediction.ipynb  # Model training notebook
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The project uses the **Loan Prediction Dataset**.

### Input Features

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

### Target

- Loan Status (Approved / Rejected)

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/DarkDevilX123/Loan_Approval_Prediction.git
```

Move into the project folder

```bash
cd Loan_Approval_Prediction
```

Install the required libraries

```bash
pip install numpy pandas matplotlib seaborn scikit-learn joblib fastapi uvicorn
```

---

## ▶️ Run the Application

Start the FastAPI server

```bash
uvicorn app:app --reload
```

Open the HTML frontend in your browser and submit the form.

FastAPI runs at

```
http://127.0.0.1:8000
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

## 🤖 Machine Learning Model

- Algorithm: Decision Tree Classifier
- Model Serialization: Joblib
- Backend: FastAPI
- Frontend: HTML & CSS

---

## 👨‍💻 Author

**Athul Krishna Biju**

---

## 📄 License

This project is developed for educational and learning purposes.
