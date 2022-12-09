#!/usr/bin/env python
# coding: utf-8

# In[3]:


def swap(string):
    #storing 1st character
    start=string[0]
    #storing last character
    end=string[-1]
    swapped_string = end + string[1:-1] + start
    print(swapped_string)
s=input("Enter a string:")  
swap(s)


# In[ ]:




