import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Common configuration settings

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://queries_user:queries_pass@localhost:5435/queries_db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://postgres:password@localhost/db_training_management_test')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL', 'sqlite:///training_queries_production.db')