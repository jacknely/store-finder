from pathlib import Path

import pytest

from app.api.stores.file import File
from app.api.stores.stores import Stores


def test_store_init():
    store = Stores()
    assert store.data == []


def test_import_stores_error():
    with pytest.raises(ValueError):
        test_stores = Stores()
        test_stores.add_data("")
        assert len(test_stores.data) == 2


def test_search_stores_zero(test_store, mock_response_200):
    test_store.add_location()
    resp = test_store.search_stores("GU34 2QS", 100)
    assert "distance" in resp[0].keys()
    assert 0.0 in resp[0].values()


def test_search_stores_big(test_store, mock_response_200):
    test_store.add_location()
    resp = test_store.search_stores("GU34 2Q3", 10000)
    assert "distance" in resp[1].keys()
    assert 9655.28 in resp[1].values()


def test_import_stores():
    file = File()
    test_file_path = Path(__file__).parent / "files/test_stores.json"
    data = file.import_json(test_file_path)
    test_stores = Stores()
    test_stores.add_data(data)
    assert len(test_stores.data) == 2


def test_add_location(test_store, mock_response_200):
    test_store.add_location()
    assert len(test_store.data) == 2


def test_add_location_no_data(test_store, mock_response_200):
    delattr(test_store, "data")
    with pytest.raises(AttributeError):
        test_store.add_location()


def test_get_distance(test_store):
    """results comparable to www.movable-type.co.uk/scripts/latlong.html"""
    point_1 = (40.7486, -73.9864)
    point_2 = (45.7486, -79.9864)
    result = test_store.get_distance(point_1, point_2)
    assert float(result) == 678.2359432446029


def test_get_distance_big(test_store):
    """results comparable to www.movable-type.co.uk/scripts/latlong.html"""
    point_1 = (0.7486, -31.9864)
    point_2 = (5.7486, -9.9864)
    result = test_store.get_distance(point_1, point_2)
    assert float(result) == 2499.91062530837


def test_get_distance_error(test_store):
    with pytest.raises(TypeError):
        point_1 = 0.7486
        point_2 = (5.7486, -9.9864)
        test_store.get_distance(point_1, point_2)


def test_get_distance_error_string(test_store):
    with pytest.raises(TypeError):
        point_1 = (0.7486, "233")
        point_2 = (5.7486, -9.9864)
        test_store.get_distance(point_1, point_2)
