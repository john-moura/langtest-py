from datetime import datetime
from src import db

class Test(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name_en = db.Column(db.String)
    name_de = db.Column(db.String)
    short_description_en = db.Column(db.String)
    short_description_de = db.Column(db.String)
    description_en = db.Column(db.String)
    description_de = db.Column(db.String)
    weight = db.Column(db.numeric)
    duration = db.Column(db.Integer)
    cover_image_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    subject = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=True)
    course = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True)

    def __repr__(self):
        return f"Test('{self.id}', 
                '{self.name_en}', 
                '{self.name_de}', 
                '{self.short_description_en}', 
                '{self.short_description_de}', 
                '{self.description_en}', 
                '{self.description_de}', 
                '{self.created_at}', 
                '{self.weight}', 
                '{self.duration}', 
                '{self.cover_image_url}', 
                '{self.subject}', 
                '{self.course}')"


class Test_Part_Type(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    parts = db.relationship('Test_Part', backref = 'part_type', lazy = True)

    def __repr__(self):
        return f"Test_Part_Type('{self.id}', 
                '{self.name}', 
                '{self.created_at}')"


class Test_Part(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title_en = db.Column(db.String)
    title_de = db.Column(db.String)
    part_type = db.Column(db.Integer, db.ForeignKey('part_type.id'), nullable=True)
    test = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    questions = db.relationship('Question', backref = 'test_part', lazy = True)

    def __repr__(self):
        return f"Test_Part('{self.id}', 
                '{self.title_en}', 
                '{self.title_de}', 
                '{self.part_type}', 
                '{self.test}', 
                '{self.created_at}', 
                '{self.questions}')"


class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    idx = db.Column(db.Integer)
    header_en = db.Column(db.String)
    header_de = db.Column(db.String)
    subheader_en = db.Column(db.String)
    subheader_de = db.Column(db.String)
    text_en = db.Column(db.String)
    text_de = db.Column(db.String)
    image_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    test_part = db.Column(db.Integer, db.ForeignKey('test_part.id'), nullable=True)
    answers = db.relationship('Answer', backref = 'question', lazy = True)
    
    def __repr__(self):
        return f"Question('{self.id}', 
                '{self.idx}', 
                '{self.header_en}', 
                '{self.header_de}', 
                '{self.subheader_en}', 
                '{self.subheader_de}', 
                '{self.text_en}', 
                '{self.text_de}', 
                '{self.image_url}', 
                '{self.created_at}', 
                '{self.test_part}')"


class Answer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    idx = db.Column(db.String)
    text_en = db.Column(db.String)
    text_de = db.Column(db.String)
    is_correct = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    question = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)

    def __repr__(self):
        return f"Answer('{self.id}', 
                '{self.idx}', 
                '{self.text_en}', 
                '{self.text_de}', 
                '{self.is_correct}', 
                '{self.created_at}', 
                '{self.question}')"