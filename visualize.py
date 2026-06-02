import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("loan_data.csv")

# Count approved/rejected loans
loan_counts = df["Loan_Approved"].value_counts()

# Plot
plt.figure(figsize=(5,5))

plt.pie(
    loan_counts,
    labels=["Approved", "Rejected"],
    autopct="%1.1f%%"
)

plt.title("Loan Approval Distribution")

plt.show()