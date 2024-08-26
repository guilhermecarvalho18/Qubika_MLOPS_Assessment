from fastapi import FastAPI, HTTPException, File, UploadFile
import pandas as pd
from models.predict import make_prediction  
from io import StringIO

app = FastAPI()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Read the uploaded CSV file
        contents = await file.read()
        # Convert the CSV content into a DataFrame
        input_data = pd.read_csv(StringIO(contents.decode('utf-8')))
        # Generate predictions
        predictions = make_prediction(input_data)
        # Return predictions as a list
        return {"predictions": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
