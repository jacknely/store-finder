from flask_restx import Api

from app.api.ping import ping_namespace
from app.api.stores.views import stores_namespace

api = Api(version="1.0", title="Stores API", doc="/doc")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(stores_namespace, path="/api")
