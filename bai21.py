# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:42:37 2024

@author: Le Pham Nhu Y
"""
a=int(input("Nhập số bất kì:"))
chuoi={0:"Khong",1:"Mot",2:"Hai",3:"Ba",4:"Bon",5:"Nam",6:"Sau",7:"Bay",8:"Tam", 9:"Chin"}
if 0<=a<=9:
    print(chuoi[a])
else:
    print("Khong đoc đuoc")
