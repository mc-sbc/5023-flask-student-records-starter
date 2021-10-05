from app import db

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
     # This attribute should have backref called grade, so that you can access the Grade from Student objects. 
    students = db.relationship('Student', backref='grade')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)
    english_mark = db.Column(db.Integer)
    science_mark = db.Column(db.Integer)
    mathematics_mark = db.Column(db.Integer)
    does_homework = db.Column(db.Boolean)
    stays_on_task = db.Column(db.Boolean)

class House(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    colour = db.Column(db.Text)
    # This attribute should have backref called ‘house’, so that you can access the House from Student objects. 
    students = db.relationship('Student', backref='house')
