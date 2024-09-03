# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:01:43 2024

@author: Le Pham Nhu Y
"""
n=int(input("Nhập vào n:"))
digits=[int(i) for i in str(n)]
digits.sort()
tangdan=int(''.join(map(str,digits)))
print("Thứ tự tăng dần là:",tangdan)
