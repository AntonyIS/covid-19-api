import os

# Define root folder location
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Define core settings for the app
    """
    # Defines the location of the api db
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "api.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False