from . import db

class Comment(db.mode1):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    company = db.Column(db.String(100000))
    