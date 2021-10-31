import json
from flask import Blueprint, request, Response
from flask_security import current_user
import functions.users_functions as uf 

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        print(current_user.get_id())
        if current_user.is_authenticated:
            return 'veja o log', 200
        else:
            return 'não autenticado', 401
    elif request.method == 'POST':
        response = Response(response='OK' ,status=200)
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