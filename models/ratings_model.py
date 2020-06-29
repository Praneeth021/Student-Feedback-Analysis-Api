from db import db


class RatingModel(db.Model):
    __tablename__='ratings'

    teacher_id=db.Column(db.String(30), db.ForeignKey('teachers.tid'), primary_key=True)
    rating=db.Column(db.String(10))

    def __init__(self, teacher_id, rating):
        self.teacher_id=teacher_id
        self.rating=rating

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
