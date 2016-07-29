import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
user = 'hulinjun2006@126.com'
pwd = 'tanglirong520'
to = ['453105647@qq.com']
msg = MIMEMultipart()
msg['Subject'] = '这里是主题'
content1 = MIMEText('这里是正文！', 'plain', 'utf-8')
msg.attach(content1)
attfile = 'D:\\Program Files\\jmeter_anto\\result_log\\jtl\\TestReport_dbc.jtl'
basename = os.path.basename(attfile)
try:
	with open(attfile, 'rb') as fp:
		att = MIMEText(fp.read(), 'base64', 'utf-8')
		att["Content-Type"] = 'application/octet-stream'
		att.add_header('Content-Disposition', 'attachment',filename=('gbk', '', basename))
		encoders.encode_base64(att)
		msg.attach(att)
except OSError as resean:
	print(resean)
#-----------------------------------------------------------
s = smtplib.SMTP('smtp.126.com')
s.login(user, pwd)
s.sendmail(user, to, msg.as_string())
print('发送成功')
s.close()