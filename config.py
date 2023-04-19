import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """ Environment Variables for the Flask App, SQLAlchemy"""

    # FLASK
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")

    # SECRET KEY FOR FLASK-WTF
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
