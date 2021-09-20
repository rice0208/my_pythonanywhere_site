from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask) -> None:
    from . import icons
    app.register_blueprint(icons.bp)