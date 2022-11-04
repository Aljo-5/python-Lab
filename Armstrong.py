#!/usr/bin/env python
# coding: utf-8

# In[19]:


num=int(input("Enter the number"))

sum=0
temp=num
while(temp>0):
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if(num==sum):
    print("Armstrong number is:",num)
else:
    print("Not an Armstrong number",num)


# In[ ]:





# In[ ]:




