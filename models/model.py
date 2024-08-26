import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from models.preprocess import preprocess_data 
import pickle

# Load dataset and preprocess the data
df = pd.read_csv("data/dataset.csv")
df_imputed = preprocess_data(df)

# Splitting the data into features and target
X = df_imputed.drop('Loan_Approval', axis=1)
y = df_imputed['Loan_Approval']

# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

# Scaling the features to avoid the algorithm to struggle to converge due to differences in 
# features ranges
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Training the Logistic Regression model
src = LogisticRegression()
src.fit(X_train, y_train)

# Predictions
y_pred = src.predict(X_test)
print(y_pred)

# Saving the trained model to a file
with open("prod_exports/logistic_regression_model.pkl", "wb") as f:
    pickle.dump(src, f)

# Save the scaler to a file
scaler_path = os.path.join("prod_exports/scaler.pkl")
with open(scaler_path, "wb") as f:
    pickle.dump(scaler, f)

print("Model and scaler trained and saved.")
