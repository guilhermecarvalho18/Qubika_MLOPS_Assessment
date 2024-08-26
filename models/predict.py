import pickle
import pandas as pd
from models.preprocess import preprocess_data

def load_model_and_scaler():
    """
    Load the trained model and scaler from files.
    
    Returns:
    model: The trained machine learning model.
    scaler: The scaler used for preprocessing the data.
    """
    with open("prod_exports/logistic_regression_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    with open("prod_exports/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    
    return model, scaler

def make_prediction(input_data):
    """
    Make predictions based on the input data and return a pandas Series indexed by the input data's index.
    
    Parameters:
    input_data (pd.DataFrame): The input data for which predictions are to be made.
    
    Returns:
    pd.Series: Predictions indexed by the input data's index.
    """
    # Load the model and scaler
    model, scaler = load_model_and_scaler()

    # Preprocess the input data
    processed_data = preprocess_data(input_data)

    # Ensure the input to scaler is a 2D array
    if not isinstance(processed_data, pd.DataFrame):
        processed_data = pd.DataFrame(processed_data)
        
    # Scale the input data
    scaled_data = scaler.transform(processed_data)

    # Make predictions
    predictions = model.predict(scaled_data)

    # Return predictions as a pandas Series, indexed by the input data's index
    return pd.Series(predictions, index=input_data.index)
