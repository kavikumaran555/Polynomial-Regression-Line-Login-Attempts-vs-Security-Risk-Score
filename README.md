# Polynomial-Regression-Line-Login-Attempts-vs-Security-Risk-Score

📘 Project Overview

The goal of this project is to explore how an increase in login attempts may impact the security risk level of an employee account.
Instead of assuming a straight-line relationship, Polynomial Regression helps capture non-linear patterns between the two variables.

🧠 Key Concepts

Polynomial Features:
Expands the original input variable (Login_Attempts) into multiple polynomial terms to capture complex, curved relationships.

Linear Regression on Polynomial Data:
After transforming the data, a simple Linear Regression model is trained on these polynomial features.

Visualization:
The actual data points, predicted values, and the regression curve are plotted using Matplotlib.

Model Evaluation:
The R² score is calculated to measure how well the model fits the data.

⚙️ Technologies Used

Python

pandas

numpy

matplotlib

scikit-learn

🧩 Code Explanation
Steps Followed:

Import required libraries

Read the dataset (employee_login_attempt_data.csv)

Define input (Login_Attempts) and output (Security_Risk_Score) variables

Apply polynomial feature transformation

Train a linear regression model

Predict the results

Visualize:

Blue dots → Actual data

Red dots → Predicted data

Green line → Regression curve

Print R² Score for model accuracy

📊 Sample Output

Graph: A curved regression line fitting the scattered data points

Console Output:

R2 Score: 0.94

🧾 Example Use Case

This model can be used by security teams to understand how user behavior (like repeated login attempts) might relate to the risk of suspicious activity, helping identify unusual login patterns.
