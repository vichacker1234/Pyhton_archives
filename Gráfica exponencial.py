#!/usr/bin/env python
# coding: utf-8

# In[1]:


v=[2,4,6,8]
v


# In[3]:


import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(0,10,100)
b=np.exp(-a)
plt.plot(a,b)
plt.show


# In[4]:


import matplotlib.pyplot as plt
from numpy.random import rand
a=rand(100)
b=rand(100)
plt.scatter(a,b)
plt.show


# In[7]:


import numpy as np
import  mathplot
r=np.array([(9,8,7),(6,5,4)])#Extrae los valores
print(r)
print(r[0:1])


# In[9]:


import numpy as np
r=np.array([(9,8,7),(6,5,4)])#operaciones
m=np.array([(1,2,3),(4,5,6)])
print(np.sqrt(r))#raiz cuadrada
print(r+m)
print(r-m)
print(r*m)
print(r/m)


# In[ ]:




