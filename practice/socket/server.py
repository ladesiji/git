#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py
"""
    socket 练习
    模拟一个TCP服务器
"""

import socket           # 导入 socket 模块

ss = socket.socket()    # 创建 socket 对象
host = "192.168.43.1"   # 主机地址   
port = 8421             # 设置端口
ss.bind((host, port))   # 绑定地址 端口

ss.listen(5)            # 等待客户端连接

while True:
    cs = ss.accept()    # 建立客户端连接
    print(f"{cs[1]} 连接成功")
    print('receve:'cs[0].recv(1024).decode())
    cs[0].send(f"欢迎{cs[1]}访问 {host}".encode('utf-8'))
    cs[0].close         # 关闭连接




