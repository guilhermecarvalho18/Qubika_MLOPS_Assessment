# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the 'api' directory to the container
COPY api /app/api

# Copy the 'models' directory to the container, as it's needed for model loading
COPY models /app/models

# Copy the 'prod_exports' directory to the container, as it contains the model and scaler files
COPY prod_exports /app/prod_exports

# Expose port 80 to the outside world
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "80"]
