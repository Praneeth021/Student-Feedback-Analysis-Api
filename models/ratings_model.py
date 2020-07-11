from db import db
from sqlalchemy_serializer import SerializerMixin


class RatingModel(db.Model, SerializerMixin):
    __tablename__ = 'ratings'

    teacher_id = db.Column(db.String(30), db.ForeignKey(
        'teachers.tid'), primary_key=True)
    rating = db.Column(db.String(10))

    def __init__(self, teacher_id, rating=0):
        self.teacher_id = teacher_id
        self.rating = rating

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(teacher_id=id).first()
