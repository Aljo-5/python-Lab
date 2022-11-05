#!/usr/bin/env python
# coding: utf-8

# In[11]:


num=int(input("Enter the number"))
sum=0
for i in range(1, num):
    if(num%i==0):
        sum=sum+i
if(num==sum):
    print(num,"is a perfect number")
        
else:
    print(num,"is not a perfect number")
    


# In[ ]:





# In[ ]:




