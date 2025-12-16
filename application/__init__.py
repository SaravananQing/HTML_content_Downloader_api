from flask import Flask
from requests import get,post
from .routes import main


def Create_app(config_doc=None):
    app=Flask(__name__)
    if config_doc:
        app.config.from_object(config_doc)
    app.register_blueprint(main)
    return app