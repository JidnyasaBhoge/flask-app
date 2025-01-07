# Use Python as the base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask's port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
