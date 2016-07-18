import sqlite3
import pytest


@pytest.fixture
def sqlite_cursor():
    return sqlite3.connect(':memory:').cursor()


@pytest.fixture
def my_fixt(request):
    return getattr(request.function, "my_param", "lol")
