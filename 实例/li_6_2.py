#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# ʹ�õݹ�
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
 
# ����˵�10��쳲���������
print(fib(10))