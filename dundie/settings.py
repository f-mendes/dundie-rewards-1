import os

SMTP_HOST = "localhost"
SMTP_PORT = 25
SMTP_TIMEOUT = 5

EMAIL_FROM = "dundie@localhost"
ROOT_PATH = os.path.dirname(__file__)
DATABASE_PATH = os.path.join(ROOT_PATH, "..", "assets", "database.json")
