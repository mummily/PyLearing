#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ��Ŀ���ж�101-200֮���ж��ٸ����������������������
# ����������ж������ķ�������һ�����ֱ�ȥ��2��sqrt(�����)������ܱ����������������������������֮������
 
total = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d' % m)
        total += 1
    leap = 1
print('The total is %d' % total)