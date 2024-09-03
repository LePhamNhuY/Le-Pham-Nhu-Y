# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:19:32 2024

@author: Le Pham Nhu Y
"""
h=int(input("Nhập giờ:"))
t=int(input("Nhập phút:"))
s=int(input("Nhập giây:"))
if 0<=h<=23 and 0<=t<=59 and 0<=s<=59:
    print("Giờ hợp lệ")
else:
    print("Không hợp lệ")

