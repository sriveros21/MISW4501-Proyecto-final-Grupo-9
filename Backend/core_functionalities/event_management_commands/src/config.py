import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Common configuration settings

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://commands_user:commands_pass@localhost:5433/commands_db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://commands_user_test:commands_pass_test@localhost:5433/commands_db_test')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL', 'postgresql://commands_user_prod:commands_pass_prod@localhost:5433/commands_db_prod')