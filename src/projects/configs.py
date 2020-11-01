import os

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://agutierrez:optativo123@35.224.193.212:5432/agutierrez'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET = '123456'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default='localhost')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET = os.getenv('SECRET_JWT', default='123456')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}