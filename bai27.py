# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:13:05 2024

@author: le Pham Nhu Y
"""
hinh=input("Nhập hình:")
if hinh=="v":
    print("Tính P và S của hình vuông")
    canh=float(input("Nhập cạnh:"))
    print("P=",canh*4)
    print("S=",canh*canh)
elif hinh=="n":
    print("Tính P và S của hình chữ nhật")
    d=float(input("Nhập chiều dài:"))
    r=float(input("Nhập chiều rộng:"))
    print("P=",(d+r)*2)
    print("S=",d*r)
elif hinh=="t":
    print("Tính P và S của hình tròn")
    r=float(input("Nhập bán kính:"))
    print("P=",r*2*3.14)
    print("S=",r*r*3.14)
else:
    print("Không hợp lệ")




