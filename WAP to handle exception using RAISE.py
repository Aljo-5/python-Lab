#!/usr/bin/env python
# coding: utf-8

# In[16]:


try: 
    num = int(input("Enter a positive integer: ")) 
    if(num <= 0): 
        raise ValueError("That is a negative number!")
except ValueError as e:
        print(e)


# In[ ]:





# In[ ]:




