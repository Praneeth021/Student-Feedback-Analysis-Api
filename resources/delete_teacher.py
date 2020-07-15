from flask_restful import Resource, reqparse, request
from models.teachers_model import TeacherModel
from models.user_model import UserModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class DeleteTeacher(Resource):
    
    @jwt_required
    def put(self):

        current_user = get_jwt_identity()
        user = UserModel.query.filter_by(id=current_user).first()
        user = user.to_dict()

        tid=request.json.get('tid')
        teacher=TeacherModel.find_by_tid(tid=tid)

        if not (user['admin']):
            return make_response(jsonify({"msg": "You are not authorised to access the page"}), 403)

        if  TeacherModel.find_by_tid(tid=tid):
            db.session.delete(teacher)
            db.session.commit()
            return {"msg":"deleted"}

        return {"msg":"Not Exists"}