#!/usr/bin/env python
"""
    生成随机 登陆 日志
    包括 日期 - 邮箱地址 
"""

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')
txt = ""
for i in range(randrange(5, 11)):
    dtint = randrange(2**32)      # 选取随机数
    dtstr = ctime(dtint)          # 选取日期
    llen = randrange(4, 8)        # login 长度
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)    # 域名 长度
    dom = ''.join(choice(lc) for j in range(dlen))
    txt += f'{dtstr}::{login}@{dom}.{choice(tlds)}::{dtint}-{llen}-{dlen}'+"\n"
with open('redata.txt', 'w') as f:
    f.write(txt)
