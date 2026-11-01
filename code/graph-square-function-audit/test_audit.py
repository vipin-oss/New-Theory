"""Algebraic/abstract diagnostics only; no physical base or PDE validation."""
import math
import unittest


class AuditDiagnostics(unittest.TestCase):
    def test_reference_characteristic_and_memory(self):
        # Arbitrary positive parameters, not an experimental material set.
        for a, k, b, lam, c, theta, kap in [(2, 3, -0.7, 1.2, 4, 2, 0.8), (1, 2, 3, 0.4, 5, 0.6, 2)]:
            d = a + k
            r, alpha, gamma, mu = k/d, a/d, lam*b/d, lam*a/d
            m0 = c + b*b*theta/d
            b0, s0 = -b*r*gamma*theta, mu*b*r*theta
            self.assertAlmostEqual(mu*b0 + gamma*s0, 0.0, places=12)
            for n in (1, 3, 10):
                q = 2*math.pi*n
                an, d0 = (kap*q*q-b0)/m0, gamma*s0/m0
                discr = math.sqrt((an-mu)**2+4*d0)
                minus, plus = -(an+mu+discr)/2, -(an+mu-discr)/2
                self.assertLess(minus, -mu)
                self.assertGreater(plus, -mu)
                self.assertLess(plus, 0)
                self.assertAlmostEqual(an*mu-d0, mu*kap*q*q/m0, places=9)
                # Integral of positive reference feedback over the fixed delay.
                t = .01
                def convolution(root):
                    return (math.exp(root*t)-math.exp(-mu*t))/(root+mu)
                memory = math.exp(-mu*t) + d0/discr*(convolution(plus)-convolution(minus))
                self.assertGreaterEqual(memory + 1e-14, math.exp(-mu*t))

    def test_periodic_k_functional_lacunary_lower_bound(self):
        # For mode 2^k, min over a Fourier coefficient of
        # (2^k)^2|c-b|^2 + 2^-j (2^k)^6 |b|^2.
        for j in (8, 16, 32):
            cutoff = j//4 + 1
            for k in range(cutoff, cutoff+8):
                omega = 2**k
                amplitude = 1/(omega*k)
                A, B = omega**2, 2**(-j)*omega**6
                minimum = A*B/(A+B)*amplitude**2
                self.assertGreaterEqual(minimum+1e-15, .5/k**2)

    def test_rank_one_endpoint_has_kernel(self):
        q1, q2 = 2*math.pi, 4*math.pi
        # Coefficients h1=q1 and h2=-q2 give zero observation.
        self.assertEqual(q1/q1-q2/q2, 0)


if __name__ == '__main__':
    unittest.main()
