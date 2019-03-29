# !usr/bin/python
# -*- coding = UTF-8 -*-
# 文件名: client.py

"""
    socket 练习
    客户端程序
"""

import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = "192.168.43.1"       # 主机地址
port = 8421                 # 设置端口号

s.connect((host, port))
print s.recv(1024)
s.close()
