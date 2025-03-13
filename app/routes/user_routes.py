from flask import Blueprint, request
from app.services.user_service import login_user, register_user
from flask_cors import CORS

user_routes = Blueprint("user", __name__)

CORS(user_routes, origins=["http://localhost:4200"], supports_credentials=True)

@user_routes.route("/login", methods=["POST"])
def login():
    return login_user(request.json)

@user_routes.route("/register", methods=["POST"])
def register():
    return register_user(request.json)