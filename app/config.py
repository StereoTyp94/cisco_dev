import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'secret key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_FILE_SIZE = 1024 * 1024 + 1
    UPLOAD_FOLDER = 'C:\cisco_dev\\answers'
    ALLOWED_EXTENSIONS = ['txt']#, 'pdf', 'png', 'jpg', 'jpeg', 'gif']