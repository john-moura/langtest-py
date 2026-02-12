from datetime import datetime
from src import db

class Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    thumb_url = db.Column(db.String)
    subjects = db.relationship('Subject', backref = 'course', lazy = True)

    def __repr__(self):
        return f"Course('{self.id}', '{self.name}', '{self.description}', '{self.created_at}', '{self.thumb_url}')"


class Subject(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    thumb_url = db.Column(db.String)
    course = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    tests = db.relationship('Test', backref = 'subject', lazy = True)

    def __repr__(self):
        return f"Subject('{self.id}', '{self.name}', '{self.description}', '{self.created_at}', '{self.thumb_url}')"