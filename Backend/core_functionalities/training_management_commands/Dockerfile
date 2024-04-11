# Usar una imagen base de Python
FROM python:3.11

WORKDIR /training_management_commands

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /training_management_commands

# Comando para ejecutar la aplicación Flask
CMD ["python", "-m", "src.main"]