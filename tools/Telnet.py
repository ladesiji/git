
#encoding=utf-8

"""
    作者：王雨晨
    日期：2/15/2019
    功能：自动登录交换机，并保存配置文件
    版本：1.0

"""


import telnetlib
import time


def readfile(filename):
    """
        文件内容格式为制表符分隔的数据
        读取TXT log ,返回列表格式数据[[host1,user,password],...[[hostn,user,password]]
    """
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    date = [line.strip('\n').split('\t') for line in lines]
    return date


def do_telnet(Host, Username, Password, comands):

    # 连接Host服务器
    tn = telnetlib.Telnet(Host,timeout=10)
    tn.set_debuglevel(2)

    # 输入登录名
    tn.read_until(b'Username:')
    tn.write(Username.encode('ascii') + b'\r\n')

    # 输入登录密码
    tn.read_until(b'Password:')
    tn.write(Password.encode('ascii') + b'\r\n')

    # 执行命令
    tn.write(b'\r\n')
    for comand in comands:
        tn.write(comand.encode('ascii') + b'\r\n')
        if comand[:4]=='save':
            print('正在保存配置文件...')
            tn.read_until(b'[Y/N]:')
            tn.write('y'.encode('ascii')+b'\r\n')
            tn.read_until(b'[Y/N]:')
            tn.write('y'.encode('ascii')+b'\r\n')
        tn.read_until(b'successfully')
        # 执行命令间隔时间 1  秒钟
        time.sleep(1)
    tn.close()
    print('保存完成!')


def main():
    """
        主函数
    """
    # 读取文件获取IP地址账号密码
    ip_address_filename = "D:/tftp/address.txt"
    print('正在读取地址文件...')
    date = readfile(ip_address_filename)
    print('读取文件完成')

    # 记录登陆交换机个数
    num = 0

    # 按顺序登陆交换机列表中地址
    for i in date:
        Host = i[0]
        Username = i[1]
        Password = i[2]
        comands = ['save {}.cfg'.format(Host), 'tftp 10.100.3.100 put {}.cfg'.format(Host)]
        print()
        print('正在登陆{}'.format(Host))
        # 调用telnet 函数，完成登陆和保存
        do_telnet(Host,Username,Password,comands)
        print()
        print('{}配置保存已完成'.format(Host))
        print("*"*20)
        num += 1

    print()
    print("*"*20)
    print('已下载{}文件，结束!'.format(num))


if __name__ == main():
    main()
