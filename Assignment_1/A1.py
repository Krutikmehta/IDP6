#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x = np.array([1,2,3,4,2,1])
h = np.array([1,-0.5,1.25,-0.625,0.3125,-0.15625])


# In[3]:


w = np.exp(-1j*2*np.pi/3)
W = np.exp(-1j*2*np.pi/6)


# In[4]:


B1 = np.matrix([[w**0,w**0,w**0,0,0,0],[w**0,w**1,w**2,0,0,0],[w**0,w**2,w**4,0,0,0],[0,0,0,w**0,w**0,w**0],[0,0,0,w**0,w**1,w**2],[0,0,0,w**0,w**2,w**4]])
B2 = np.matrix([[1,0,0,W**0,0,0],[0,1,0,0,W**1,0],[0,0,1,0,0,W**2],[1,0,0,W**3,0,0],[0,1,0,0,W**4,0],[0,0,1,0,0,W**5]])
P = np.matrix([[1,0,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,1,0],[0,1,0,0,0,0],[0,0,0,1,0,0],[0,0,0,0,0,1]])


# In[5]:


W = np.matmul(np.matmul(B2,B1),P)
X = np.matmul(W,x)
H = np.matmul(W,h)
Y = np.multiply(H,X)
y = (1/6)*np.matmul(W.H,Y.T)


# In[7]:


plt.figure(figsize=(15,15))
plt.subplot(3,3,4)
plt.stem(np.abs(np.array(X).ravel()),use_line_collection=True)
plt.title('$|X(k)|$')
plt.grid()

plt.subplot(3,3,7)
plt.stem(np.angle(np.array(X).ravel()),use_line_collection=True)
plt.title(r'$\angle{X(k)}$')
plt.grid()

plt.subplot(3,3,5)
plt.stem(np.abs(np.array(H).ravel()),use_line_collection=True)
plt.title('$|H(k)|$')
plt.grid()

plt.subplot(3,3,8)
plt.stem(np.angle(np.array(H).ravel()),use_line_collection=True)
plt.title(r'$\angle{H(k)}$')
plt.grid()

plt.subplot(3,3,6)
plt.stem(np.abs(np.array(Y).ravel()),use_line_collection=True)
plt.title('$|Y(k)|$')
plt.grid()

plt.subplot(3,3,9)
plt.stem(np.angle(np.array(Y).ravel()),use_line_collection=True)
plt.title(r'$\angle{Y(k)}$')
plt.grid()

plt.subplot(3,3,1)
plt.stem(x,use_line_collection=True)
plt.title(r'x(n)')
plt.grid()
plt.subplot(3,3,3)
plt.stem(np.array(y).ravel(),use_line_collection=True)
plt.title(r'y(n)')
plt.grid()
plt.subplot(3,3,2)
plt.stem(h,use_line_collection=True)
plt.title(r'h(n)')
plt.grid()
plt.savefig('A1_1.pdf')
plt.savefig('A1_1.eps')

plt.subplots_adjust(hspace=0.3,wspace=0.3)
plt.show()


# In[ ]:




