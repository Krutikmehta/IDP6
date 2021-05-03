from cheb import cheb
from lp_stable_cheb import lp_stable_cheb
import numpy as np
import matplotlib.pyplot as plt

## Design param of low pass chebychev 
eps = 0.4
N = 4

### Calculating polynomial approximation using lp_stable_cheb
p,G = lp_stable_cheb(0.4, N=4)

### Savity check for p : obtained using chebychev poly: cheb.py
p1 = eps**2*np.convolve(cheb(N),cheb(N)) + np.concatenate((np.zeros(2*N),np.array([1])))

## Comparing both methods by plotting 


OMEGA = np.arange(0,2.01,0.01)
H_stable = np.abs(G/np.polyval(p,1j*OMEGA))
H_cheb = np.abs(np.sqrt(1/np.polyval(p1,1j*OMEGA)))

plt.plot(OMEGA,H_stable,'o', label = 'Design')
plt.plot(OMEGA,H_cheb,label = 'Specification')
plt.grid()
plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,LP}(j\Omega)|$')
plt.legend()
plt.title('Design and Specifications for $\epsilon$  = 0.4')
plt.savefig('../../figs/iir/spec.eps')
plt.savefig('../../figs/iir/spec.pdf')
plt.show()