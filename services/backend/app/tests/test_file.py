from pathlib import Path

import pytest

from app.api.stores.file import File


def test_file_import():
    file = File()
    test_file_path = Path(__file__).parent / "files/test_stores.json"
    data = file.import_json(test_file_path)
    assert "Hayes" in data[0].values()


def test_file_import_error():
    with pytest.raises(FileNotFoundError):
        file = File()
        data = file.import_json("")
