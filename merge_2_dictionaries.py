# -*- coding: utf-8 -*-
"""merge 2 dictionaries

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QLEFn0oA6DIXtnVPsR3k1u6d3KpSEmOO
"""

x={"Name":"Aljo","Age":20,"Year":1999, "College":"Nirmala"}
y={"Sub":"Python","Year":2000,"College":"Scms"}
print("First dictionary",x)
print("Second dictionary",y)
x.update(y)
print("Dictionary after merging",x)