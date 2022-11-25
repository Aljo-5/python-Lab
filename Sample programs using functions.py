#!/usr/bin/env python
# coding: utf-8

# In[21]:


def add(a,b):
    c=a+b
    print("add",c)
add(3,5)


# In[6]:


def add(a,b):
    c=a+b
    print("REsult",c)
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
add(a,b)


# In[7]:


def add(a,b=5):
    c=a+b
    print("add",c)
add(3)    


# In[8]:


def add(a,b=5):
    c=a+b
    print("add",c)
add(3,6)    


# In[22]:


def oddeven(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")
oddeven(6)        


# In[23]:


def oddeven():
    a=int(input("Enter the number"))
    if(a%2==0):
       print("even")
    else:
        print("odd")
oddeven()         


# In[29]:


def add(a,b):
    c=a+b
    return c
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
z=add(x,y)
print("z=",z)


# In[31]:


def age(a):
    a=int(input("Enter the number"))
    print("a=",a)
age(a)    


# In[ ]:




