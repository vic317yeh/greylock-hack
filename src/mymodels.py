from peewee import *

database = MySQLDatabase('greylock', **{'password': 'greylock', 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Flags(BaseModel):
    fid = PrimaryKeyField()
    location_lat = DecimalField()
    location_log = DecimalField()
    name = TextField()
    photo_url = TextField(null=True)
    rating = IntegerField()

    class Meta:
        db_table = 'Flags'

class Friends(BaseModel):
    email = CharField()
    friend_email = CharField()

    class Meta:
        db_table = 'Friends'
        indexes = (
            (('email', 'friend_email'), True),
        )
        primary_key = CompositeKey('email', 'friend_email')

class Userflags(BaseModel):
    email = CharField()
    fid = IntegerField()
    rating = IntegerField(null=True)
    review = TextField(null=True)
    timestamp = TextField()

    class Meta:
        db_table = 'UserFlags'
        indexes = (
            (('email', 'fid'), True),
        )
        primary_key = CompositeKey('email', 'fid')

class Users(BaseModel):
    email = CharField()
    location_lat = DecimalField()
    location_log = DecimalField()
    name = TextField(null=True)
    password = CharField()
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'Users'

