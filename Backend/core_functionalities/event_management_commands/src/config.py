import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Common configuration settings

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('COMMANDS_DATABASE_URL', 'postgresql://commands_user:commands_pass@localhost:5433/commands_db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://postgres:password@localhost/db_event_management_test')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///events_commands_production.db')