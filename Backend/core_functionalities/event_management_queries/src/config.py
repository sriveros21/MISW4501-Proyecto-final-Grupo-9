class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Common config settings

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///training_development.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///training_production.db'
    # Production config settings