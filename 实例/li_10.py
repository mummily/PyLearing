#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ��Ŀ����ͣһ�����������ʽ����ǰʱ�䡣
# �����������

import time
 
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
 
# ��ͣһ��
time.sleep(1)
 
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))