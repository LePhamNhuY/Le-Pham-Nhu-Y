# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:06:03 2024

@author: Le Pham Nhu Y
"""
import math
a=float(input("Nhập vào a:"))
b=float(input("Nhập vào b:"))
s=((a+b)/(math.pow(a,1/3)+math.pow(b,1/3))-math.pow(a*b,1/3))/math.pow((math.pow(a,1/3)-math.pow(b,1/3)),2)
print("Kết quả biểu thức:",s)
