import socket
from select import select


__all__ = ['start_server', 'shutdown']

server_socket = None


class SelectResult:
    def __init__(self):
        self.new_connections = []
        self.can_read = []
        self.can_write = []

    def __bool__(self):
        return bool(self.new_connections + self.can_read + self.can_write)


def start_server():
    global server_socket

    if server_socket is not None:
        raise RuntimeError('Server is already started')

    sock = socket.socket()
    sock.setblocking(False)
    sock.bind(('0.0.0.0', 8000))
    sock.listen(1)

    server_socket = sock


def select_server_socket(connections):
    mapping = {conn.get_sock_fileno(): conn for conn in connections}
    sockets = list(mapping.keys())

    inputs_rdy, outputs_rdy, _ = select(
        [server_socket] + sockets,
        sockets,
        []
    )

    result = SelectResult()
    for _input in inputs_rdy:
        if _input == server_socket:
            new_sock = _input.accept()[0]
            new_sock.setblocking(False)

            from imapserver.network import Connection
            result.new_connections.append(Connection(new_sock))
        else:
            result.can_read.append(mapping[_input])

    for _output in outputs_rdy:
        result.can_write.append(mapping[_output])


def shutdown():
    global server_socket

    if server_socket is None:
        raise RuntimeError('Server is not started')

    server_socket.close()
    server_socket = None
