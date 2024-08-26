from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_predict():
    # Prepare the CSV content
    csv_content = """Age,Annual_Income,Credit_Score,Loan_Amount,Number_of_Open_Accounts
30,73198,414,35636,3
45,54000,630,25000,5
"""
    # Simulate uploading the CSV file
    response = client.post(
        "/predict/",
        files={"file": ("input.csv", csv_content, "text/csv")}
    )
    
    assert response.status_code == 200
    assert "predictions" in response.json()
