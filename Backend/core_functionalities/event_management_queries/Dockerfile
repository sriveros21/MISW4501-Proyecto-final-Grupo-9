# Usar una imagen base de Python
FROM python:3.11

WORKDIR /event_management_queries

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /event_management_queries

# Set environment variables
# FLASK_APP is used to specify how to load the application. 
# This should be the name of your Flask app's main module or package.
ENV FLASK_APP=src.main
# Optional: Set to development if you want debug mode on by default
ENV FLASK_ENV=development

# Command to run the Flask application
# Use flask run and specify the host to run on all network interfaces inside the container
CMD ["flask", "run", "--host=0.0.0.0", "--port=3002"]