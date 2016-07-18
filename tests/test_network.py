import pytest
from unittest import mock

from imapserver.network import start_server, Connection


class TestStartServer:
    def setup_method(self, method):
        self.socket_factory_mock = mock.Mock()
        self.socket_mock = mock.Mock()
        self.socket_factory_mock.return_value = self.socket_mock

    def test_if_socket_is_listening(self, monkeypatch):
        monkeypatch.setattr('socket.socket', self.socket_factory_mock)
        monkeypatch.setattr('imapserver.network.core.server_socket', None)
        start_server()

        from imapserver.network.core import server_socket
        assert server_socket is not None

        self.socket_mock.listen.assert_called_with(1)

    def test_if_socket_is_non_blocking(self, monkeypatch):
        monkeypatch.setattr('socket.socket', self.socket_factory_mock)
        monkeypatch.setattr('imapserver.network.core.server_socket', None)
        start_server()

        self.socket_mock.setblocking.assert_called_with(False)


class TestConnection:
    def create_test_connection(self, *args, **kwargs):
        return Connection(mock.Mock(*args, **kwargs))

    @pytest.mark.skip
    def test_send_message(self):
        conn = self.create_test_connection()
        message = b'* OK IMAP4rev1 Service Read'
        conn.send(message)
        conn.sock.send.assert_called_with(message)

    @pytest.mark.skip
    def test_send_partial_message(self):
        conn = self.create_test_connection(side_effect=[3, 5, 13])
        message = b'* OK IMAP4rev1 Service Read'

        conn.send(message)
        assert conn.send_buffer == b'IMAP4rev1 Service Read'

        conn.send(message)
        assert conn.send_buffer == b' Service Read'

        conn.send(message)
        assert conn.send_buffer == b''

    def test_new_connection_has_no_unsended_data(self):
        conn = self.create_test_connection()
        assert not conn.has_unsended_data()

    @pytest.mark.skip
    def test_connection_has_unsended_data(self):
        conn = self.create_test_connection(side_effect=[3])
        message = b'* OK IMAP4rev1 Service Read'
        conn.send(message)
        assert conn.has_unsended_data()

    @pytest.mark.skip
    def test_if_string_encoded(self):
        conn = self.create_test_connection()
        message = '* OK IMAP4rev1 Service Read'
        conn.send(message)

        assert conn.sock.send.assert_called_with(b'* OK IMAP4rev1 Service Read')

    # def test_read(self):
    #     sock = mock.Mock()
    #     conn = Connection(sock)
    #     conn.read()
    #     conn.read()
