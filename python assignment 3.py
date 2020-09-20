#!/usr/bin/env python
# coding: utf-8

# In[13]:


"""
question 1.1 
"""
from functools import reduce
r= [1,2,3,4,5,6,7,8,9,10,11,12]
myreduce = reduce(lambda a,b: a+b,r)
print(myreduce)


# In[6]:


"""
question1.2 filter 
"""
def even (n):
    return  n%2==0
      
r= [1,2,3,4,5,6,7,8,9,10,11,12]
even=list(filter(even,r))
print(even)

        
    


# In[8]:


"""
question1.2 
"""
r = [1,2,3,4,5,6,7,8,9,10,11,12]
even=list(filter(lambda n: n%2==0,r))
print(even)


# In[15]:


"""

question 1.2


"""
letters = list('xyz')
pattern = []
for i in range(len(letters)):    
       for j in range(1,5):     
           pattern.append(letters[i]*j)
        
print(pattern)


# In[ ]:




