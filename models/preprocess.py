import pandas as pd
from sklearn.impute import SimpleImputer

def preprocess_data(df, impute_value=0):
    """
    Preprocess the input dataframe by imputing missing values.
    
    Args:
    - df (pd.DataFrame): The input dataframe to preprocess.
    - impute_value (int, float, or str): The value used to fill missing data. Default is 0.
    
    Returns:
    - pd.DataFrame: The preprocessed dataframe with imputed values.
    """
    # Identify columns with missing values
    columns_with_null = df.columns[df.isnull().any()]

    # Create an imputer object with the specified fill value
    imputer = SimpleImputer(strategy="constant", fill_value=impute_value)

    # Apply imputation on columns with missing values
    df_imputed = df.copy()
    df_imputed[columns_with_null] = imputer.fit_transform(df_imputed[columns_with_null])

    return df_imputed

if __name__ == "__main__":
    # Test code or script logic to run when preprocess.py is executed directly
    
    # Example: Load a test dataset to preprocess
    test_data = pd.DataFrame({
        "Age": [25, None, 30],
        "Annual_Income": [50000, 60000, None],
        "Credit_Score": [700, None, 650]
    })

    print("Original Data:")
    print(test_data)

    # Preprocess the data
    processed_data = preprocess_data(test_data)

    print("\nProcessed Data:")
    print(processed_data)

