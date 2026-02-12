from datetime import datetime
from src import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    google_id = db.Column(db.String, unique=True)
    avatar_url = db.Column(db.String)

    def __repr__(self):
        return f"User('{self.id}', '{self.first_name}', '{self.last_name}', '{self.email}', '{self.google_id}', '{self.avatar_url}')"