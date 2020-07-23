from pathlib import Path

from app.api.stores.file import File
from app.api.stores.stores import Stores

file = File()
file_path = Path(__file__).parent / "files/stores.json"
data = file.import_json(file_path)
stores = Stores()
stores.add_data(data)
stores.add_location()
