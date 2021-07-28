import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-cryptographic-key'
    LOC_VAR_01 = os.environ.get('LOC_VAR_01') or 'Failed'
    APP_VERSION = os.environ.get('APP_VERSION') or 'Unknown'

