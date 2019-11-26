#!/usr/bin/python

"""
    使用SocketServer类，TCPServer 和 StreamRequestHandler，
    完成时间戳TCP 服务器
"""

from socketserver import (TCPServer as TCP,
        StreamRequestHandler  as SRH)
from time import ctime

HOST = ""
POST = 8421
ADDR = (HOST, POST)

class MyRequestHandler(SRH):

    def handle(self):
        print(f"... connected form:{self.client_address}")
        self.wfile.write(f"{ctime()} {self.rfile.readline().decode()}"
                .encode('utf-8'))

tcpServ = TCP(ADDR, MyRequestHandler)
print("waiting for connection...")
tcpServ.serve_forever()
