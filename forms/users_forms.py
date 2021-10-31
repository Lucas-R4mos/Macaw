import re
from mongoengine.errors import ValidationError
from wtforms.fields.html5 import EmailField
from wtforms.validators import (
    Email,
    Length
)
from wtforms import (
    Form,
    StringField,
    PasswordField
)


# custom validators

class PasswordValidator(object):
    def __call__(self, form, field):
        if len(field.data) < 8:
            raise ValidationError('Password must have at least 8 characters.')
        elif len(field.data) > 32:
            raise ValidationError(
                'Password must not have more than 32 characters.')
        elif not re.search(r"[a-z]", field.data):
            raise ValidationError(
                'Password must have at least one lower case character.')
        elif not re.search(r"[A-Z]", field.data):
            raise ValidationError(
                'Password must have at least one capital character.')
        elif not re.search(r"[0-9]", field.data):
            raise ValidationError('Password must have at least one number.')
        elif not re.search(r"[!@#_\-.*]", field.data):
            raise ValidationError(
                'Password must have at least one special character.')
        elif re.search(r"[{}()$'\"`/\\]", field.data):
            raise ValidationError(
                'Password not must have dangerous characters.')


class RequiredField(object):
    def __call__(self, form, field):
        if not field.raw_data:
            raise ValidationError(f'Missing {field.name} field.')


# forms

class RegistrationUserForm(Form):
    email = EmailField('email', [
        Email(message='Invalid email.'),
        RequiredField()
    ])

    name = StringField('name', [
        Length(
            max=60,
            message='Name field must not have more than 60 characters.'
        ),
        RequiredField()
    ])

    username = StringField('username', [
        Length(
            max=20,
            min=6,
            message='Username field must not have more than 20 characters or less than 6 characters.'
        ),
        RequiredField()
    ])

    password = PasswordField('password', [
        PasswordValidator(),
        RequiredField()
    ])
