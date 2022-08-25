"""Core module of dundie"""
from csv import reader

from dundie.database import add_person, commit, connect
from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database.

    >>> len(load('assets/people.csv'))
    2
    """
    try:
        csv_data = reader(open(filepath, "r"))
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
    db = connect()
    people = []
    header = ["name", "dept", "role", "email"]
    for row in csv_data:
        person_data = dict(zip(header, [word.strip() for word in row]))
        pk = person_data.pop("email")
        person, created = add_person(db, pk, person_data)

        return_data = person.copy()
        return_data["created"] = created
        return_data["pk"] = pk
        people.append(return_data)

    commit(db)
    return people
