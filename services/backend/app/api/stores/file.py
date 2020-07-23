""" all classes and funcs related to external files will be here"""
import json
from operator import itemgetter


class File:
    """Class representation of a file"""

    def __init__(self):
        self.data = []

    def import_json(self, json_path: str) -> list:
        """import json file as property data"""

        try:
            with open(json_path) as json_file:
                raw_data = json.load(json_file)

        except FileNotFoundError:
            raise FileNotFoundError("Cannot load json data")

        self.data = sorted(raw_data, key=itemgetter("name"))
        return raw_data
