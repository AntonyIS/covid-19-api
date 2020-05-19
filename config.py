import os
from os import environ

class Config(object):
    ENV = 'prod'
    if ENV == 'dev':
        debug = True
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:GeoDev@localhost/covidapi"
    elif ENV == 'prod':
        debug = 'False'
        SQLALCHEMY_DATABASE_URI = "postgres://mozhnghyvetbvr:86b2c83ff9c3057e870100932398b53b40bb7d7e212e34d245d82f9008aaeb53@ec2-52-87-135-240.compute-1.amazonaws.com:5432/d438kerhs0i6rc"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
