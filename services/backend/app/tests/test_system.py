import json


def test_get(test_app):
    client = test_app.test_client()
    resp = client.get("/api?postcode=CA30HN&radius=1000")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data[0]["distance"] == 355.75
    assert data[0]["name"] == "Bletchley"


def test_get_missing_rad(test_app):
    client = test_app.test_client()
    resp = client.get("/api?postcode=CA30HN")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert "Invalid query parameters" in data["message"]


def test_get_no_stores(test_app):
    client = test_app.test_client()
    resp = client.get("/api?postcode=CA30HN&radius=1")
    assert resp.status_code == 204
