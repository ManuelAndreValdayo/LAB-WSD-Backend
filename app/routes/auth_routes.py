from flask import Blueprint, request
from app.services.auth_service import login_user, register_user
from flask_cors import CORS

auth_routes = Blueprint("auth", __name__)

CORS(auth_routes, origins=["http://localhost:4200"], supports_credentials=True)

@auth_routes.route("/login", methods=["POST"])
def login():
    return login_user(request.json)

@auth_routes.route("/register", methods=["POST"])
def register():
    print(request.json)
    return register_user(request.json)