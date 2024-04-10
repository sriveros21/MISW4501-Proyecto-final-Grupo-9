from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
#from sqlalchemy.orm import declarative_base
import uuid
from sqlalchemy.dialects.postgresql import UUID
#
 
#Base = declarative_base()
 
class Model():
   id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
   
   createdAt = Column(DateTime)
   updatedAt = Column(DateTime)
 
   def __init__(self):
       self.createdAt = datetime.now() # Revisar los formatos sugeridos
       self.updatedAt = datetime.now() # Revisar los formatos sugeridos



























# from sqlalchemy import Column, String, Integer, Enum
# from sqlalchemy.orm import declarative_base
# import enum

# Base = declarative_base()

# class TIPOIDENTIFICACION(enum.Enum):
#     CEDULA = "CEDULA"
#     TARJETA_IDENTIDAD = "TARJETA_IDENTIDAD"
#     PASAPORTE = "PASAPORTE"
#     DNI = "DNI"

# class GENERO(enum.Enum):
#     MASCULINO = "MASCULINO"
#     FEMENINO = "FEMENINO"
#     OTRO = "OTRO"

# class Usuario():
#    usuario = Column(String, primary_key=True)
#    contrasena = Column(String, nullable=False)
#    tipo_identificacion = Column(Enum(TIPOIDENTIFICACION))
#    numero_identificacion = Column(Integer, unique=True, nullable=False)
#    nombre = Column(String)
#    apellido = Column(String)
#    genero = Column(Enum(GENERO))