"""Algebra-only checks; no result here certifies an infinite-dimensional PDE."""
import math
import unittest


class Cycle5Algebra(unittest.TestCase):
    def test_corrector_cancels_oscillatory_order(self):
        # Smooth even f=1+t+(x-1/2)^2 on I=(0,1), both time and x vary.
        x = 0.31
        for n in (1, 2, 5, 13):
            q = 2*math.pi*n
            fx, fxx, fx0 = 2*(x-.5), 2., -1.
            # The correction also has zero spatial trace at both ends.
            self.assertAlmostEqual(fx0 * math.cos(0.) - fx0, 0.)
            self.assertAlmostEqual(math.cos(q) + fx0, 0.)
            Hxx = -2*q*fxx*math.sin(q*x)-q*q*fx*math.cos(q*x)
            # From A and C, divide out common c_L e^(-mu t).
            trial_osc = -2*fx*math.cos(q*x)/q
            corrector_laplacian = -2*Hxx/(q**3)
            self.assertAlmostEqual(trial_osc+corrector_laplacian,
                                   4*fxx*math.sin(q*x)/q**2, places=12)

    def test_restart_bare_memory_exponential(self):
        for mu, t0, t in ((.7, .1, .8), (1.3, .02, .03), (.01, 2., 9.)):
            self.assertAlmostEqual(math.exp(-mu*(t-t0))*math.exp(-mu*t0),
                                   math.exp(-mu*t), places=14)

    def test_quadratic_minimizer_of_dyadic_cost(self):
        for j in range(1, 10):
            lam, c = 7.3, 1.8
            w = 2**(-j)*lam
            f = c/(1+w)
            objective = (c-f)**2+w*f*f
            self.assertAlmostEqual(objective, c*c*w/(1+w), places=14)
            self.assertGreaterEqual((c-(f+.01))**2+w*(f+.01)**2, objective)


if __name__ == '__main__':
    unittest.main()
