import os

class Config(object):
    DEBUG = True

    # MONGO_URI = "mongodb+srv://admin:zrmcTWzoak8witRH@macaw-cluster.2xqic.mongodb.net/macaw_db?retryWrites=true&w=majority"
    # MONGO_URI = "mongodb%2Bsrv%3A%2F%2Fadmin%3AzrmcTWzoak8witRH%40macaw-cluster.2xqic.mongodb.net%2Fmacaw_db%3FretryWrites%3Dtrue%26w%3Dmajority"

    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://macaw-cluster.2xqic.mongodb.net/macaw_db',
        'db': 'macaw_db',
        'connect': False,
        'username': 'admin',
        'password': 'zrmcTWzoak8witRH'
    }

    SECRET_KEY = os.environ.get("SECRET_KEY", 'XgxQh1Jbcx1MaaG-KEXaw8EyqpvUbWijb6rYTEwh4KA')
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT", '165869467775770647268415457827141187051')