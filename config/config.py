import os

class Config(object):
    DEBUG = True

    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://macaw-cluster.2xqic.mongodb.net/macaw_db',
        'connect': False,
        'username': 'admin',
        'password': 'zrmcTWzoak8witRH'
    }

    SECRET_KEY = os.environ.get("SECRET_KEY", 'XgxQh1Jbcx1MaaG-KEXaw8EyqpvUbWijb6rYTEwh4KA')
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT", '165869467775770647268415457827141187051')