import pytest

from app.api.stores.postcodeio import search


def test_search_single():
    result = search(["CA30HN"])
    assert "CA3 0HN" in result[0].values()


def test_search_terminated():
    with pytest.raises(ValueError):
        result = search(["GU195DG"])


def test_search_multi():
    result = search(["CA30HN", "LA15DF"])
    assert "CA3 0HN" in result[0].values()
    assert "LA1 5DF" in result[1].values()


def test_search_single_no_value():
    with pytest.raises(ValueError):
        result = search([""])


def test_search_single_bad_value():
    with pytest.raises(ValueError):
        result = search(["g^"])


def test_search_single_value():
    with pytest.raises(OSError):
        result = search("")


def test_search_single_404_code(mock_response_404):
    with pytest.raises(IOError):
        result = search(["CA30HN"])
