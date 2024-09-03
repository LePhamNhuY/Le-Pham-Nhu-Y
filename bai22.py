# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 08:52:18 2024

@author: Le Pham Nhu Y
"""
a=float(input("Nhập vào a:"))
b=float(input("Nhập vào b:"))
if a==0 and b==0:
    print("Phương trình có vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
elif a!=0 and b!=0:
    print("Phương trình có nghiệm duy nhất:",-b/a)
else:
    print("Không hợp lệ")

