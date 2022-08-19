import json

from dundie.settings import DATABASE_PATH

SCHEMA_DB = {"people": {}, "balance": {}, "movement": {}, "user": {}}


def connect(database_path=DATABASE_PATH) -> dict:
    """Connect to the database and return dict data."""
    try:
        with open(database_path, "r") as f:
            return json.loads(f.read())
    except (FileNotFoundError, json.JSONDecodeError):
        return SCHEMA_DB


def commit(database: dict, database_path=DATABASE_PATH) -> None:
    """Commit the database to the file."""
    if database.keys() != SCHEMA_DB.keys():
        raise RuntimeError("Database schema is not valid.")

    with open(database_path, "w") as f:
        f.write(json.dumps(database, indent=4))
