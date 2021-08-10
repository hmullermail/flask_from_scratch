import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    START_FLAG = os.environ.get('START_FLAG') or 'False'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-cryptographic-key'
    LOC_VAR_01 = os.environ.get('LOC_VAR_01') or 'Failed'
    APP_VERSION = os.environ.get('APP_VERSION') or 'Unknown'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '/data/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DELTA = int(os.environ.get('DELTA')) or 60