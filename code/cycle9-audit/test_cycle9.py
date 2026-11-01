"""Synthetic algebraic checks only; no PDE solution, parameters or experiments."""
import unittest
import numpy as np


class PreparationAlgebra(unittest.TestCase):
    def test_history_ode_and_equilibrium_slice(self):
        # Dimensionless examples exercise identities, not material calibration.
        for r in (0.1, 0.4, 0.8):
            lam = 1.7
            s = np.linspace(-2.0, 0.0, 31)
            a1, a2 = 6 - 2*r, 3*r - 6
            f = a1*np.exp(lam*s) + a2*np.exp(2*lam*s)
            z = 0.5*a1*np.exp(lam*s) + a2*np.exp(2*lam*s)/3
            zp = lam*(0.5*a1*np.exp(lam*s) + 2*a2*np.exp(2*lam*s)/3)
            np.testing.assert_allclose(zp, lam*(f-z), atol=2e-15)
            self.assertAlmostEqual(f[-1], r)
            self.assertAlmostEqual(z[-1], 1.0)
            fp0 = lam*(a1+2*a2)
            cp0 = fp0-r*lam*(r-1)  # D=1, k=r
            self.assertAlmostEqual(cp0, -lam*(2-r)*(3-r))
            self.assertLess(cp0, 0)
            self.assertLess(-r*lam*(1-r)**2, 0)

    def test_reflection_reconstruction_and_parity(self):
        x = np.linspace(0, 1, 2001)
        h_odd = np.sin(2*np.pi*x)
        memory_even = 1 + np.cos(2*np.pi*x)
        theta_even = np.cos(2*np.pi*x)
        self.assertLess(np.max(np.abs(h_odd + h_odd[::-1])), 1e-14)
        self.assertLess(np.max(np.abs(memory_even - memory_even[::-1])), 1e-14)
        r, beta, m = 0.3, 0.4, 0.2
        mean = np.trapezoid(memory_even, x)
        strain = m + r*(memory_even-mean) + beta*(theta_even-np.trapezoid(theta_even, x))
        self.assertLess(np.max(np.abs(strain-strain[::-1])), 1e-14)
        self.assertAlmostEqual(np.trapezoid(strain, x), m)
        self.assertAlmostEqual(np.trapezoid(memory_even*h_odd, x), 0.0, places=14)
        self.assertAlmostEqual(np.trapezoid((memory_even-h_odd)**2, x),
                               np.trapezoid(memory_even**2+h_odd**2, x), places=13)

    def test_entropy_identity_algebra(self):
        c, k, lam, kap, b = 2.0, 0.7, 1.3, 1.1, -0.5
        theta, theta_x, theta_xx, eps_t, w = 1.8, 0.2, -0.3, 0.4, -0.2
        theta_t = (kap*theta_xx-b*theta*eps_t+k*lam*w*w)/c
        eta_t = c*theta_t/theta+b*eps_t
        entropy_flux_derivative = kap*(theta_xx/theta-theta_x**2/theta**2)
        production = kap*theta_x**2/theta**2+k*lam*w*w/theta
        self.assertAlmostEqual(eta_t-entropy_flux_derivative, production)
        self.assertGreaterEqual(production, 0.0)


if __name__ == '__main__':
    unittest.main()
