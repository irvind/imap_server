import socket
import ssl


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(sock)

ssl_sock.connect(('imap.yandex.ru', 993))
print(ssl_sock.recv(1024).strip())

commands = (
    'NOOP',
    'LOGIN irvinddz lxfrhnbs_irvind',
)

idx = 1
for cmd in commands:
    print('> ' + cmd.strip())

    q = '{:03} {}\r\n'.format(idx, cmd)
    ssl_sock.sendall(q.encode('ascii'))

    r = ssl_sock.recv(1024)
    print(r.strip())
