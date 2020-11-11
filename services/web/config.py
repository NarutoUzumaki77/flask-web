import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(64)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/app/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/app/media"

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    """
    Production Configuration. it is essentially an extended configuration
    of the :class:`config.Config`
    """
    pass


class TestingConfig(Config):
    """
    Test Configuration. it is essentially an extended configuration
    of the :class:`config.Config`
    """
    TESTING = True
    DB_NAME = "hotel_db_test"
    DB_USERNAME = "postgres"
    DB_PASSWORD = "password!"
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@db:5432/{}".\
        format(DB_USERNAME, DB_PASSWORD, DB_NAME)

    SESSION_COOKIE_SECURE = False
