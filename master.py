from flask import Flask
from flask_security import Security, MongoEngineUserDatastore, \
    auth_required, hash_password
from mongo_engine import mongo_collections
from flask_limiter import RateLimitExceeded
from werkzeug.exceptions import Forbidden
import flask_wtf
from flask_wtf.csrf import CSRFError

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')
    flask_wtf.CSRFProtect(app)

    mongo_engine, User, Role = mongo_collections.create_mongo_engine()

    mongo_engine.init_app(app)
    app.user_datastore = MongoEngineUserDatastore(
        mongo_engine, User, Role
    )
    app.security = Security(app, app.user_datastore)

    @app.errorhandler(CSRFError)
    def csrf_error(e):
        return 'No token provided.', 401

    @app.errorhandler(405)
    def method_not_allowed(e):
        return 'Method not allowed', 405

    @app.errorhandler(401)
    def unauthorized(e):
        return 'Unauthorized.', 401

    @app.errorhandler(Exception)
    def internal_error(e):
        if isinstance(e, RateLimitExceeded):
            status = 'Request limit exceeded. Try again in a few moments.'
            code = 429
        elif isinstance(e, Forbidden):
            status = 'User does not have permission to execute this operation.'
            code = 403
        else:
            status = 'Internal Server Error.'
            code = 500

        return status, code

    @app.route('/', methods=['GET'])
    def index():
        return "Welcome to Macaw!", 200
        

if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port='5001'
    )
