""" all funcs for communicating with postcode.io will be here"""
import requests


def search(postcodes: list) -> str:
    """PostCodeIO API wraper that returns a list of dics"""

    resp = requests.post(
        "https://api.postcodes.io/postcodes", json={"postcodes": postcodes}
    )

    if resp.status_code != 200:
        raise IOError(
            "Error connecting to 3rd party API ensure connect and valid inputs"
        )

    query = resp.json()["result"]

    if query[0]["result"] is None:
        raise ValueError("No results for given input")

    return [postcode["result"] for postcode in query]
