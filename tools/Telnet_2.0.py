
#encoding=utf-8

"""
    作者：王雨晨
    日期：3/7/2019
    功能：自动登录交换机，并保存配置文件
    版本：2.0
    修改：不用搭建TFTP服务器，直接读取display current-configuration
    执行时，py文件目录下需要有address.txt 的地址文件。
    获取配置文件保存在目录下。

"""


import telnetlib
import os
import time


def readfile(filename):
    """
        文件内容格式为制表符分隔的数据
        读取TXT log ,返回列表格式数据[[host1,user,password],...[[hostn,user,password]]
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    data = [line.strip('\n').split('\t') for line in lines]
    return data


def do_telnet(Host, Username, Password, comand):
    """
        telnet 功能，返回读取到的配置文件
    """
    # 连接Host服务器
    tn = telnetlib.Telnet(Host, timeout=10)
    # debug模式，看到交到信息
    # tn.set_debuglevel(2)
    # 输入登录名
    tn.read_until(b'Username:', timeout=3)
    tn.write(Username.encode('ascii') + b'\r\n')
    # 输入登录密码
    tn.read_until(b'Password:', timeout=3)
    tn.write(Password.encode('ascii') + b'\r\n')

    print("登陆{}成功，正在读取配置信息...".format(Host))

    # 执行命令
    tn.write(b'\r\n')

    tn.write(comand.encode('ascii') + b'\r\n')
    x = '##'
    data = []
    while x != b'   ':
        x = tn.read_until(b'--More--', timeout=1)
        data.append(x)
        tn.write(b'   ')
    tn.close()
    return data


def writefile(data, filepath):
    """
        以Host 为文件名，写入数据
    """
    # 数据处理
    txt = b''.join(data)
    s = txt.find(b' ---- More')
    while s != -1:
        txt = txt[0:s - 1] + txt[s + 67:]
        s = txt.find(b' ---- More')
    start = txt.find(b'current-configuration')
    end = txt.find(b'return')
    result = (txt[start + 22:end + 8])

    # 数据写入
    with open(filepath, 'w') as f:
        f.write(result.decode())


def main():
    """
        主函数
    """
    # 读取文件获取IP地址账号密码
    # ip_address_filename = "D:/tftp/address.txt"
    ip_address_filename = "address.txt"
    print()
    print("*" * 20)
    print('正在读取地址文件...')

    # 获取日期
    day = time.strftime("%Y%m%d", time.localtime())
    # 检查配置文件目录，没有就创建
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '配置文件-{}'.format(day))
    if not os.path.exists(path):
        os.makedirs(path)

    try:
        data = readfile(ip_address_filename)
        print('读取地址文件完成')
        print("共有 {} 个地址需要访问".format(len(data)))
        print("*" * 20)
        # 记录登陆交换机个数
        num = 0
        # 按顺序登陆交换机列表中地址
        Username = 'lyyd'
        Password = 'lyydqyw'
        for i, value in enumerate(data):
            Host = value[0]
            print()
            print('正在登陆第 {} 个地址 {}...'.format(i+1, Host))
            # tftp 服务器需要修改成自已的
            comand = 'display current-configuration'

            # 调用telnet 函数，完成登陆和保存
            try:
                configuration = do_telnet(Host, Username, Password, comand)
                filepath = os.path.join(path, '{}.txt'.format(Host))
                writefile(configuration, filepath)
                print('{} 配置保存已完成'.format(Host))
                num += 1
            except Exception as e:
                print("登录 {} 失败，原因: {}".format(Host, e))

        print()
        print("*" * 20)
        print('已下载 {} 个文件，程序结束!'.format(num))

    except Exception as e:
        print(e)


if __name__ == main():
    main()
