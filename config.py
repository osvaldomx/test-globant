"""
Test Globant
"""

class Config():
    ORIGINS = ['*']
    SECRET_KEY = "123456"

class DevelopConfig(Config):
    DEBUG = True
    PORT = 5000
    ENV = 'dev'
    HOST = '0.0.0.0'
