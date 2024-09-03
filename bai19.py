# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:20:15 2024

@author: Le Pham Nhu Y
"""
a=int(input("Nhập vào a:"))
b=int(input("Nhập vòa b:"))
c=int(input("Nhập vào c:"))
d=int(input("Nhập vào d:"))
nhonhat=a
if nhonhat>b:
    nhonhat=b
if nhonhat>c:
    nhonhat=c
if nhonhat>d:
    nhonhat=d
else:
    print("Số nhỏ nhất là:",nhonhat)