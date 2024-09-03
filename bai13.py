# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:15:42 2024

@author: Le Pham Nhu Y
"""
ngay=int(input("Nhập ngày:"))
thang=int(input("Nhập tháng:"))
nam=int(input("Nhập năm:"))
#a) 
print(f"{ngay}/{thang}/{nam}")
#b)
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
#c) 
print(f"{nam}/{thang}/{ngay}")
