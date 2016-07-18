class Connection:
    def __init__(self, sock):
        self.sock = sock
        self.buffer = bytearray()
        self.send_buffer = bytearray()

    def send(self, msg):
        """
        Send octets to client.
        """
        l = self.sock.send(msg)
        print(l)
        self.buffer.extend(msg[l:])

    def read(self):
        """
        Read octets from client and put them into the buffer.
        """
        pass

    def get_buffer_data(self):
        """
        Get buffer content.
        """
        pass

    def has_unsended_data(self):
        pass

    def has_command(self):
        pass

    def pop_command(self):
        pass

    def get_sock_fileno(self):
        pass


class Session:
    def __init__(self, connection):
        self.state = 'not_authenticated'
        self.conn = connection
        self.mailbox = None

    def process_command(self):
        TaskManager = None
        validate_command = lambda x: True
        parse_command = None
        command = self.conn.pop_command()
        if not validate_command(command):
            pass
        else:
            def finish_func():
                pass

            TaskManager.run_task(
                connection=self,
                command=parse_command(command),
                finish=finish_func
            )
