#!/usr/bin/python 
#-*-coding:GBK -*- 

import smtplib 
from email.mime.text import MIMEText 
from email.header import Header 

sender = 'wangbin184035@hollysys.com' 
receivers = ['wangbin184035@hollysys.com' ] # �����ʼ���������Ϊ���QQ��������������� 

# ������������һ��Ϊ�ı����ݣ��ڶ��� plain �����ı���ʽ�������� utf-8 ���ñ��� 
message = MIMEText('Python �ʼ����Ͳ���...', 'plain', 'utf-8') 
message['From'] = Header("����̳�", 'utf-8') # ������ 
message['To'] = Header("����", 'utf-8') # ������ 

subject = 'Python SMTP �ʼ�����' 
message['Subject'] = Header(subject, 'utf-8') 

try: 
    smtpObj = smtplib.SMTP('localhost') 
    smtpObj.sendmail(sender, receivers, message.as_string()) 
    print("�ʼ����ͳɹ�")
except smtplib.SMTPException: 
    print("Error: �޷������ʼ�")