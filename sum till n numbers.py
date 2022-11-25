#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum
num=int(input("Enter the number: "))
print("The Sum till",num,"is",sum(num))


# In[ ]:




