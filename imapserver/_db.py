import sqlite3
import os


_db = None


class DB:
    db_path = 'db.sqlite'

    def __init__(self):
        if not os.path.exists(self.db_path):
            self.conn = self.init_database()
        else:
            self.conn = sqlite3.connect(self.db_path)

        self.cur = self.conn.cursor()

    def init_database(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        sql_file_path = os.path.join(os.path.dirname(__file__), 'sql', 'init.sql')
        with open(sql_file_path, 'r') as sql_file:
            cur.executescript(sql_file.read())

        return conn

    def execute_sql(self, sql, *args):
        self.cur.execute(sql, *args)
        return self.cur.fetchall()

    def select(self, table, where='', fields='*', **query_args):
        q = 'SELECT {} FROM {}'.format(fields, _from)
        if where:
            q += ' WHERE ' + where

        self.cur.execute(q, query_args)
        return self.cur.fetchall()

    def shutdown(self):
        self.cur.close()
        self.conn.close()


def get_db():
    global _db
    if _db is None:
        _db = DB()

    return _db


def get_user(login):
    db = get_db()
    result = db.select(table='users', where='login = :login', login=login)

    if len(result) == 0:
        return None

    return result[0]
