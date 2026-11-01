"""Abstract diagnostics for finite-bin inequalities; not a PDE or experiment test."""
import unittest
import numpy as np


def integral_exp(rate, left, right):
    return np.exp(rate * left) * np.expm1(rate * (right - left)) / rate


def reference_matrices(bins):
    # Two synthetic distinct exponential combinations, not material parameters.
    rates = np.array([[-0.7, -2.0], [-1.1, -3.4]])
    signs = np.array([1.0, -1.0])
    a, b = 0.2, 1.3
    gram = np.zeros((2, 2))
    dgram = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for m in range(2):
                    rate = rates[i, k] + rates[j, m]
                    factor = signs[k] * signs[m]
                    gram[i, j] += factor * integral_exp(rate, a, b)
                    dgram[i, j] += factor * rates[i, k] * rates[j, m] * integral_exp(rate, a, b)
    edges = np.linspace(a, b, bins + 1)
    lengths = np.diff(edges)
    matrix = np.empty((bins, 2))
    for j in range(bins):
        for i in range(2):
            matrix[j, i] = sum(signs[k] * integral_exp(rates[i, k], edges[j], edges[j+1])
                               for k in range(2)) / np.sqrt(lengths[j])
    return gram, dgram, matrix, max(lengths)


class FiniteBinDiagnostics(unittest.TestCase):
    def test_reference_projection_error_bound(self):
        g, dg, b, delta = reference_matrices(48)
        remainder = (g - b.T @ b)
        self.assertGreater(np.linalg.eigvalsh(g)[0], 0)
        self.assertLessEqual(np.linalg.eigvalsh(remainder)[-1],
                             (delta / np.pi)**2 * np.trace(dg) + 1e-13)
        sigma = np.sqrt(np.linalg.eigvalsh(g)[0])
        self.assertGreaterEqual(np.linalg.svd(b, compute_uv=False)[-1] + 1e-12,
                                sigma - delta * np.sqrt(np.trace(dg)) / np.pi)

    def test_perturbation_and_two_point_remainder(self):
        g, dg, b, delta = reference_matrices(160)
        sigma = np.sqrt(np.linalg.eigvalsh(g)[0])
        mesh = delta * np.sqrt(np.trace(dg)) / np.pi
        e, r = sigma / 10, sigma / 8
        perturbation = np.zeros_like(b)
        perturbation[0, 0] = e
        rng = np.random.default_rng(81)
        for _ in range(40):
            v = rng.normal(size=2)
            remainder = np.zeros(len(b))
            remainder[1] = r * np.linalg.norm(v)
            observed = (b + perturbation) @ v + remainder
            self.assertGreaterEqual(np.linalg.norm(observed) + 1e-12,
                                    (sigma - mesh - e - r) * np.linalg.norm(v))
        self.assertGreater(sigma - mesh - e - r, 0)

    def test_least_squares_error_factor(self):
        matrix = np.diag([2.0, 0.5])
        h = np.array([0.1, -0.2])
        noise = np.array([0.02, -0.03])
        recovered = np.linalg.solve(matrix, matrix @ h + noise)
        alpha = np.linalg.svd(matrix, compute_uv=False)[-1]
        eta = np.linalg.norm(noise)
        self.assertLessEqual(np.linalg.norm(recovered - h), eta / alpha + 1e-14)
        self.assertLessEqual(np.linalg.norm(recovered - h), 2 * eta / alpha + 1e-14)


if __name__ == '__main__':
    unittest.main()
