import pytest
import socket


def start_test_server(port=8000):
    pass


def connect_to_server(port=8000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', port))
    return sock


@pytest.mark.skip
def test_receiving_greetings():
    start_test_server()
    sock = connect_to_server()

    data = sock.read(1024)
    assert data[:2] == b'OK'
