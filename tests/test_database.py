import pytest

from dundie.database import SCHEMA_DB, commit, connect


@pytest.mark.unit
def test_database_schema():
    db = connect()
    assert db.keys() == SCHEMA_DB.keys()


@pytest.mark.unit
def test_commit_to_database():
    db = connect()
    data = {"name": "Joe Doe", "role": "Salesman", "dept": "Sales"}
    db["people"]["joe@doe.com"] = data
    commit(db)

    db = connect()
    assert db["people"]["joe@doe.com"] == data
