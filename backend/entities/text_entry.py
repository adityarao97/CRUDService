from pony.orm import PrimaryKey, Required
from database import db


class TextEntry(db.Entity):
    id = PrimaryKey(int, auto=True)
    content = Required(str)
