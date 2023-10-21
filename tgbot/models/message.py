from peewee import *
import datetime
from .base import BaseModel
from .user import User

class Message(BaseModel):
    user = ForeignKeyField(User, backref='messages', on_delete='CASCADE')
    text = TextField()
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'messages'