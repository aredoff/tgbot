from peewee import *
import datetime
from .base import BaseModel
from .user import User

class Secret(BaseModel):
    user = ForeignKeyField(User, backref='code', unique=True, null=True, on_delete='SET NULL')
    code = IntegerField(unique=True)
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'secrets'