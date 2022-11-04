#!/usr/bin/env python
# coding: utf-8

# In[10]:


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
op=input("Enter the operator:  +,-,*,/,%,^")
if(op=="+"):
    print("Sum is",a+b)
elif(op=="-"):
    print("Difference is",a-b)
elif(op=="*"):
    print("Product is",a*b)
elif(op=="/"):
    print("Ouotient is",a//b)
elif(op=="%"):
    print("Remainder is",a%b)
elif(op=="^"):
    print("power is",a**b)
else:
    print("It is not an Operator")


# In[ ]:




