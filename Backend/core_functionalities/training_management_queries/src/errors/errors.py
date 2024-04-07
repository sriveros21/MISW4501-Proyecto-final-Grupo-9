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


# 401	El token no es válido o está vencido.
class InvalidTokenGetUser(ApiError):
    code=401
    description="El token no es válido o está vencido"

# 403	El token no está en el encabezado de la solicitud.
class NoTokenGetUser(ApiError):
    code=403
    description="El token no está en el encabezado de la solicitud."