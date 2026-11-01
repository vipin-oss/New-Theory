"""Abstract/comparison diagnostics only, not physical data or a PDE proof."""
import unittest
import numpy as np


class Cycle6Diagnostics(unittest.TestCase):
    def test_reference_roots_and_accumulation(self):
        q = 2*np.pi*np.arange(1., 201.)
        mu, d = 1., .25
        a = (q*q + .5)/2
        gap = np.sqrt((a-mu)**2 + 4*d)
        fast = -(a+mu+gap)/2
        # Stable root formula avoids cancellation near -mu.
        slow = -mu + 2*d/(gap+a-mu)
        self.assertTrue(np.all(fast < -mu))
        self.assertTrue(np.all((-mu < slow) & (slow < 0)))
        self.assertTrue(np.all(np.diff(fast) < 0))
        self.assertTrue(np.all(np.diff(slow) < 0))
        np.testing.assert_allclose((slow+mu)*(slow+a), d, rtol=1e-8)
        self.assertLess(slow[-1]+mu, slow[0]+mu)

    def test_slow_taylor_remainder_bound(self):
        q = 2*np.pi*np.arange(15., 80.)
        a = (q*q+.5)/2
        gap = np.sqrt((a-1.)**2 + 1.)
        eps = .5/(gap+a-1.)
        t = .8
        for r in (1, 2, 3):
            # Compare series tail directly to avoid cancellation in exp minus Taylor.
            tail = np.zeros_like(eps)
            term = np.ones_like(eps)
            import math
            for k in range(1, r+10):
                term = term*(eps*t)/k
                if k >= r:
                    tail += term
            bound = np.exp(eps*t)*(eps*t)**r/math.factorial(r)
            self.assertTrue(np.all(tail <= bound*(1+1e-12)))
            self.assertTrue(np.all((q/gap)*tail <= (q/gap)*bound))

    def test_conjugated_heat_cross_term_identity(self):
        # Smooth fabricated functions test the integration-by-parts signs only.
        x = np.linspace(0, 1, 601); t = np.linspace(.1, .9, 501)
        X, T = np.meshgrid(x, t)
        k, s, eta, tc = 1.2, .8, .3, .5
        M = 1+.1*T+.1*np.cos(2*np.pi*X)
        Mt = .1; Mx = -.2*np.pi*np.sin(2*np.pi*X)
        B = .2*T+.1*np.cos(2*np.pi*X)
        Bx = -.2*np.pi*np.sin(2*np.pi*X)
        pt = -2*eta*(T-tc); ptt = -2*eta
        V = s*M*pt+k*s*s+B
        Vt = s*(Mt*pt+M*ptt)+.2
        Vx = s*Mx*pt+Bx
        v = np.sin(np.pi*X)*(1+T)
        vt = np.sin(np.pi*X)
        vx = np.pi*np.cos(np.pi*X)*(1+T)
        vxx = -np.pi**2*v
        A = -k*vxx-V*v; D = M*vt+2*k*s*vx
        integrate = lambda z: np.trapezoid(np.trapezoid(z,x,axis=1),t)
        left = 2*integrate(A*D)
        bulk = integrate(-k*Mt*vx**2+2*k*Mx*vx*vt+(Mt*V+M*Vt)*v**2+2*k*s*Vx*v**2)
        time_boundary = np.trapezoid((k*M*vx**2-M*V*v**2)[-1],x)-np.trapezoid((k*M*vx**2-M*V*v**2)[0],x)
        side = -2*k*k*s*np.trapezoid(vx[:,-1]**2-vx[:,0]**2,t)
        self.assertAlmostEqual(left, bulk+time_boundary+side, delta=4e-4)


if __name__ == '__main__':
    unittest.main()
