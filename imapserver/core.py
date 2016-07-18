from imapserver.network import start_server, select_server_socket


class ImapServer:
    def __init__(self):
        self.connections = []

    def run(self):
        self.init()
        self.serve_loop()

    def init(self):
        start_server()

    def serve_loop(self):
        while True:
            result = select_server_socket(self.connections)
            self.connections.extend(result.new_connections)
