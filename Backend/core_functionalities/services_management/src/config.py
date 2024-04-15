import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Common configuration settings

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://services_user:services_pass@localhost:5437/services_db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://services_user_test:services_pass_test@localhost:5437/services_db_test')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL', 'postgresql://services_user_prod:services_pass_prod@localhost:5437/services_db_prod')