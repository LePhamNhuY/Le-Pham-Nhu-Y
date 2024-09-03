# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:34:19 2024

@author: Le Pham Nhu Y
"""
a=int(input("Nhập vào a:"))
b=int(input("Nhập vào b:"))
c=int(input("Nhập vào c:"))
if a>b:
    print("Số có giá trị lớn nhất là:",a)
elif c>a:
    print("Số có giá trị lớn nhất là:",c)
elif b>c:
    print("Số có giá trị lớn nhất là:",b)
else:
    print("Không có số lớn nhất")