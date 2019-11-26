#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
    创建TCP客户端
    提示用户输入，并发关到服务器
    接收服务器返回的添加了时间戳的相同消息
    并显示结果
"""

import socket

HOST = '192.168.43.1'
PORT = 8421
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())

tcpCliSock.close()
