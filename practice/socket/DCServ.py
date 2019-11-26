#/usr/bin/python

"""
    半双工聊天程序-服务器端
    消息发送出去后，要等到有回复了才能发送下一条消息
    服务启动后等待客户端消息，回复客户端消息。
"""

from socket import *
from time import ctime, sleep

HOST = ''
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
udpSerSock.setblocking(0)

addr=''
while True:
    print('waiting for messagdde...')
    try:
        data, addr = udpSerSock.recvfrom(BUFSIZ)
    except Exception:
        sleep(1)
        pass
    else:
        if data.decode('utf-8') =='bye':
            print('对方挂断对话')
            break
        print(f"{addr}> {data.decode('utf-8')}")
    if not addr:
        continue
    my_msg = input('> ')
    if my_msg:
        udpSerSock.sendto(my_msg.encode('utf-8'), addr)
    if my_msg == 'bye':
        print("主动挂断对话")
        break

udpSerSock.close()
    

