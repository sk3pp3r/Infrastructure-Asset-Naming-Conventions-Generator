# Dockerfile for Streamlit Application

# Specify the base image
#FROM python:3.7
FROM python:latest

# Maintainer
LABEL maintainer="Haim Cohen <haim1979n@gmail.com>"

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Expose port
EXPOSE 8501

# Run Streamlit
CMD streamlit run app.py
