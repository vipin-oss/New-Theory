"""Finite-dimensional and high-precision cross-checks, not infinite-dimensional proof."""
import unittest
import mpmath as mp
import numpy as np
from scipy.special import roots_legendre
from study import H,D

class OperatorTests(unittest.TestCase):
    def test_kernel_positive(self):
        t,w=roots_legendre(80);t=(t+1)/2;w=w/2
        mat=D*np.sqrt(w*t)[:,None]*H(t,t)*np.sqrt(w*t)[None,:]
        self.assertGreater(np.linalg.eigvalsh(mat).min(),-1e-14)
    def test_infinite_tail_identity_at_60_digits(self):
        mp.mp.dps=60;d=mp.mpf('0.14');T=mp.mpf(1)
        b=mp.mpf(3);v=lambda s:s*(1-s)
        # Series integral uses incomplete gamma and polynomial moments, independent
        # of the exact Bessel/Laplace resummation used by the operator.
        terms=[]
        for j in range(35):
            moment=1/(mp.mpf(j+3)*(j+4))
            pref=d**(j+1)*moment/(mp.factorial(j)*mp.factorial(j+1)*b**(j+2))
            terms.append((pref*mp.gammainc(j+2,0,b*T),pref*mp.gammainc(j+2,b*T,mp.inf)))
        local=sum(v[0] for v in terms);tail=sum(v[1] for v in terms)
        full=mp.quad(lambda s:s*(s*(1-s))*d/b**2*mp.e**(d*s/b),[0,T])
        self.assertLess(abs(local+tail-full),mp.mpf('1e-48'))
        self.assertGreater(tail,0)
    def test_operator_normalization(self):
        t=np.array([.2,.6]);np.testing.assert_allclose(H(t,np.array([0]))[:,0],1)
if __name__=='__main__':unittest.main()
