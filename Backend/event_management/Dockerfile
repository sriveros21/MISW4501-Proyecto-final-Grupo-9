# Usar una imagen base de Python
FROM python:3.11

WORKDIR /event_management

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /event_management

# Comando para ejecutar la aplicación Flask
CMD ["python", "-m", "src.main"]