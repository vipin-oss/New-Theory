"""High-precision structural checks; not a proof of infinite-dimensional existence."""
import unittest
import mpmath as mp

class Structure(unittest.TestCase):
    def setUp(self): mp.mp.dps=60
    def test_entire_tail_borel_identity(self):
        d=mp.mpf('0.14'); T=mp.mpf(1); N=48
        # Manufactured v(s)=1-s has v(T)=0. q(t)=t T v(t).
        cp=[mp.mpf(0)]+[d**p/(mp.factorial(p-1)*mp.factorial(p)*(p+1)*(p+2)) for p in range(1,N)]
        def deriv(j):
            return sum(cp[p]*mp.factorial(p)/mp.factorial(p-j)*T**(p-j) for p in range(max(j,1),N))
        for b in [mp.mpf(5),mp.mpf(12),mp.mpf(60)]:
            tail=sum(cp[p]*mp.gammainc(p+1,b*T,mp.inf)/b**(p+1) for p in range(1,N))
            expansion=mp.exp(-b*T)*sum(deriv(j)/b**(j+1) for j in range(N))
            self.assertLess(abs(tail-expansion),mp.mpf('1e-52'))
    def test_fredholm_algebra_not_neumann(self):
        # Exact finite algebra tests E S=I, E(I+SR)=E+R.
        E=mp.matrix([[1,0,2,0],[0,1,0,3]])
        S=mp.matrix([[1,0],[0,1],[0,0],[0,0]])
        R=mp.matrix([[mp.mpf('.2'),1,2,3],[4,mp.mpf('.3'),6,7]])
        self.assertEqual(E*S,mp.eye(2))
        self.assertEqual(E*(mp.eye(4)+S*R),E+R)
    def test_endpoint_combination(self):
        x=mp.matrix([1,2,3]);y=mp.matrix([3,1,0]);L=lambda z:z[0]+2*z[2]
        k=L(y)*x-L(x)*y
        self.assertEqual(L(k),0)
        self.assertGreater(mp.norm(k),0)
if __name__=='__main__':unittest.main()
