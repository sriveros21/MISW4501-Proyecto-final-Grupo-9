from ..models.services import Service
from ..extensions import db

def add_service(data):
    new_service = Service(**data)
    db.session.add(new_service)
    db.session.commit()
    return new_service.id