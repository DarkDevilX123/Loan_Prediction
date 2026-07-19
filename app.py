from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
import joblib

app = FastAPI(title="Loan Approval Prediction API")

# Load trained model
model = joblib.load("loan_model.pkl")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Loan Prediction API</title>
    </head>
    <body style="font-family:Arial;text-align:center;padding-top:100px;background:#111;color:white;">
        <h1>Loan Approval Prediction API</h1>
        <h2>Open your HTML page and submit the form.</h2>
    </body>
    </html>
    """


@app.post("/predict", response_class=HTMLResponse)
async def predict(

    Gender: int = Form(0),
    Married: int = Form(0),
    Dependents: int = Form(0),
    Education: int = Form(0),
    Self_Employed: int = Form(0),
    Credit_History: float = Form(0),
    Property_Area: int = Form(0),
    Loan_Amount_Term: float = Form(360),
    LoanAmount: float = Form(1),
    ApplicantIncome: float = Form(1),
    CoapplicantIncome: float = Form(0)

):

    total_income = ApplicantIncome + CoapplicantIncome

    if LoanAmount <= 0:
        LoanAmount = 1

    if total_income <= 0:
        total_income = 1

    loan_amount_log = np.log(LoanAmount)
    total_income_log = np.log(total_income)

    input_data = pd.DataFrame([{
        "Gender": Gender,
        "Married": Married,
        "Dependents": Dependents,
        "Education": Education,
        "Self_Employed": Self_Employed,
        "Loan_Amount_Term": Loan_Amount_Term,
        "Credit_History": Credit_History,
        "Property_Area": Property_Area,
        "LoanAmount_log": loan_amount_log,
        "TotalIncome_log": total_income_log
    }])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    approval = probability[1] * 100
    rejection = probability[0] * 100

    if prediction == 1:
        result = "✅ LOAN APPROVED"
        color = "#00ff66"
        percent = approval
    else:
        result = "❌ LOAN REJECTED"
        color = "#ff3333"
        percent = rejection

    return f"""
    <!DOCTYPE html>
    <html>

    <head>

    <title>Prediction Result</title>

    <style>

    body{{
        background:#000;
        color:white;
        font-family:Arial;
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
    }}

    .card{{
        width:550px;
        background:#111;
        border:2px solid red;
        border-radius:15px;
        padding:40px;
        text-align:center;
        box-shadow:0px 0px 25px red;
    }}

    h1{{
        color:{color};
    }}

    h2{{
        color:white;
    }}

    h3{{
        color:yellow;
        font-size:40px;
    }}

    a{{
        display:inline-block;
        margin-top:20px;
        padding:12px 25px;
        background:red;
        color:white;
        text-decoration:none;
        border-radius:10px;
    }}

    </style>

    </head>

    <body>

        <div class="card">

            <h1>{result}</h1>

            <h2>Prediction Confidence</h2>

            <h3>{percent:.2f}%</h3>

            <a href="javascript:history.back()">Predict Again</a>

        </div>

    </body>

    </html>
    """