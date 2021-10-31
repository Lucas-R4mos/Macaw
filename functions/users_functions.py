import functions.utility_functions as utils
import forms.users_forms as uf
from flask import current_app
from werkzeug.datastructures import ImmutableMultiDict
from flask_security import hash_password


def register_user(request, response):
    try:
        data = utils.check_json_return_data(request)
        if(
            (data['email'] and not isinstance(data['email'], str)) or
            (data['password'] and not isinstance(data['password'], str)) or
            (data['name'] and not isinstance(data['name'], str)) or
            (data['username'] and not isinstance(data['username'], str))
        ) or data is not None:
            pass
    except Exception as e:
        response.data, response.status_code = 'Invalid JSON.', 400
        return response

    try:
        form = uf.RegistrationUserForm(ImmutableMultiDict(data))

        if form.validate():
            user_datastore = current_app.user_datastore
            try:
                if user_datastore.find_user(username=form.username.data):
                    response.data, response.status_code = 'Username already in use.', 409
                elif user_datastore.find_user(email=form.email.data):
                    response.data, response.status_code = 'Email address already in use.', 409
                else:
                    user_datastore.create_user(
                        name=form.name.data,
                        username=form.username.data,
                        password=hash_password(form.password.data),
                        email=form.email.data
                    )
                    response.data, response.status_code = 'User created.', 201

            except Exception as e:
                raise e

        else:
            for _, errors in form.errors.items():
                response.data, response.status_code = errors[0], 400
                break

    except Exception as e:
        # this except will catch custom form validation errors
        if (e.message):
            return e.message, 400
        else:
            print(e, dir(e))
            return 'Internal Server Error.', 500

    return response
