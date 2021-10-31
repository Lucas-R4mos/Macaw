import os

class Config(object):
    DEBUG = True

    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGO_DB_HOST', 'mongodb+srv://macaw-cluster.2xqic.mongodb.net/macaw_db'),
        'connect': False,
        'username': os.environ.get('MONGO_DB_USERNAME'),
        'password': os.environ.get('MONGO_DB_PASSWORD'),
        'tls': True
    }

    SECRET_KEY = os.environ.get("SECRET_KEY", 'XgxQh1Jbcx1MaaG-KEXaw8EyqpvUbWijb6rYTEwh4KA')
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT", '165869467775770647268415457827141187051')
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = True
    WTF_CSRF_CHECK_DEFAULT = False