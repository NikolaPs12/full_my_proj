import os

class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/uploads/'
    SERVER_PATH = os.path.join(ROOT, UPLOAD_PATH.lstrip('/'))

    # Используем переменную окружения для подключения к БД
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://nikola:password@localhost:5432/mydb"
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456789'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Изменено на False для производительности