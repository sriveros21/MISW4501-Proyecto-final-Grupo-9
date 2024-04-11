# Usar una imagen base de Python
FROM python:3.11

WORKDIR /services_management

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /services_management

# Comando para ejecutar la aplicación Flask
CMD ["python", "-m", "src.main"]