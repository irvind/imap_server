import pytest

from imapserver.db import DbLayer


def test_single_select():
    layer = DbLayer('cat')
    row = layer.select(name='Jinger')[0]
    assert row['name'] == 'Jinger'


@pytest.mark.skip
def test_select_order_by():
    # Jinger 5
    # Kleo 7
    # Joseph 8
    layer = DbLayer('cat')
    rows = layer.select(age=('>', 5), order_by=['age'])

    assert rows[0]['name'] == 'Jinger'
    assert rows[1]['name'] == 'Kleo'
    assert rows[2]['name'] == 'Joseph'


@pytest.mark.skip
def test_select_order_by_desc():
    layer = DbLayer('cat')
    rows = layer.select(age=('>', 5), order_by=['-age'])

    assert rows[2]['name'] == 'Joseph'
    assert rows[1]['name'] == 'Kleo'
    assert rows[0]['name'] == 'Jinger'
