import os


class Config:
    PG_USER = '<PG_USER>'
    PG_PASSWORD = '<PG_PASSWORD>'
    PG_HOST = 'localhost'
    PG_PORT = 5432
    DB_NAME = '<DB_NAME>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{DB_NAME}"
    SECRET_KEY = 'secret_key'


class TestConfig:
    PG_USER = '<PG_USER>'
    PG_PASSWORD = '<PG_PASSWORD>'
    PG_HOST = 'localhost'
    PG_PORT = 5432
    DB_NAME = '<DB_NAME>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{DB_NAME}"
    SECRET_KEY = 'test_key'


class ProductConfig:
    SECRET_KEY = 'product_key'


def run_config(env='DEV'):
    # env = os.environ.get('ENV')
    if env == 'TEST':
        return TestConfig
    elif env == 'PROD':
        return ProductConfig
    return Config
