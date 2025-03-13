from app.extensions import db
from app.models.user import User
from flask import jsonify

class UserDB():

    def fncObtainUser(id: int) -> any:
        try:
            return db.session.query(User).filter_by(id=id).first()
        except Exception as e:
            return jsonify({"message": "Error obtainig the user","details": str(e)}), 400
    
    def fncCheckUser(username: str) -> any:
        try:
            return db.session.query(User).filter_by(username=username).first() is not None
        except Exception as e:
            return jsonify({"message": "Error obtainig the user","details": str(e)}), 400

    
    def fncCheckEmail(email: str) -> any:
        try:
            return db.session.query(User).filter_by(email=email).first() is not None
        except Exception as e:
            return jsonify({"message": "Error obtainig the user","details": str(e)}), 400
        
    def fncCreateUser(user: User):
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "User created successfully"}), 201
        except Exception as e:
            return jsonify({"message": "Error creating the user","details": str(e)}), 400
