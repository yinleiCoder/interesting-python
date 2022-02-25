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
    阻塞等待连接请求(新套接字)<---三次握手---connect()
       |                                 |
    recv() <------------------------- send()
       |                                 |
    send() -------------------------> recv()
       |                               |
    close()<-------------------------close()

Socket客户端：

"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

while True:
    re_data = input()
    client.send(re_data.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))

# client.send('yinlei'.encode('utf8'))
# data = client.recv(1024)
# print(data.decode('utf8'))
#
# client.close()




