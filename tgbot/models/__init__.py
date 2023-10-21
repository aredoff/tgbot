from .base import db
from .user import User
from .secret import Secret



def conect_db():
    db.connect()
    db.create_tables([User, Secret, ])

def close_db():
    db.close()