from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)

    @app.route("/")
    def index():
        return render_template("main.html")

    return app


def register_blueprints(app: Flask) -> None:
    from . import icons, ads

    app.register_blueprint(icons.bp)
    app.register_blueprint(ads.bp)  # deprecated
    app.register_blueprint(icons.bp_silicon)
