# -*- coding: utf-8 -*-
"""1st character replaced with $

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ar4zmc_iv134cxzPqxsdImZakj3uuUZn
"""

str1=input("Enter the string:")
s=str1[0]
for i in range(len(str1)):
  str=str1.replace(str1[0],'$')
  str1=s+str[1:]
print(str1)