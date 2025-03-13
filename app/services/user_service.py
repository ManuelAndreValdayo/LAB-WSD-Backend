from app.models.user import User
from app.extensions import db
from app.persistence.userDB import UserDB
from flask_jwt_extended import create_access_token
from http import HTTPStatus
import bcrypt

def register_user(data):
    if(UserDB.fncCheckUser(data["username"]) or UserDB.fncCheckEmail(data["email"])):
        return {"message": "The User already exists"}, HTTPStatus.CONFLICT
    else:
        user = User()
        user.name = data["name"]
        user.surnames = data["surnames"]
        user.username = data["username"]
        user.email = data["email"]
        user.password = bcrypt.hashpw(data["password"].encoded['utf-8'], bcrypt.gensalt())

        return UserDB.fncCreateUser(user)
    # if User.query.filter_by(username=data["username"]).first():
    #     return {"message": "El usuario ya existe"}, 400

    # user = User(username=data["username"], email=data["email"])
    # user.set_password(data["password"])
    # db.session.add(user)
    # db.session.commit()

    # return {"message": "Usuario registrado exitosamente"}, 201

def login_user(data):
    # user = User.query.filter_by(username=data["username"]).first()
    # if user and user.check_password(data["password"]):
    #     token = create_access_token(identity=user.id)
    #     return {"access_token": token}, 200
    return {"message": "Credenciales inválidas"}, 401
