#!/usr/bin/python 
#-*-coding:GBK -*- 
# �ļ�����client.py 

import socket # ���� socket ģ�� 

s = socket.socket() # ���� socket ���� 
host = socket.gethostname() # ��ȡ���������� 
port = 12345 # ���ö˿ں� 
s.connect((host, port)) 

print(s.recv(1024).decode())
s.close()