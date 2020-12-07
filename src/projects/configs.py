import os

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://iakfhrksnxewry:952315906aef7dfeeb65e4cb046e80fde073ba313f7ed3f1f6b115bafc8c8a06@ec2-3-208-224-152.compute-1.amazonaws.com:5432/d9n15804vblt47'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET = '123456'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default='localhost')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET = os.getenv('SECRET_JWT', default='123456')


config = {
    'development': DevelopmentConfig,
    'production': DevelopmentConfig
}