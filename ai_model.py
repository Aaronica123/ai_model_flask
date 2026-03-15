from extensions import db, migrate

class AI(db.Model):
    __tablename__='ai'
    reg=db.Column(db.Integer, primary_key=True)
    marks=db.Column(db.Integer)
    def __repr__(self):
        return f"the reg is made {self.reg} and marks is {self.marks}"
    
class AI_DATA(db.Model):
    __tablename__="marks"
    reg=db.Column(db.Integer)
    cat_1=db.Column(db.Integer)
    cat_2=db.Column(db.Integer)
    cat_3=db.Column(db.Integer)
    exam_1=db.Column(db.Integer)
    exam_2=db.Column(db.Integer)
    id_count=db.Column(db.Integer,autoincrement=True, primary_key=True)
    
    def response(self):
        return f" the reg {self.reg} has marks {self.exam_1}, {self.exam_2}"
    
        

    
