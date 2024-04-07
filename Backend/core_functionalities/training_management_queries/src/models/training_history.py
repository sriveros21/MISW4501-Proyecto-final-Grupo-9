from marshmallow import Schema, fields
from  sqlalchemy  import  Column, String, DateTime
# from .model  import  Model
from .database_queries import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
 

class TrainingHistory(Base):
    __tablename__  =  'training_history'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(DateTime)
    username=Column(String, nullable=False)
    sport=Column(String)
    time=Column(String)
    distance=Column(String)
    weight=Column(String, nullable=False)
    intensity=Column(String)
    series=Column(String)
    calories=Column(String)
   
    def  __init__(self, date, username, sport, time, distance, weight, intensity, series, calories):
        self.date = date
        self.username = username
        self.sport = sport
        self.time = time
        self.distance = distance
        self.weight = weight
        self.intensity = intensity
        self.series = series
        self.calories = calories


class  TrainingHistorySchema(Schema):
    id = fields.Str()
    date = fields.DateTime()
    username = fields.Str()
    sport = fields.Str()
    time = fields.Str()
    distance = fields.Str()
    weight = fields.Str()
    intensity = fields.Str()
    series = fields.Str()
    calories = fields.Str()




 



























# from sqlalchemy import Column, String, Integer, ForeignKey
# from marshmallow import Schema, fields
# from  sqlalchemy  import  Column, String, Integer
# from .model  import  Usuario
# from .database import Base
# from sqlalchemy.orm import relationship

# class DeportistasNoProfesionales(Usuario, Base):

#     __tablename__  =  'desportitas_no_profesionales'
#     id_deporte = Column(String)
#     edad = Column(String, unique=True, nullable=False)
#     peso = Column(String, unique=True, nullable=False)
#     altura = Column(String, unique=True, nullable=False)
#     pais_ciudad_nacimiento = Column(String)
#     pais_ciudad_residencia = Column(String, ForeignKey('ciudades.id'))
#     antiguedad_residencia = Column(Integer)


#     def  __init__(
#             self,
#             usuario,
#             contrasena,
#             tipo_identificacion,
#             numero_identificacion,
#             nombre,
#             apellido,
#             genero,
#             pais_ciudad_residencia,
#             antiguedad_residencia,
#             id_deporte,
#             edad,
#             peso,
#             altura,
#             pais_cioudad_nacimiento,
#         ):
#         Usuario.__init__(self)
#         self.usuario = usuario
#         self.contrasena = contrasena
#         self.tipo_identificacion = tipo_identificacion
#         self.numero_identificacion = numero_identificacion
#         self.nombre = nombre
#         self.apellido = apellido
#         self.antiguedad_residencia = antiguedad_residencia
#         self.genero = genero
#         self.pais_ciudad_residencia = pais_ciudad_residencia
#         self.id_deporte = id_deporte
#         self.edad = edad
#         self.peso = peso
#         self.altura = altura
#         self.pais_cioudad_nacimiento = pais_cioudad_nacimiento


# class  DeportistaNoProfesionalesSchema(Schema):
#     usuario = fields.Str()
#     contrasena = fields.Str()
#     tipo_identificacion = fields.Str()
#     numero_identificacion = fields.Str()
#     nombre = fields.Str()
#     apellido = fields.Str()
#     antiguedad_residencia = fields.Str()
#     genero = fields.Str()
#     pais_ciudad_residencia = fields.Str()
#     id_deporte = fields.Str()
#     edad = fields.Str()
#     peso = fields.Str()
#     altura = fields.Str()
#     pais_cioudad_nacimiento = fields.Str()


# class Pais(Base):
#     __tablename__  =  'paises'
#     id = Column(String, primary_key=True)
#     nombre = Column(String)
#     ciudades = relationship('Ciudad', back_populates='pais')


# class Ciudad(Base):
#     __tablename__  =  'ciudades'
#     id = Column(String, primary_key=True)
#     nombre = Column(String)
#     pais = Column(String, ForeignKey('paises.id'))
#     modelos = relationship('DeportistasNoProfesionales', back_populates='ciudad')


# class ProfesionalServiciosComplementarios(Usuario, Base):
#     pais_ciudad_residencia = Column(String, ForeignKey('ciudades.id'))
#     antiguedad_residencia = Column(Integer)
#     __tablename__  =  'profesionales_servicios_complementarios'
#     def  __init__(
#             self,
#             usuario,
#             contrasena,
#             tipo_identificacion,
#             numero_identificacion,
#             nombre,
#             apellido,
#             antiguedad_residencia,
#             genero,
#             pais_ciudad_residencia,
#         ):
#         Usuario.__init__(self)
#         self.usuario = usuario
#         self.contrasena = contrasena
#         self.tipo_identificacion = tipo_identificacion
#         self.numero_identificacion = numero_identificacion
#         self.nombre = nombre
#         self.apellido = apellido
#         self.antiguedad_residencia = antiguedad_residencia
#         self.genero = genero
#         self.pais_ciudad_residencia = pais_ciudad_residencia


# class OrganizadorEventosMasivos(Usuario, Base):
#     pais_ciudad_residencia = Column(String, ForeignKey('ciudades.id'))
#     antiguedad_residencia = Column(Integer)

#     __tablename__  =  'organizadores_eventos_masivos'   
#     def  __init__(
#             self,
#             usuario,
#             contrasena,
#             tipo_identificacion,
#             numero_identificacion,
#             nombre,
#             apellido,
#             antiguedad_residencia,
#             genero,
#             pais_ciudad_residencia,
#         ):
#         Usuario.__init__(self)
#         self.usuario = usuario
#         self.contrasena = contrasena
#         self.tipo_identificacion = tipo_identificacion
#         self.numero_identificacion = numero_identificacion
#         self.nombre = nombre
#         self.apellido = apellido
#         self.antiguedad_residencia = antiguedad_residencia
#         self.genero = genero
#         self.pais_ciudad_residencia = pais_ciudad_residencia


# class PerfilFisiologico(Base):
#     __tablename__  =  'perfiles_fisiologicos'
#     id_perfil_fisiologico = Column(String, primary_key=True)
#     etnia = Column(String) 
#     peso = Column(String)
#     altura = Column(String)
#     imc = Column(String)
#     persion_arterial = Column(String)
#     frecuencia_cardiaca = Column(String)
#     termperatura_corporal = Column(String)
#     quimica_sanguinia = Column(String)
#     funcion_pulmonar = Column(String)
#     fuerza_muscular = Column(String)
#     resistencia_cardiovascular = Column(String)
#     flexibilidad = Column(String)


# class PerfilDemografico(Base):
#     __tablename__  =  'perfiles_demograficos'
#     id_perfil_demografico = Column(String, primary_key=True)
#     estado_civil = Column(String)
#     ingresos = Column(String)
#     raza = Column(String)
#     ocupacion = Column(String)
#     religion = Column(String)
#     usuario = Column(String, ForeignKey('desportitas_no_profesionales.usuario'))




