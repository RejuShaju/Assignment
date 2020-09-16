#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Write a program which will find all such numbers which are divisible by 7 but are not amultiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
#in a comma-separated sequence on a single line.
#(Q1)
ul = int(2000)
ll = int(3200)
for i in range (ul,ll+1): 
    if (i% 7==0 and i% 5==0):
        print (i, end =",")


# In[14]:


#Write a Python program to accept the user's first and last name and then getting themprinted in the the reverse order with a space between first name and last name.
#(Q2)
first_name= str("Reju")
second_name= str("Shaju")
print (second_name+" "+first_name)


# In[18]:


#Write a Python program to find the volume of a sphere with diameter 12 cm.
#(Q3)
pi = 3.1415926535897931
r= 12
v= 4/3*pi* r**3
print(v)


# In[ ]:





# In[ ]:




