"""Deterministic pointwise shape-chain-rule and finite-mode algebra checks.

These tests check formulas, not physical admissibility, PDE well-posedness,
uniqueness, or novelty. Requires only Python 3's standard library.
"""
import random
import unittest


def surface(e, j, js, gu, hv, guu, hvv, alpha, beta):
    # Local model J=1+e*j, J_s=e*js, exact at the test point.
    J, Js = 1 + e * j, e * js
    first = alpha * gu * hv / J
    second_u = guu / J**2 - Js * gu / J**3
    second_v = hvv / J**2 - Js * hv / J**3
    return first + beta * second_u * second_v * J


class Audit(unittest.TestCase):
    def test_surface_variation(self):
        rng = random.Random(401)
        for _ in range(100):
            j, js, gu, hv, guu, hvv = [rng.uniform(-2, 2) for _ in range(6)]
            alpha, beta = 0.7, 1.2
            exact = (-alpha*j*gu*hv - 3*beta*j*guu*hvv
                     - beta*js*(gu*hvv+guu*hv))
            step = 1e-5
            numeric = (surface(step,j,js,gu,hv,guu,hvv,alpha,beta)
                       - surface(-step,j,js,gu,hv,guu,hvv,alpha,beta))/(2*step)
            self.assertAlmostEqual(numeric, exact, delta=2e-7)

    def test_endpoint_log_polynomial_specialization(self):
        # At L=-d_j/gamma all other summands vanish, for distinct d_j.
        ds, bs, qs, cs, gamma = [1.,3.,6.], [2.,-1.,4.], [3.,2.,-2.], [1.,2.,5.], 0.8
        for j in range(3):
            z = -ds[j]/gamma
            terms = []
            for n in range(3):
                prod = 1.
                for m in range(3):
                    if m != n:
                        prod *= ds[m] + gamma*z
                terms.append(cs[n]*(bs[n]-qs[n]*z)*prod)
            want = cs[j]*(bs[j]+qs[j]*ds[j]/gamma)
            for m in range(3):
                if m != j:
                    want *= ds[m]-ds[j]
            self.assertAlmostEqual(sum(terms), want, places=10)

if __name__ == '__main__':
    unittest.main()
