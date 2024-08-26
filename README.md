# Machine Learning Model Deployment

## Overview

This project demonstrates the deployment of a machine learning model using FastAPI. The project is designed to be cloud-agnostic, enabling deployment across various cloud providers (AWS, GCP, Azure) with minimal configuration changes. 

**Note**: Due to time constraints, the logging/monitoring features and the CI/CD deployment were not fully implemented. However, the structure and initial configurations are in place to support these features in the future. 
## Features 

- **Cloud-Agnostic Deployment**: The project is containerized using Docker and can be deployed on any cloud platform that supports containers. 
- **Logging and Monitoring**: Initial setup for logging and monitoring is included, but further implementation is needed. 
- **CI/CD Pipeline**: The CI/CD pipeline structure is provided, with plans for automated testing, linting, model validation, containerization, and deployment.

## Project Structure

```plaintext
Qubika_MLOPS_Assessment/
├── api/
│   ├── __init__.py
│   ├── app.py                         # FastAPI application with endpoints
├── models/
│   ├── __init__.py
│   ├── model.py                       # Machine learning model code
│   ├── preprocess.py                  # Data preprocessing code
│   ├── predict.py                     # Prediction logic
├── prod_exports/
│   ├── logistic_regression_model.pkl  # Serialized model
│   ├── scaler.pkl                    # Serialized scaler
├── storage/
│   ├── __init__.py
│   └── storage_manager.py             # StorageManager class for cloud-agnostic storage
├── tests/
│   ├── test_api.py                    # Unit tests for the API endpoints
│   └── test_model.py                  # Unit tests for the model
├── infra/
│   ├── terraform/                     # Terraform scripts for cloud-agnostic infrastructure
├── main.tf                    # Main Terraform configuration file
├── Dockerfile                 # Dockerfile for building the application container
├── .gitignore                         # Git ignore file
├── README.md                          # Project documentation
├── LICENSE                            # License 
├── config.yaml                    # Configuration file for environment-specific settings
├── requirements.txt            # Python dependencies
```
Getting Started
---------------

### Prerequisites

-   **Docker**: Ensure Docker is installed and running on your machine.
-   **Python**: Make sure Python 3.11 or later is installed.
-   **Terraform**: (Optional) For infrastructure provisioning.
## Model Pipeline Enhancements

### Implementation of Standard Scaler

During the development of the model pipeline, it was necessary to implement a standard scaler to normalize the features before feeding them into the model. This decision was based on the following considerations:

- **Feature Scaling**: The original dataset contained features with varying scales (e.g., `Annual Income` could be in the range of tens of thousands, while `Credit Score` might range from 300 to 850). Without scaling, the model could be biased towards features with larger numerical ranges, potentially impacting its performance.
  
- **Model Performance**: Many machine learning models, including logistic regression (used in this project), perform better when the input features are standardized. Standard scaling (which transforms features to have a mean of 0 and a standard deviation of 1) helps the model converge faster and potentially achieve better accuracy.

### Updated Model Pipeline

The model pipeline was adjusted to include the following steps:

1. **Data Preprocessing**:
   - Handling of missing values using imputation.
   - **Standard Scaling**: All numerical features are scaled using `StandardScaler` from `scikit-learn`.

2. **Model Training**:
   - The preprocessed and scaled data is used to train a logistic regression model.

3. **Prediction**:
   - For predictions, the input data is first scaled using the same scaler before being passed to the model.

### Installation

1.  **Clone the Repository**:

    ```bash
    git clone https://github.com/guilhermecarvalho18/Qubika_MLOPS_Assessment.git
    cd Qubika_MLOPS_Assessment
    ```

2.  **Set Up the Environment**:

    Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate``
    ```

    Install the dependencies:

    ```bash
    pip install -r requirements.txt`
    ```

3.  **Configure Environment Variables**:

    Set up environment variables for cloud provider configuration (e.g., AWS S3, GCP Storage):

    ```bash
    export STORAGE_PROVIDER=aws
    export BUCKET_NAME=my-s3-bucket
    export DATABASE_URL=postgresql://user:password@hostname/dbname
    ```

### Running the Application

1.  **Locally with FastAPI**:

    Start the FastAPI application locally:

    ```bash
    uvicorn api.app:app --host 127.0.0.1 --port 8080 --reload
    ```
    The application will be available at `http://127.0.0.1:8080`.

2.  **Using Docker**:

    Build and run the Docker container:

    ```bash
    docker build -t my-fastapi-app .
    docker run -d -p 8080:80 my-fastapi-app
    ```
    Access the application at `http://localhost:8080`.

### Running Tests

1.  **Unit Tests**:

    Run the unit tests using `pytest`:

    ```bash
    python -m unittest discover tests/  
    ```   


### Deployment

1.  **CI/CD Pipeline with GitHub Actions**:

    The project includes a GitHub Actions workflow for CI/CD. The pipeline performs the following steps:

    -   Linting and formatting checks.
    -   Running unit tests.
    -   Building and pushing Docker images to Docker Hub.
    -   Deploying the application to a Kubernetes cluster.
2.  **Infrastructure as Code with Terraform**:

    Use Terraform to provision cloud resources:

    ```bash
    terraform init
    terraform apply
    ```    

### Logging and Monitoring

1.  **Logging**:

    Logs are structured and can be aggregated using a centralized logging service like AWS CloudWatch, GCP Stackdriver, or ELK Stack.

2.  **Monitoring**:

    Health checks are exposed at `/health`. Metrics can be collected using Prometheus, and alerts can be configured based on log patterns or performance metrics.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

-   Thanks to the open-source community for providing excellent tools and resources that made this project possible.