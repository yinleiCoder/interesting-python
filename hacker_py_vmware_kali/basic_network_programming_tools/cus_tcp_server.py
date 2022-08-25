import socket
import threading

"""
TCP服务端：
可以用TCP服务端做一个远程代码执行工具或代理工具。
以下是标准的多线程TCP服务器
"""

IP = "0.0.0.0"
PORT = 9998


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == '__main__':
    main()
