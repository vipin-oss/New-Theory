import unittest
import numpy as np
from scipy.linalg import expm
import pilot as p

class LocalMGTTests(unittest.TestCase):
    def test_no_defect_is_periodic_product(self):
        w=1.49; n=3
        expected=[v for _ in range(2*n) for v in (p.A,p.B)]+[p.A]
        self.assertEqual(p.layers(n,1.),expected)
        Pcell=expm(p.matrix(w,.5,.1,p.B)*p.B[2])@expm(p.matrix(w,.5,.1,p.A)*p.A[2])
        P=expm(p.matrix(w,.5,.1,p.A)*p.A[2])@np.linalg.matrix_power(Pcell,2*n)
        np.testing.assert_allclose(p.transfer(w,.5,.1,p.layers(n,1.)),P,rtol=1e-9,atol=1e-7)
        self.assertAlmostEqual(p.solve(w,.5,.1,p.layers(n,1)),p.solve(w,.5,.1,p.layers(n,1+1e-7)),places=6)

    def test_elastic_limit_independent_two_by_two(self):
        for w in (1.1,1.4,np.pi/2,1.7,2.0):
            for d in (1.,2.):
                stack=p.layers(4,d)
                self.assertAlmostEqual(p.solve(w,.5,0,stack),p.elastic(w,stack),places=10)

    def test_power_and_positive_absorption(self):
        for tau in (.1,.5,1.):
            for w in (1.4,1.576,1.75):
                b=p.balance(w,tau,.1,p.layers(4))
                self.assertLess(abs(b['residual']),1e-9)
                self.assertGreaterEqual(b['absorption'],-1e-12)
                self.assertLess(b['terminal_q'],1e-9)

    def test_resonance_gap_and_spatial_confinement(self):
        peak=p.peak(4,.5,.1)
        self.assertGreater(abs(p.bloch(peak['omega'])),1.)
        xs,us=p.profile(peak['omega'],.5,.1,p.layers(4)); mid=us[np.argmin(abs(xs-13))]
        self.assertGreater(mid,3*max(us[0],us[-1]))
        self.assertGreater(peak['fwhm'],0)

if __name__=='__main__': unittest.main(verbosity=2)
