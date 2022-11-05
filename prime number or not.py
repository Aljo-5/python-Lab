#!/usr/bin/env python
# coding: utf-8

# In[3]:


n=int(input("Enter the number: "))
for i in range(2, n):
    if(n%i==0):
        print("It is not prime number")
        break;
else:
    print("It is a prime number")
    


# In[ ]:




