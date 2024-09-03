# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:00:58 2024

@author: Le Pham Nhu Y
"""
from datetime import timedelta
gio=int(input("nhập giờ thứ nhất:"))
phut=int(input("nhập phút thứ nhất:"))
giay=int(input("nhập giây thứ nhất:"))
h=int(input("Nhập giờ thứ hai:"))
t=int(input("Nhập phút thứ hai:"))
s=int(input("Nhập phút thứ hai:"))
time1=timedelta(hours=gio, minutes=phut, seconds=giay)
time2=timedelta(hours=h, minutes=t, seconds=s)
print("Cộng hai giờ được: ",time1+time2)
print("Trừ hai giờ được: ",time1-time2)
