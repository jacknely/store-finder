from pathlib import Path

import pytest
import requests

from app import create_app
from app.api.stores.file import File
from app.api.stores.stores import Stores


@pytest.fixture(scope="module")
def test_store():
    """fixture to be used to initate tests with test data"""
    file = File()
    test_file_path = Path(__file__).parent / "files/test_stores.json"
    data = file.import_json(test_file_path)
    stores = Stores()
    stores.add_data(data)
    yield stores


@pytest.fixture(scope="module")
def test_app():
    """instantiates a flask object with config test"""
    app = create_app()
    app.config.from_object("app.config.TestingConfig")
    with app.app_context():
        yield app


# Below are Mock Responses for calls to postcode.io


class MockResponse404:
    def __init__(self):
        self.status_code = 404


@pytest.fixture
def mock_response_404(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse404()

    monkeypatch.setattr(requests, "post", mock_post)


class MockResponse200:
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json():
        return {
            "status": 200,
            "result": [
                {
                    "query": "GU34 2QS",
                    "result": {
                        "postcode": "GU34 2QS",
                        "longitude": -0.805149,
                        "latitude": 51.818086,
                    },
                },
                {
                    "query": "GU34 2Q3",
                    "result": {
                        "postcode": "GU34 2Q3",
                        "longitude": 45.67,
                        "latitude": -24.89,
                    },
                },
            ],
        }


@pytest.fixture
def mock_response_200(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse200()

    monkeypatch.setattr(requests, "post", mock_post)
