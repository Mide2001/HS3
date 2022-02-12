from HS3 import db

class Survey(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=True)
    site = db.Column(db.String(length=30), nullable=True)
    date = db.Column(db.String(length=30), nullable=True)
    road = db.Column(db.String(length=100), nullable=True)
    town = db.Column(db.String(length=30), nullable=True)
    county = db.Column(db.String(length=30), nullable=True)
    phone = db.Column(db.Integer(), nullable=True)
    email = db.Column(db.String(length=30), nullable=True)
    pipe_use = db.Column(db.String(length=30), nullable=True)
    year_laid = db.Column(db.String(length=30), nullable=True)
    pipe_length = db.Column(db.String(), nullable=True)
    pipe_shape = db.Column(db.String(length=30), nullable=True)
    pipe_size = db.Column(db.String(), nullable=True)
    pipe_material = db.Column(db.String(length=30), nullable=True)

#from HS3 import db
#db.create_all()


