# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:41:19 2024

@author: Le Pham Nhu Y
"""

a=int(input("Nhập vào a:"))
b=int(input("Nhập vào b:"))
c=int(input("Nhập vào c:"))
if a>b:
    t=a
    a=b
    b=t
elif b>c:
    t=b
    b=c
    c=t
else:
    t=a
    a=c
    c=t
print("Thứ tự tăng dần là:",a,b,c)


