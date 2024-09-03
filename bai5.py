# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:29:05 2024

@author: Le Pham Nhu Y
"""
from datetime import timedelta
gio=int(input("Nhập giờ:"))
phut=int(input("Nhập phút:"))
giay=int(input("Nhập giây:"))
time1=timedelta(hours=gio, minutes=phut, seconds=giay)
print("Kết quả",time1,"đổi ra giây:",gio*3600+phut*60+giay,"giây")
