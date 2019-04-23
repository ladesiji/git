#!/usr/bin/python
# -*- coding=utf-8 -*-

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.ha.chinamobile.com'
POP3SVR = 'pop.ha.chinamobile.com'

who = 'wangyuchen@ha.chinamobile.com'
body = '''\
From: %(who)s
To: %(who)s
Subject: test msg
Hello World!
''' % {'who':who}

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail(who, [who], origMsg]
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('wangyuchen')
recvSvr.pass_('password')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody
