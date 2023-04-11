import os

class Config(object):
    SECRET_KEY=os.environ.get("SECRET_KEY") or "esta-es-una-clave-secreta"
    SQLALCHEMY_DATABASE_URI="mysql://root:990122754Luz@localhost/mydb2"
    SQLALCHEMY_TRACK_MODIFICATIONS=False