#!/usr/bin/python
#-*-coding:GBK -*- 

fo = open("foo.txt", "r")
print("�ļ���: ", fo.name)
print("�Ƿ��ѹر� : ", fo.closed)
print("����ģʽ : ", fo.mode)

#��ȡ
str = fo.read(2)
print("��ȡ���ַ����� : ", str)

#�ر�
fo.close()