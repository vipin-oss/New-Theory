"""Finite algebraic checks only; do not validate PDE results."""
import math
import unittest


class NextCycleChecks(unittest.TestCase):
    def test_scalar_k_functional_minimum(self):
        for lam in (1.0, 3.0, 100.0, 8192.0):
            for j in (0, 4, 10):
                t = 2.0**(-j) * lam
                c = 1.25
                b = c/(1+t)
                objective = (c-b)**2+t*b*b
                self.assertAlmostEqual(objective, c*c*t/(1+t))
                self.assertLessEqual(objective, c*c*t)
                self.assertLessEqual(objective, c*c)

    def test_log_dyadic_weight(self):
        for lam in (1, 2, 8, 1024, 2**30):
            total = sum((2.0**(-j)*lam)/(1+2.0**(-j)*lam) for j in range(100))
            expected = 1+math.log2(lam)
            self.assertGreaterEqual(total, .4*expected)
            self.assertLessEqual(total, 2*expected)

    def test_regularized_projection_formula(self):
        # Diagonal O with an exact kernel; this does not model the actual O.
        for singular in (0.0, 0.1, 1.0, 3.0):
            for alpha in (.01, .1, 1):
                control = singular/(singular*singular+alpha)
                residual = 1-singular*control
                self.assertAlmostEqual(residual, alpha/(singular*singular+alpha))
                self.assertLessEqual(abs(control), 1/(2*math.sqrt(alpha))+1e-12)


if __name__ == '__main__':
    unittest.main()
