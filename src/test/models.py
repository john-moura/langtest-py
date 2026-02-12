from datetime import datetime
from src import db

class Test(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    short_description = db.Column(db.String)
    description = db.Column(db.String)
    weight = db.Column(db.numeric)
    duration = db.Column(db.Integer)
    cover_image_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    subject = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=True)
    course = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True)

    def __repr__(self):
        return f"Test('{self.id}', 
                '{self.name}', 
                '{self.short_description}', 
                '{self.description}', 
                '{self.created_at}', 
                '{self.weight}', 
                '{self.duration}', 
                '{self.cover_image_url}', 
                '{self.subject}', 
                '{self.course}')"

class Test_Part(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    part_type = db.Column(db.Integer, db.ForeignKey('part_type.id'), nullable=True)
    test = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Test_Part('{self.id}', '{self.title}', '{self.part_type}', '{self.test}', '{self.created_at}')"