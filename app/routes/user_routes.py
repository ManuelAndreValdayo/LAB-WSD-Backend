from flask import Blueprint, request
from app.services.auth_service import register_user

user_routes = Blueprint('user', __name__)  # Definir el Blueprint correctamente


