#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ��Ŀ����� 9*9 �˷��ھ���
# ����������������п��ǣ���9��9�У�i�����У�j������
 
for i in range(1, 10):
    print()
    for j in range(1, i+1):
        print("%d*%d=%d " % (i, j, i*j),end='')