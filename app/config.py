import os

class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/uploads/'
    SERVER_PATH = os.path.join(ROOT, UPLOAD_PATH.lstrip('/'))

    # Используем переменную окружения для подключения к БД с явным указанием кодировки
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://nikola:password@localhost:5432/mydb?client_encoding=utf8"
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456789'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Изменено на False для производительности
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
        'connect_args': {
            'client_encoding': 'utf8'
        }
    }