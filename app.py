import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("loan_model.pkl", "rb"))

# Page Configuration
st.set_page_config(
    page_title="CreditWise Loan Approval",
    page_icon="🏦",
    layout="wide"
)

# Sidebar
st.sidebar.title("🏦 CreditWise Bank")

st.sidebar.info(
    """
    AI-Powered Loan Approval System

    Predict whether a loan should be:
    ✅ Approved
    ❌ Rejected
    """
)

st.sidebar.success("Machine Learning Project")

# Main Title
st.title("🏦 CreditWise Loan Approval System")

st.markdown(
    "### Intelligent Loan Approval Prediction using Machine Learning"
)

# Project Description
st.info(
    "This AI-powered system predicts whether a loan application should be approved or rejected based on applicant financial details."
)

st.write("---")

# Create 2 Columns
col1, col2 = st.columns(2)

# Left Column
with col1:

    income = st.number_input(
        "💰 Applicant Income",
        min_value=0.0
    )

    credit_score = st.slider(
        "📈 Credit Score",
        300,
        900,
        700
    )

    existing_loans = st.selectbox(
        "🏦 Existing Loans",
        [0, 1, 2, 3, 4, 5]
    )

# Right Column
with col2:

    savings = st.number_input(
        "💵 Savings",
        min_value=0.0
    )

    loan_amount = st.number_input(
        "📌 Loan Amount",
        min_value=0.0
    )

    age = st.slider(
        "🎂 Age",
        18,
        60,
        25
    )

st.write("---")

# Prediction Button
if st.button("🔍 Predict Loan Approval"):

    # Prepare input data
    input_data = np.array([
        [
            income,
            credit_score,
            existing_loans,
            savings,
            loan_amount,
            age
        ]
    ])

    # Prediction
    prediction = model.predict(input_data)

    st.subheader("Prediction Result")

    # Output Result
    if prediction[0] == 1:

        st.success(
            "✅ Loan Approved: Applicant is likely eligible for the loan."
        )

        st.balloons()

    else:

        st.error(
            "❌ Loan Rejected: Applicant may not meet loan eligibility criteria."
        )

st.write("---")

# Footer
st.markdown(
    "Made with ❤️ using Machine Learning and Streamlit"
)