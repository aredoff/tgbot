from peewee import *
from playhouse.shortcuts import ReconnectMixin
from tgbot.config import config
from dotenv import load_dotenv
import os

load_dotenv()

class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase):
    pass

db = ReconnectMySQLDatabase(config.database.database,
                            host=config.database.host,
                            port=config.database.port,
                            user=config.database.user,
                            passwd=config.database.password,
                            charset='utf8')

# db = SqliteDatabase('db.sqlite', pragmas={
#     'journal_mode': 'wal',
#     'cache_size': -1024 * 64})

class BaseModel(Model):
    class Meta:
        database = db