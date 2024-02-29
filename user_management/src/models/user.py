from marshmallow import Schema, fields
from  sqlalchemy  import  Column, String, Integer, DateTime, CheckConstraint, Enum
from .model  import  Model
from .database import Base
import bcrypt, enum

class StatusUser(enum.Enum):
    POR_VERIFICAR="POR_VERIFICAR"
    NO_VERIFICADO="NO_VERIFICADO"
    VERIFICADO="VERIFICADO"

# Extender la clase Model proporcionada
class User(Model, Base):
    __tablename__  =  'user'
    username=Column(String, unique=True, nullable=False)
    email=Column(String, unique=True, nullable=False)
    phoneNumber=Column(String)
    dni=Column(String)
    fullName=Column(String)
    password=Column(String, nullable=False)
    salt=Column(String)
    token=Column(String)
    status=Column(Enum(StatusUser))
    expireAt=Column(DateTime)

    # Agregando restricción para que el campo no contenga espacios
    __table_args__ = (
        CheckConstraint("username !~* '\\s'", name='no_espacios'),
        CheckConstraint(
            "email ~* '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'",
            name='formato_correo'
        ),
        )
    
    def set_password(self, pwd):
        self.salt = bcrypt.gensalt()
        pwd = bcrypt.hashpw(pwd.encode('utf-8'), self.salt)
        self.password = pwd.decode('utf-8')
    
    def  __init__(self, username, email, phoneNumber, dni, fullName, pwd, status):
        Model.__init__(self)
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber
        self.dni = dni
        self.fullName = fullName
        self.set_password(pwd)
        self.status = status

        #self.password = set_password(pwd)
        #self.salt = salt
        #self.token = token
        #self.status = status
        #self.expireAt = expireAt


# Especificar los campos que estarán presentes al serializar el objeto como JSON.
class  UserSchema(Schema):
    id =fields.Str()
    username = fields.Str()
    email = fields.Str()
    phoneNumber = fields.Str()
    dni = fields.Str()
    fullName = fields.Str()
    password = fields.Str()
    salt = fields.Str()
    token = fields.Str()
    status = fields.Str()
    expireAt= fields.DateTime()
    createdAt= fields.DateTime()
    updatedAt= fields.DateTime()

class  UserSchema2(Schema):
    id =fields.Str()
    username = fields.Str()
    email = fields.Str()
    fullName = fields.Str()
    dni = fields.Str()
    phoneNumber = fields.Str()
    status = fields.Function(lambda o : o.status.value )








