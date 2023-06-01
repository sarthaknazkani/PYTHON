# Base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code to the container
COPY . .

# Expose the port that the app will run on
EXPOSE 5000

# Start the app
CMD ["python", "main.py"]
