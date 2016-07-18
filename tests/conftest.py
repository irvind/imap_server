import sqlite3
import pytest
import sys


simple_db = """CREATE TABLE cats (
    id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO cats(name) VALUES ('mishca'), ('vasya');
"""


@pytest.fixture
def sqlite(request):
    db_conn = sqlite3.connect(':memory:')

    script_name = getattr(request.function, 'db_script', None)
    if script_name:
        # script = getattr(sys.modules[__name__], script_name)
        script = globals()[script_name]
        db_conn.executescript(script)

    return db_conn
