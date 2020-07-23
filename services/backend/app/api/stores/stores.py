""" this module contains all business logic related to stores """
import math

from app.api.stores.postcodeio import search


class Stores:
    """ class representation of a stores """

    def __init__(self):
        self.data = []

    def add_data(self, data: list) -> list:
        """ adds raw store data to store object """

        if len(data) > 1:
            self.data = data
        else:
            raise ValueError("Cannot load json data")

    def add_location(self) -> list:
        """ adds location to all stores saved in data property """

        postcodes = [store["postcode"] for store in self.data]

        results = search(postcodes)

        for index, store in enumerate(self.data):
            try:
                self.data[index]["longitude"] = results[index]["longitude"]
                self.data[index]["latitude"] = results[index]["latitude"]
            except TypeError:
                self.data[index]["longitude"] = "NAN"
                self.data[index]["latitude"] = "NAN"

        self.data = [data for data in self.data if "NAN" not in data.values()]

        return self.data

    def search_stores(self, postcode: str, radius: int) -> list:
        """ takes a postcode and radius and returns stores in area """

        postcode_info = search([postcode])[0]
        location_a = (postcode_info["longitude"], postcode_info["latitude"])

        results = []
        for i, store in enumerate(self.data):

            try:
                location_b = (self.data[i]["longitude"], self.data[i]["latitude"])
                distance = self.get_distance(location_a, location_b)
            except TypeError:
                print(f"{self.data[i]['postcode']} Error. Postcode not added")

            if distance <= radius:
                new_store = self.data[i]
                new_store["distance"] = round(distance, 2)
                results.append(new_store)

        return results

    @staticmethod
    def get_distance(dist_a: tuple, dist_b: tuple) -> float:
        """ takes two sets of long,lat
        co-ordinates and returns distance between
        constants taken from:
        www.movable-type.co.uk/scripts/latlong.html
        """
        r = 6371300
        long_1 = math.radians(dist_a[0])
        lat_1 = math.radians(dist_a[1])
        long_2 = math.radians(dist_b[0])
        lat_2 = math.radians(dist_b[1])

        delta_long = long_2 - long_1
        delta_lat = lat_2 - lat_1

        a = math.sin(delta_lat / 2) * math.sin(delta_lat / 2) + math.cos(
            lat_1
        ) * math.cos(lat_2) * math.sin(delta_long / 2) * math.sin(delta_long / 2)

        b = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        dist = r * b / 1000

        return dist
