from db import db
from sqlalchemy_serializer import SerializerMixin

class TeacherModel(db.Model, SerializerMixin):
    __tablename__='teachers'
    tid=db.Column(db.String(30),primary_key=True)
    username=db.Column(db.String(80))
    deptartment=db.Column(db.String(80))
    gender=db.Column(db.String(30))
    image=db.Column(db.String(80))
    designation=db.Column(db.String(80))
    email=db.Column(db.String(80))
    date_joined=db.Column(db.String(15))

    

    def __init__(self,tid,username,deptartment,gender,image,designation,email,date_joined):
        self.tid=tid
        self.username=username
        self.deptartment=deptartment      
        self.gender=gender
        self.image=image
        self.designation=designation
        self.email=email
        self.date_joined=date_joined

         

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def find_by_tid(cls,tid):
        return cls.query.filter_by(tid=tid).first()

    