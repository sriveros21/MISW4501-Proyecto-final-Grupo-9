from .base_command import BaseCommannd
from ..errors.errors import InvalidParams,EmailUsernameExist
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from ..models.database import db_session #, init_db
from ..models.user import User


class CreateUser(BaseCommannd):
  def __init__(self, username, password, email, dni, fullName, phoneNumber):
    self.username = username
    self.password = password
    self.email = email
    self.dni = dni
    self.fullName = fullName
    self.phoneNumber = phoneNumber

  def execute(self):
    u = User(self.username, self.email, self.phoneNumber, self.dni, self.fullName, self.password,"POR_VERIFICAR")
    db_session.add(u)
    
    if (self.username=="" or self.email=="" or self.password=="" or self.username is None or self.email is None or self.password is None ):
      raise InvalidParams
    
    else:
      try:
        db_session.commit()
        response={"id":u.id, "createdAt":u.createdAt}
        db_session.close()
        return response
      except IntegrityError  as e:
        if isinstance(e.orig, UniqueViolation):
          db_session.close()
          raise EmailUsernameExist














































# from .base_command import BaseCommannd
# from ..errors.errors import InvalidParams, EmailUsernameExist
# from sqlalchemy.exc import IntegrityError
# from psycopg2.errors import UniqueViolation
# from ..models.database import db_session 
# from ..models.users import DeportistaNoProfesional


# class CreateUser(BaseCommannd):
#   def __init__( 
#         self, 
#         tipo_identificacion,
#         numero_identificacion,
#         nombre,
#         apellido,
#         antiguedad_residencia,
#         genero,
#         pais_ciudad_residencia,
#         id_deporte,
#         edad,
#         peso,
#         altura,
#         pais_cioudad_nacimiento,
#         contrasena,
#       ):
#     self.tipo_identificacion = tipo_identificacion 
#     self.numero_identificacion = numero_identificacion 
#     self.nombre = nombre 
#     self.apellido = apellido 
#     self.antiguedad_residencia = antiguedad_residencia 
#     self.genero = genero 
#     self.pais_ciudad_residencia = pais_ciudad_residencia 
#     self.id_deporte = id_deporte 
#     self.edad = edad 
#     self.peso = peso 
#     self.altura = altura 
#     self.pais_cioudad_nacimiento = pais_cioudad_nacimiento 
#     self.contrasena = contrasena 

#   def execute(self):
#     usuario_nuevo = DeportistaNoProfesional(
#       self.tipo_identificacion,
#       self.numero_identificacion,
#       self.nombre,
#       self.apellido,
#       self.antiguedad_residencia,
#       self.genero,
#       self.pais_ciudad_residencia,
#       self.id_deporte,
#       self.edad,
#       self.peso,
#       self.altura,
#       self.pais_cioudad_nacimiento,
#       self.contrasena,
#     )
    
#     db_session.add(usuario_nuevo)
    
#     if (
#         self.tipo_identificacion == "" or
#         self.numero_identificacion == "" or
#         self.nombre == "" or
#         self.apellido == "" or
#         self.antiguedad_residencia == "" or
#         self.genero == "" or
#         self.pais_ciudad_residencia == "" or
#         self.id_deporte == "" or
#         self.edad == "" or
#         self.peso == "" or
#         self.altura == "" or
#         self.pais_cioudad_nacimiento == "" or
#         self.contrasena == "" 
#        ):
#       raise InvalidParams
    
#     else:
#       try:
#         db_session.commit()
#         response = {"id":usuario_nuevo.numero_identificacion, "Nombre":usuario_nuevo.nombre}
#         db_session.close()

#         return response
#       except IntegrityError  as e:
#         if isinstance(e.orig, UniqueViolation):
#           db_session.close()
#           raise EmailUsernameExist

