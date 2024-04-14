from sqlalchemy import Column, String, Float, Boolean, Integer
from ..extensions import db

class Service(db.Model):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    available = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Service(name={self.name}, available={self.available})>"