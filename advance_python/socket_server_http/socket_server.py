"""
Socket编程流程：
    Socket
       |
    bind(协议，地址，端口)
       |
    listen(监听客户端socket请求)
       |
    accept()                             Socket
       |                                  |
    阻塞等待连接请求(新套接字)<-----三次握手---connect()
       |                                 |
    recv() <------------------------- send()
       |                                 |
    send() -------------------------> recv()
       |                               |
    close()<-------------------------close()

Socket服务端：
    多客户端用多线程
"""

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
sock, addr = server.accept()

# 获取从客户端发送的数据
while True:
    data = sock.recv(1024)
    print(data.decode('utf8'))
    re_data = input()
    sock.send(re_data.encode('utf8'))
    # sock.send(f'hello {data.decode("utf8")}'.encode('utf8'))
    # sock.close()
    # server.close()