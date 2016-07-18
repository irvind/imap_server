def test_can_create_database_in_memory(sqlite_cursor):
    sqlite_cursor.execute('SELECT * FROM sqlite_master')


def test_can_create_database(sqlite_cursor, my_fixt):
    sqlite_cursor.executescript("""CREATE TABLE cats (
        id INTEGER PRIMARY KEY,
        name TEXT
    );""")

    sqlite_cursor.execute("""SELECT name FROM sqlite_master
        WHERE type='table' AND name='cats'
    """)

    assert sqlite_cursor.fetchone() is not None

    assert my_fixt == 'ok'
test_can_create_database.my_param = 'ok'


def test_can_insert_and_select(sqlite_cursor, my_fixt):
    sqlite_cursor.executescript("""CREATE TABLE cats (
        id INTEGER PRIMARY KEY,
        name TEXT
    );

    INSERT INTO cats(name) VALUES ('mishca'), ('vasya');
    """)

    sqlite_cursor.execute("SELECT name FROM cats")

    assert sqlite_cursor.fetchone()[0] == 'mishca'
    assert sqlite_cursor.fetchone()[0] == 'vasya'
    assert sqlite_cursor.fetchone() is None

    assert my_fixt == 'lol'
