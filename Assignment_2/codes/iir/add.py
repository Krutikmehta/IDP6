
#This fuctions adds two polynomials defined by vectors x and y 
#z = add(x,y)

import numpy as np
def add(x,y):
    m = len(x)
    n = len(y)
    print(m-n)
    if m==n:
        z = x+y
    elif m>n:
        z = np.concatenate((np.zeros(m-n),y)) + x
    else:
        z = np.concatenate((np.zeros(n-m),x)) + y
                   
    return z
