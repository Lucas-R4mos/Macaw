from json.decoder import JSONDecodeError
import functions.utility_functions as utils
import forms.users_forms as uf
from flask import current_app
from werkzeug.datastructures import ImmutableMultiDict
from flask_security import hash_password
from mongoengine.errors import ValidationError
from json.decoder import JSONDecodeError


def register_user(request, response):
    try:
        data = utils.check_json(request)
        if (
            not data or
            not ('email' in data and type(data['email']) == str) or
            not ('password' in data and type(data['password']) == str) or
            not ('name' in data and type(data['name']) == str) or
            not ('username' in data and type(data['username']) == str)
        ):
            return 'Invalid JSON.', 400
    except JSONDecodeError:
        return 'Invalid JSON.', 400

    try:
        form = uf.RegistrationUserForm(ImmutableMultiDict(data))

        if form.validate():
            user_datastore = current_app.user_datastore
            if user_datastore.find_user(username=form.username.data):
                response.data, response.status_code = 'Username already in use.', 409
            elif user_datastore.find_user(email=form.email.data):
                response.data, response.status_code = 'Email address already in use.', 409
            else:
                user_datastore.create_user(
                    name=form.name.data,
                    username=form.username.data,
                    password=hash_password(form.password.data),
                    email=form.email.data,
                    roles=['common']
                )
                response.data, response.status_code = 'User created.', 201

        else:
            for _, errors in form.errors.items():
                return errors[0], 400

    except ValidationError as e:
        return e.message, 400

    return response
