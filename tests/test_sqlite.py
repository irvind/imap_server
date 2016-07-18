def test_can_create_database(sqlite):
    sqlite.executescript("""CREATE TABLE cats (
        id INTEGER PRIMARY KEY,
        name TEXT
    );""")

    cursor = sqlite.execute("""SELECT name FROM sqlite_master
        WHERE type='table' AND name='cats'
    """)

    assert cursor.fetchone() is not None


def test_can_insert_and_select(sqlite):
    sqlite.executescript("""CREATE TABLE cats (
        id INTEGER PRIMARY KEY,
        name TEXT
    );

    INSERT INTO cats(name) VALUES ('mishca'), ('vasya');
    """)

    cursor = sqlite.execute("SELECT name FROM cats")

    assert cursor.fetchone()[0] == 'mishca'
    assert cursor.fetchone()[0] == 'vasya'
    assert cursor.fetchone() is None


def test_fetched_row_is_tuple(sqlite):
    cursor = sqlite.execute("SELECT name FROM cats")
    row = cursor.fetchone()
    assert isinstance(row, tuple)
test_fetched_row_is_tuple.db_script = 'simple_db'
