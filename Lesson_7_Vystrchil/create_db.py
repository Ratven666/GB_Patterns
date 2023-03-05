import sqlite3

from kmd_framework.common.variables import DB_NAME


def create_db():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    with open("create_db.sql", "r") as f:
        text = f.read()
    cur.executescript(text)
    cur.close()
    con.close()
