"""Finite-dimensional algebra diagnostics, not evidence about the physical PDE."""
import unittest
import numpy as np


class TemporalGraphAlgebra(unittest.TestCase):
    def test_nonlocal_quotient_includes_mean_and_cross_term(self):
        rng = np.random.default_rng(930)
        n, h = 9, .13
        q = np.eye(n) - np.ones((n, n)) / n
        theta, theta_next, v, v_next = (rng.normal(size=n) for _ in range(4))
        dz = (theta_next - theta) / h
        dv = (v_next - v) / h
        lhs = (theta_next * (q @ v_next) - theta * (q @ v)) / h
        rhs = theta_next * (q @ dv) + dz * (q @ v)
        np.testing.assert_allclose(lhs, rhs, rtol=1e-13, atol=1e-13)
        self.assertGreater(np.linalg.norm(dz * (q @ v)), .1)

    def test_small_perturbation_mass_quadratic_bound(self):
        rng = np.random.default_rng(120)
        n, c, d, theta0 = 15, 2., .7, 3.
        q = np.eye(n) - np.ones((n, n)) / n
        y = rng.uniform(-.3, .3, n)
        mass = c*np.eye(n) + d*np.diag(theta0+y) @ q
        for _ in range(40):
            u = rng.normal(size=n)
            actual = u @ mass @ u
            lower = (c - d*np.max(np.abs(y))) * (u @ u)
            self.assertGreaterEqual(actual + 1e-12, lower)
        self.assertFalse(np.allclose(mass, mass.T))

    def test_tikhonov_limit_is_kernel_projection_not_zero(self):
        o = np.array([[1., 0., 0.], [0., .2, 0.]])
        e = np.array([1., 1., 1.]) / np.sqrt(3)
        kernel = np.array([0., 0., e[2]])
        previous = float('inf')
        for alpha in (1e-2, 1e-4, 1e-6, 1e-8):
            f = np.linalg.solve(o @ o.T + alpha*np.eye(2), o @ e)
            error = o.T @ f - e
            identity = -alpha*np.linalg.solve(o.T @ o + alpha*np.eye(3), e)
            np.testing.assert_allclose(error, identity, atol=1e-12)
            gap = np.linalg.norm(error + kernel)
            self.assertLess(gap, previous)
            previous = gap
        self.assertLess(previous, 1e-6)
        self.assertAlmostEqual(np.linalg.norm(kernel), 1/np.sqrt(3))

    def test_dyadic_rate_from_mollification_cost(self):
        for j in range(1, 20):
            tau = 2**(-j/4)
            # Square the A-error tau^(1/2)+tau and H3 cost tau^-1.
            total = (tau**.5 + tau)**2 + 2**(-j) * tau**-2
            bound = 4*(2**(-j/4) + 2**(-j/2))
            self.assertLessEqual(total, bound)


if __name__ == '__main__':
    unittest.main()
