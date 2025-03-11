from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt
from app.routes import user_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    #Registrar rutas
    app.register_blueprint(user_routes, url_prefix='/user')

    return app