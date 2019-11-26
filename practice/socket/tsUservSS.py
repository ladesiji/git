#!/usr/bin/python

"""
    使用SocketServer类，UDPServer 和 StreamRequestHandler，
    完成时间戳UDP 服务器
"""

from socketserver import (UDPServer as UDP,
        BaseRequestHandler  as BRH)
from time import ctime

HOST = ""
POST = 8421
ADDR = (HOST, POST)

class MyRequestHandler(BRH):

    def handle(self):
        print(f"... connected form:{self.client_address[0]}")
        data, sock = self.request
        sock.sendto(f"{ctime()} {data.decode()}".encode('utf-8'), 
             self.client_address)

udpServ = UDP(ADDR, MyRequestHandler)
print("waiting for connection...")
udpServ.serve_forever()
