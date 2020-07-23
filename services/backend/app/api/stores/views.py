from flask_restx import Namespace, Resource, reqparse

from app.api.stores.models import stores

stores_namespace = Namespace("stores")

parser = reqparse.RequestParser()
parser.add_argument("radius", type=int)
parser.add_argument("postcode", type=str)


class StoreSearch(Resource):
    @stores_namespace.response(204, "No content")
    @stores_namespace.response(200, "Successful response")
    @stores_namespace.response(404, "Invalid query parameters")
    @stores_namespace.expect(parser)
    def get(self) -> tuple:
        """Endpoint to query stores by postcode and radius"""
        args = parser.parse_args()
        radius = args["radius"]
        postcode = args["postcode"]

        if not (radius and postcode):
            stores_namespace.abort(404, "Invalid query parameters")

        try:
            results = stores.search_stores(postcode, radius)
            results_north = sorted(results, key=lambda k: k["latitude"], reverse=True)

        except ValueError:
            stores_namespace.abort(404, "Invalid query parameters")

        if len(results) < 1:
            response_object = {"message": "Sorry, no stores in this area"}
            return response_object, 204

        return results_north, 200


stores_namespace.add_resource(StoreSearch, "")
