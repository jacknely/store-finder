import os

from flask import Flask
from flask_cors import CORS

cors = CORS()


def create_app():

    app = Flask(__name__)
    CORS(app)

    app.url_map.strict_slashes = False

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # register api
    from app.api import api

    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
