from db import db
from models.teachers_model import TeacherModel
from sqlalchemy_serializer import SerializerMixin


class FeedbackModel(db.Model, SerializerMixin):

    __tablename__ = 'feedbacks'

    s_id = db.Column(db.String(30), db.ForeignKey(
        'users.rollno'), primary_key=True, nullable=False)
    t_id = db.Column(db.String(30), db.ForeignKey(
        'teachers.tid'), primary_key=True, nullable=False)
    feedback = db.Column(db.String(300))

    def __init__(self, s_id, t_id, feedback):
        self.s_id = s_id
        self.t_id = t_id
        self.feedback = feedback

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_s_id(cls, s_id, t_id):
        return cls.query.filter_by(s_id=s_id, t_id=t_id).first()

    @classmethod
    def find_by_t_id(cls, t_id):
        return cls.query.filter_by(t_id=t_id).all()


    @classmethod
    def find_by_rollno(cls, s_id):
        return cls.query.filter_by(s_id=s_id).all()
