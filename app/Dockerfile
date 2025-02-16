# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container for dependency installation
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project code into the container
COPY . .

# Expose port 8000 so the container can serve the API
EXPOSE 8000

# Do not include your actual AIPROXY_TOKEN in the image;
# it will be provided when the container is run.
ENV AIPROXY_TOKEN=""

# Command to run your application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
