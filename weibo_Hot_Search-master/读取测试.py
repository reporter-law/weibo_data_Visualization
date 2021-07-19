"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
path= "J:\微博热度\\2020年\\07月\\15日\\2020年07月15日13点.md"
with open(path, "r", encoding="gbk")as f:
    content = f.read()
    print(content)
