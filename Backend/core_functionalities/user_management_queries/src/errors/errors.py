class ApiError(Exception):
    code = 422
    description = "Default message"


# 1. Errores en la creación de usuarios
class InvalidParams(ApiError):
    code=400
    description="Pending username, password or email fields"

class EmailUsernameExist(ApiError):
    code=412
    description="Email or username already exist"


# 2. Errores en la actualización de usuarios

# 400	Si la petición no contiene al menos uno de los campos esperados.
class InvalidParamsUpdate(ApiError):
    code=400
    description="All fields are required"

# 404	En el caso que el usuario con id no exista.
class UserDoesntExist(ApiError):
    code=404
    description="User doesn't exist"

# 3. Errores en la generación de Token
class InvalidUserPass(ApiError):
    code=404
    description="Username or password invalid or status is Not Verificated"

class InvalidStateUser(ApiError):
    code=401
    description="El usuario no ha sido verificado."

class PwdUsnReq(ApiError):
    code=400
    description="The username and password fields are required"


# 4. Errores en consultar información del usuario 

# 401	El token no es válido o está vencido.
class InvalidTokenGetUser(ApiError):
    code=401
    description="El token no es válido o está vencido"

# 403	El token no está en el encabezado de la solicitud.
class NoTokenGetUser(ApiError):
    code=403
    description="El token no está en el encabezado de la solicitud."