from flask import Flask
from flask_security import Security, MongoEngineUserDatastore
from mongo_engine import mongo_collections
from flask_limiter import RateLimitExceeded
from werkzeug.exceptions import Forbidden, Unauthorized, MethodNotAllowed
import flask_wtf
from flask_wtf.csrf import CSRFError
from blueprints.users_blueprint import users_blueprint as ub

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')
    flask_wtf.CSRFProtect(app)
    app.register_blueprint(ub)

    mongo_engine, User, Role = mongo_collections.create_mongo_engine()

    mongo_engine.init_app(app)
    app.user_datastore = MongoEngineUserDatastore(
        mongo_engine, User, Role
    )
    app.security = Security(app, app.user_datastore)

    @app.errorhandler(Unauthorized)
    def unauthorized(e):
        return 'Authorization required. Please, sign in.', 401

    @app.errorhandler(RateLimitExceeded)
    def rate_limit_exceeded(e):
        return 'Request limit exceeded. Try again in a few moments.', 429

    @app.errorhandler(Forbidden)
    def forbidden(e):
        return 'User does not have permission to execute this operation.', 403

    @app.errorhandler(CSRFError)
    def csrf_error(e):
        return 'No token provided.', 401

    @app.errorhandler(MethodNotAllowed)
    def method_not_allowed(e):
        return 'Method not allowed.', 405

    # when developing, disable this error handler to get more info about any eventual error
    @app.errorhandler(Exception)
    def error_handler(e):
        return "Internal server error.", 500

    @app.route('/', methods=['GET'])
    def index():
        return "Welcome to Macaw!", 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port='5050'
    )
