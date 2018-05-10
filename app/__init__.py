from flask import Flask
from app.models.book import db


def creat_app():
    app = Flask(__name__)
    # readIn config
    app.config.from_object("app.secure")
    app.config.from_object("app.settings")
    register_blueprint(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
