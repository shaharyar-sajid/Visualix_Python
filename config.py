import os
import uuid
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    MAX_CONTENT_LENGTH = 1024 * 1024
    UPLOAD_EXTENSIONS = ['.csv']
    UPLOAD_PATH = 'uploads'
    SECRET_KEY = os.environ.get('SECRET_KEY') or uuid.uuid4().hex
    BOOTSTRAP_BOOTSWATCH_THEME = 'simplex'