from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(150))
    is_admin = db.Column(db.Boolean, default=False)
            
class Trip(db.Model):                             
    id=db.Column(db.Integer, primary_key=True)
    departure = db.Column(db.String(150))
    destination=db.Column(db.String(150))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    price = db.Column(db.Integer)    
