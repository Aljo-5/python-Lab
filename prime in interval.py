#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=int(input("Enter the lower range: "))
b=int(input("Enter the upper range: "))
for number in range(a,b+1):
    if(number>1):
        for i in range(2,number):
            if(number%i==0):
                break
        else:
            print(number)


# In[ ]:




