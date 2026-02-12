from datetime import datetime
from src import db

class Subscription(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    valid_until = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Subscription('{self.id}', 
                '{self.user}', 
                '{self.course}', 
                '{self.valid_until}', 
                '{self.created_at}')"