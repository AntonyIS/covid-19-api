import os
from os import environ
from secret import DEV_SQLALCHEMY_DATABASE_URI,PROD_SQLALCHEMY_DATABASE_URI

class Config(object):
    ENV = 'prod'
    if ENV == 'dev':
        debug = True
        SQLALCHEMY_DATABASE_URI = DEV_SQLALCHEMY_DATABASE_URI
    else:
        debug = 'False'
        SQLALCHEMY_DATABASE_URI = PROD_SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
