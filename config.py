import os
APPDIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(APPDIR, 'lib.db')

CSRF_ENABLED = True
DEBUG=True
SECRET_KEY = 'SuperSecretKey_S'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APPDIR, 'lib.db')
