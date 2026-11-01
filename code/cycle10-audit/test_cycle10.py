"""Manufactured modal algebra checks, not PDE/physical evidence."""
import unittest
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad

class Cycle10(unittest.TestCase):
    def test_two_branch_response_and_terminal_coefficients(self):
        # Synthetic positive constants only, not experimental material values.
        M, kappa, B, S, mu, gamma, L = 2.0, 1.1, -0.7, 0.9, 0.6, 0.8, 1.3
        cL = np.sqrt(2 / L)
        for n in (1, 2, 5):
            q = 2 * np.pi * n / L
            A = (kappa*q*q-B)/M
            d0 = gamma*S/M
            delta = np.sqrt((A-mu)**2+4*d0)
            plus = -(A+mu-delta)/2
            minus = -(A+mu+delta)/2
            C = 2*kappa*cL*q/M
            self.assertLess(minus, -mu)
            self.assertGreater(plus, -mu)
            self.assertAlmostEqual((plus+mu)*(-minus-mu), d0, places=10)
            matrix = np.array([[-A, S/M], [gamma, -mu]])
            for t in (0.1, 0.8):
                response = expm(matrix*t) @ np.array([C, 0])
                y = C*((plus+mu)*np.exp(plus*t)+(-minus-mu)*np.exp(minus*t))/delta
                p = C*gamma*(np.exp(plus*t)-np.exp(minus*t))/delta
                np.testing.assert_allclose(response, [y,p], rtol=1e-11, atol=1e-13)

    def test_odd_dirichlet_boundary_factor(self):
        L = 1.7
        for n in range(1, 6):
            q = 2*np.pi*n/L
            derivative_left = np.sqrt(2/L)*q
            derivative_right = np.sqrt(2/L)*q*np.cos(q*L)
            self.assertAlmostEqual(derivative_left+derivative_right, 2*derivative_left)

    def test_lifting_fourier_coefficient(self):
        L = 1.2
        for n in range(1, 5):
            q=2*np.pi*n/L
            value=quad(lambda x:(1-2*x/L)*np.sqrt(2/L)*np.sin(q*x),0,L)[0]
            self.assertAlmostEqual(value, 2*np.sqrt(2/L)/q)

if __name__ == '__main__':
    unittest.main()
