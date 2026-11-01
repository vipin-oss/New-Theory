"""Tests compare independent exact calculations; numerical evidence is not proof."""
import unittest
import mpmath as mp
import numpy as np
import sympy as sp
from scipy.special import roots_legendre
from study import basis,maps,spectral,M,MU,GAMMA,S,KAPPA,L,D
from verify_precision import coefficients,transform

class MomentTests(unittest.TestCase):
    def test_endpoint_and_gram_sine(self):
        t,w=roots_legendre(400); t=(t+1)/2;w=w/2
        V=basis(t,12,'oscillatory')
        np.testing.assert_allclose((V.T*w)@V,np.eye(12),rtol=1e-12,atol=1e-12)
        self.assertLess(np.max(np.abs(basis(np.array([0.,1.]),12,'oscillatory'))),2e-14)
    def test_modal_roots_and_boundary_factor(self):
        q,d,b=spectral(12); A=(KAPPA*q*q+GAMMA*S/MU)/M
        np.testing.assert_allclose(d*b,D,rtol=1e-14)
        np.testing.assert_allclose(b-d,A-MU,rtol=1e-14)
    def test_high_precision_transform_vs_quadrature(self):
        mp.mp.dps=50;z=mp.mpf('-2.75'); k=3
        v=mp.quad(lambda t:mp.sqrt(2)*mp.sin(mp.pi*k*t)*mp.exp(z*t),[0,1])
        self.assertLess(abs(v-transform(z,k)),mp.mpf('1e-45'))
    def test_terminal_map_independent_precision(self):
        mp.mp.dps=50
        y,p,_=maps(4,4,'oscillatory',800)
        for n in (1,4):
            q,d,b=coefficients(n); mu=mp.mpf(str(MU));gamma=mp.mpf(str(GAMMA));
            C=2*mp.mpf(str(KAPPA))*mp.sqrt(2/mp.mpf(str(L)))*q/mp.mpf(str(M))
            for k in (1,3):
                Fp=transform(-mu+d,k);Fm=transform(-mu-b,k)
                self.assertAlmostEqual(y[n-1,k-1],float(C*(d*Fp+b*Fm)/(d+b)),places=11)
                self.assertAlmostEqual(p[n-1,k-1],float(C*gamma*(Fp-Fm)/(d+b)),places=11)
    def test_positive_kernel_and_jet_correction(self):
        # Independent Nystrom diagnostic for the compact kernel construction.
        from scipy.special import iv
        t,w=roots_legendre(100); t=(t+1)/2;w=w/2
        x=D*np.outer(t,t)
        H=iv(1,2*np.sqrt(x))/np.sqrt(x)
        weights=w*t
        matrix=D*H*weights[None,:]
        h=np.exp(-1/np.maximum((t-.2)*(.8-t),1e-300))
        h=np.where((t>.2)&(t<.8),h,0.)
        v=np.linalg.solve(np.eye(len(t))+matrix,h)
        self.assertLess(np.linalg.norm(v+matrix@v-h),1e-13)
        f=np.exp(MU*t)*t*v
        g=-np.exp(MU*t)*t*(matrix@v)
        np.testing.assert_allclose(f-g,np.exp(MU*t)*t*h,atol=1e-14)
        sym=D*np.sqrt(weights)[:,None]*H*np.sqrt(weights)[None,:]
        self.assertGreater(np.linalg.eigvalsh(sym).min(),-1e-13)

    def test_memory_tail_normalization(self):
        q,d,m,k,c,g,fj=sp.symbols('q d m k c g fj', positive=True)
        for j in range(1,5):
            delta=d*m/(k*q**2)
            expr=(2*c*g/q)*(-fj*delta**(j-1)/d**j)
            expected=-2*c*g*fj/d*(m/k)**(j-1)*q**(-(2*j-1))
            self.assertEqual(sp.simplify(expr-expected),0)

    def test_jet_hierarchy_symbolic(self):
        u,mu,d,F0,F1=sp.symbols('u mu d F0 F1')
        J=-d*u**2/(1-mu*u)**2*(F0+d*u/(1-mu*u)*F1)
        self.assertEqual(sp.expand(sp.series(J,u,0,4).removeO()).coeff(u,2),-d*F0)
        self.assertEqual(sp.expand(sp.series(J,u,0,4).removeO()).coeff(u,3),-2*d*mu*F0-d*d*F1)
if __name__=='__main__':unittest.main()
