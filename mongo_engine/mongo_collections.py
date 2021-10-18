from flask_mongoengine import MongoEngine
from flask_security import UserMixin, RoleMixin

def create_mongo_engine():
    db = MongoEngine()

    class Role(db.Document, RoleMixin):
        name = db.StringField(max_length=80, unique=True)
        description = db.StringField(max_length=255)

    class User(db.Document, UserMixin):
        email = db.StringField(max_length=255, unique=True)
        password = db.StringField()
        active = db.BooleanField(default=True)
        fs_uniquifier = db.StringField(max_length=64, unique=True)
        roles = db.ListField(db.ReferenceField(Role), default=[])
        name = db.StringField(max_length=60)
        username = db.StringField(max_length=20, unique=True)

    return db, User, Role