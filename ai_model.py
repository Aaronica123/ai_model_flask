from extensions import db, migrate

class AI(db.Model):
    __tablename__='ai'
    reg=db.Column(db.Integer, primary_key=True)
    marks=db.Column(db.Integer)
    def __repr__(self):
        return f"the reg is made {self.reg} and marks is {self.marks}"
    
class AI_DATA(db.Model):
    __tablename__="student_records"
    id=db.Column(db.Integer, primary_key=True)
    admission_number=db.Column(db.Integer)
    subject_id=db.Column(db.Integer)
    marks_obtained=db.Column(db.Integer)
    exam_type=db.Column(db.String)
    academic_year=db.Column(db.String)
    
    
    
    def response(self):
        return f" the reg {self.admission_number}"
    
# class Md(db.Model):
#     __tablename__='student_records'
#     id=db.Column(db.Integer,primary_key=True)
#     subject_id=db.Column(db.Integer)
#     admission_number=db.Column(db.String)
#     marks_obtained=db.Column(db.Integer)
    
#     def response(self):
#         return f"reg {self.admission_number}has been registered"
        

    
