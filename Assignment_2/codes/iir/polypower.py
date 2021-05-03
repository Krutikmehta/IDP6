#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
def polypower(v,N):
    y = 1
    if N>0:
        for i in range(1,N+1):
            y = np.convolve(y,v)
    return y


# In[ ]:





# In[ ]:





# In[ ]:




