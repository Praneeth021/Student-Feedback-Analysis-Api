from db import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import load_only


class ClassModel(db.Model, SerializerMixin):
    __tablename__='classes'

    id=db.Column(db.Integer, primary_key=True)
    department=db.Column(db.String(80))
    year=db.Column(db.String(10))
    section=db.Column(db.String(10))
    subject=db.Column(db.String(30))
    teacher_id=db.Column(db.String(30))

    def __init__(self,department,year,section, subject,teacher_id):
        self.department=department
        self.year=year
        self.section=section    
        self.subject=subject  
        self.teacher_id=teacher_id
        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_department(cls, department, year, section, subject):
        return cls.query.filter_by(department=department, year=year, section=section, subject=subject).first()

    @classmethod
    def find_by_class(cls, department, year, section):
        classes=cls.query.filter_by(department=department, year=year, section=section).all()
        return classes