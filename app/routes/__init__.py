from app.routes.auth_routes import auth_routes

def register_routes(app):
    app.register_blueprint(auth_routes, url_prefix='/auth')
