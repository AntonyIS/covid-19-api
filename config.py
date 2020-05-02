import os
from os import environ
import redis
# Define root folder location
basedir = os.path.abspath(os.path.dirname(__file__))

red = redis
class Config(object):
    """
    Define core settings for the app
    """
    # Defines the location of the api db



    ENV = 'dev'

    if ENV == 'prod':
        debug = True
        # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "api.db")
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:GeoDev@localhost/covidapi"
        REDIS_HOST = "0.0.0.0"
        REDIS_PORT = 6379
        BROKER_URL = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(host=REDIS_HOST, port=str(REDIS_PORT)))
        CELERY_RESULT_BACKEND = BROKER_URL
    else:
        debug = 'False'
        SQLALCHEMY_DATABASE_URI = "postgres://mozhnghyvetbvr:86b2c83ff9c3057e870100932398b53b40bb7d7e212e34d245d82f9008aaeb53@ec2-52-87-135-240.compute-1.amazonaws.com:5432/d438kerhs0i6rc"
        # r = redis.from_url(os.environ.get("REDIS_URL"))
        REDIS_URL = "redis://h:p336748e537327e44c4b0bbd3c3be384224bd0450707f61d544eb063f89226498@ec2-34-237-180-36.compute-1.amazonaws.com:21249"


    SQLALCHEMY_TRACK_MODIFICATIONS = False
