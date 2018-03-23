import os


class Config:
    PORT = os.getenv('PORT')
    HOST = os.getenv('HOST')


class DevelopmentConfig(Config):
    PORT = os.getenv('PORT', 5000)
    HOST = os.getenv('HOST', '0.0.0.0')
    DEBUG = True


# TODO test config
