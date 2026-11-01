import unittest
import numpy as np
from scipy.linalg import expm
from moments import abstract_columns, distance_and_control, vector_v, trapezoid_weights, galerkin

class MomentTests(unittest.TestCase):
    def test_injective_distance(self):
        K,a=abstract_columns(12,100,False)
        for n in (0,1,5):
            d,c,rank=distance_and_control(K,a,n)
            self.assertAlmostEqual(d,(n+1)**-2,places=11)
            self.assertAlmostEqual(c,(n+1)**2,places=9)
            self.assertEqual(rank,12)
    def test_infinite_kernel_truncation(self):
        m=2000
        K,a=abstract_columns(m,m,True)
        v=vector_v(m)
        # Truncation of an exact infinite kernel; high accuracy is expected,
        # not exact finite-N singularity because the infinite tail is omitted.
        self.assertLess(np.linalg.norm(K@v), 1e-6)
        self.assertLess(abs(np.dot(1/np.arange(1,m+1),v)),1e-6)
    def test_artificial_constant_coefficient_galerkin(self):
        # Pure software test, deliberately artificial; NOT a physical active base.
        x=np.linspace(0,2*np.pi,129); t=np.linspace(0,1,11)
        one=np.ones((len(t),len(x)))
        data={'x':x,'t':t,'L':2*np.pi,'M':one,'B':0*one,'S':one,
              'gamma':1.,'mu':1.,'kappa':2.,'A0':1.}
        flux=galerkin(data,1,rtol=1e-10,atol=1e-12)[:,0]
        A=np.array([[-2.,1.],[1.,-1.]])
        expected=np.array([4*np.sqrt(1/np.pi)*(expm(tt*A)@np.array([0.,1.]))[0] for tt in t])
        np.testing.assert_allclose(flux,expected,rtol=2e-8,atol=2e-10)
    def test_quadrature(self):
        x=np.array([0.,.1,.6,1.]); w=trapezoid_weights(x)
        self.assertAlmostEqual(w.sum(),1.)
        self.assertAlmostEqual(w@x,.5)
    def test_schur_inverse_agrees(self):
        K,a=abstract_columns(8,100,True)
        n=0; dist,control,_=distance_and_control(K,a,n)
        Kaug=np.column_stack((K,a)); G=Kaug.T@Kaug
        self.assertTrue(np.isclose(control**2,np.linalg.solve(G,np.eye(9)[:,n])[n],rtol=1e-8))

if __name__=='__main__': unittest.main()
