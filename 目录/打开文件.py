#!/usr/bin/python
#-*-coding:GBK -*- 

fo = open("foo.txt", "r")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

#读取
str = fo.read(2)
print("读取的字符串是 : ", str)

#关闭
fo.close()