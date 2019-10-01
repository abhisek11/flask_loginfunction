from . import db 

class User(db.Model):
    id = db.column(db.Integer,primary_key=True) #primary keys are required by SQLAlchemy
    email=db.column(db.String(100), unique=True)
    password=db.column(db.string(100))
    name=db.column(db.string(1000))