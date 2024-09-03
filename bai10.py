# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:39:38 2024

@author: Le Pham Nhu Y
"""
sx=input("Nhập biển số xe:")
s=sum(int(chuso) for (chuso) in (sx))
hangchuc=s//10
hangdv=s%10
print("Vậy số xe có",hangchuc+hangdv,"nút")
