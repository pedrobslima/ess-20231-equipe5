from server import server_ as db
from uuid import uuid4

db.connect()

db.settle()

db.disconnect()