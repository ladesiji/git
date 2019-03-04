"""
    使用python 来发送电子邮件
"""


# 导入email模块构造邮件
from email.mime.text import MIMEText

# 构造一个纯文本邮件
msg = MIMEText('hello, this is wangyuchen.I love you. send by Python...', 'plain', 'utf-8')


# 发件人邮件服务器信息
from_addr = 'wangyuchen@ha.chinamobile.com'
password = 'Winter18'
smtp_server = 'smtp. chinamobile.com'

# 收件人地址：
to_address = 'bailu@cmos.chinamobile.com'


# 调用 smtplib 模块发送邮件
import smtplib

# 创建smtp实例
server = smtplib.SMTP('smtp.chinamobile.com',25)

# 显示发送细节
# server.debuglevel()

# 传入smtp服务器的账号密码
server.login(from_addr, password)

# 发送邮件
server.sendmail(from_addr, [to_address], msg.as_string())

# 退出登陆
server.quit()

print('发送成功')
