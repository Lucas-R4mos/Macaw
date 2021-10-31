from flask_mongoengine import MongoEngine
from flask_security import UserMixin, RoleMixin

def create_mongo_engine():
    db = MongoEngine()

    class Role(db.Document, RoleMixin):
        name = db.StringField(max_length=10, unique=True)
        description = db.StringField(max_length=60)

    class User(db.Document, UserMixin):
        name = db.StringField(max_length=60)
        username = db.StringField(max_length=20, min_length=6, unique=True)
        email = db.StringField(max_length=255, unique=True)
        password = db.StringField()
        bio = db.StringField(max_length=200, default='')
        active = db.BooleanField(default=True)
        fs_uniquifier = db.StringField(max_length=64, unique=True)
        roles = db.ListField(db.ReferenceField(Role), default=['common'])

    return db, User, Role