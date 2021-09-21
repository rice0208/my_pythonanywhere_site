from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)

    @app.route("/")
    def index():
        return render_template('main.html')

    return app


def register_blueprints(app: Flask) -> None:
    from . import icons

    app.register_blueprint(icons.bp)
