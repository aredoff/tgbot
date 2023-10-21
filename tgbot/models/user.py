from peewee import *
import datetime
from .base import BaseModel

class User(BaseModel):
    telegram_id = IntegerField(unique=True)
    username = CharField(max_length=128, null=True)
    first_name = CharField(max_length=128, null=True)
    language_code = CharField(max_length=2, null=True)
    accepted = BooleanField(default=False)
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'users'









