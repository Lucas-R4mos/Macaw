from flask import Blueprint, request, Response
from flask_security import current_user
from werkzeug.exceptions import Unauthorized
import functions.users_functions as uf 

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        response = Response(response='OK', status=200)
        response = uf.get_user_data(request, response)
        return response
    elif request.method == 'POST':
        response = Response(response='OK', status=200)
        response = uf.register_user(request, response)
        return response

@users_blueprint.route('/users/<username>', methods=['GET', 'PUT', 'DELETE'])
def user():
    if request.method == 'GET':
        return 'GET username', 200
    if request.method == 'PUT':
        return 'PUT username', 200
    if request.method == 'DELETE':
        return 'DELETE username', 200