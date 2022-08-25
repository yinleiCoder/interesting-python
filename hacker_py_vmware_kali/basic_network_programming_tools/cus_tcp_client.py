import socket
"""
TCP客户端：
渗透测试过程中，经常需要创建一个TCP客户端，来测试服务、发送垃圾数据，进行fuzz等
如果黑客潜伏在某大型企业的内网环境中，则不太可能直接获取网络工具或编译器，甚至连cv操作或连接外网都用不了。
这时，创建一个TCP客户端攻破目标及其并保持对其的访问权限。
"""

target_host = "www.baidu.com"
target_port = 80

# AF_INET代表使用标准的IPV4或者主机名，SOCK_STREAM表示这是一个TCP客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"Get / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()