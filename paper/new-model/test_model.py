import unittest
import numpy as np
import sympy as sp
from model import matrix,metric,solution,energy

# Dimensionless manufactured verification values, not physical materials.
P=dict(rho=2.,C=3.,beta=.4,T0=1.5,c=2.2,kappa=.3,h=.7,kr=.8,tau=.6,ell=.4,eta=.35)

class ModelTests(unittest.TestCase):
    def test_symbolic_determinant_and_limits(self):
        s,k,r,C,A,b,T,c,K,h,kr,t=sp.symbols('s k rho C A beta T c K h kr tau',real=True,nonzero=True)
        j=sp.I
        L=sp.Matrix([[s,-1,0,0,0],[C*k**2*A/r,s,j*k*b/r,0,0],
          [0,j*k*T*b/c,s+K*k**2/c,h*k**2/c,j*k/c],
          [0,0,-1,s,0],[0,0,j*k*kr/t,0,s+1/t]])
        p=(r*s**2+C*k**2*A)*((c*s**2+K*k**2*s+h*k**2)*(1+t*s)+kr*k**2*s)+b**2*T*k**2*s**2*(1+t*s)
        self.assertEqual(sp.simplify(L.det()*r*c*t-p),0)
        # Eliminated constitutive identity and exact first-order DPL identification.
        q,theta,alpha=sp.symbols('q theta alpha')
        rflux=q+h*alpha+K*theta
        constit=sp.expand((1+t*s)*rflux+kr*theta).subs(s*alpha,theta)
        expected=(1+t*s)*q+h*alpha+(K+kr+t*h)*theta+t*K*s*theta
        self.assertEqual(sp.simplify(constit-expected),0)
        self.assertEqual(sp.expand(expected.subs({h:0,K:0})-((1+t*s)*q+kr*theta)),0)
        self.assertEqual(sp.expand(expected.subs({t:0})-(q+h*alpha+(K+kr)*theta)),0)
        # Thermal factor at beta=0: reduced GN III, GN II, Fourier, LS.
        B=(c*s**2+K*k**2*s+h*k**2)*(1+t*s)+kr*k**2*s
        self.assertEqual(sp.expand(B.subs(t,0)-(c*s**2+(K+kr)*k**2*s+h*k**2)),0)
        self.assertEqual(sp.expand(B.subs({t:0,K:0,kr:0})-(c*s**2+h*k**2)),0)
        self.assertEqual(sp.expand(B.subs({t:0,h:0})-s*(c*s+(K+kr)*k**2)),0)
        self.assertEqual(sp.expand(B.subs({h:0,K:0})-s*(t*c*s**2+c*s+kr*k**2)),0)
    def test_energy_identity(self):
        for k in (1.,2.5,9.):
            A=matrix(k,**P); H=metric(k,**P)
            rhs=np.diag([0,0,-2*P['kappa']*k*k/P['T0'],0,-2/(P['kr']*P['T0'])])
            np.testing.assert_allclose(A.conj().T@H+H@A,rhs,atol=2e-13,rtol=2e-13)
            y=np.array([.2+.1j,-.3,.5-.2j,.1,.4j]); y1=solution(k,y,0.7,**P)
            self.assertLessEqual(energy(k,y1,**P),energy(k,y,**P)+1e-12)
    def test_fourier_conduction_limit(self):
        # Exact Fourier scalar mode, with coupling disabled only as a manufactured benchmark.
        p=P|dict(beta=0.,h=0.,kr=0.,kappa=.7)
        # kr=0 makes the internal-variable metric singular; temperature evolution remains valid.
        theta0=1.3; t=.4; k=2.; y=solution(k,[0,0,theta0,0,0],t,**p)
        np.testing.assert_allclose(y[2],theta0*np.exp(-p['kappa']*k*k*t/p['c']),rtol=1e-12,atol=1e-12)
    def test_gn_two_thermal_wave(self):
        # h>0, kr=kappa=0, beta=0: alpha'' + h*k²/c alpha=0.
        p=P|dict(beta=0.,kappa=0.,kr=0.)
        k=1.7; t=.8; theta0=.9
        y=solution(k,[0,0,theta0,0,0],t,**p)
        expected=theta0*np.cos(np.sqrt(p['h']/p['c'])*k*t)
        np.testing.assert_allclose(y[2],expected,rtol=1e-12,atol=1e-12)
    def test_cattaneo_and_eringen_modes(self):
        p=P|dict(beta=0.,kappa=0.,h=0.)
        k=1.3; t=.45; theta0=.8
        roots=np.roots([p['tau']*p['c'],p['c'],p['kr']*k*k])
        # Initial r=0 gives theta'(0)=0.
        a=-theta0*roots[1]/(roots[0]-roots[1]); b=theta0-a
        expected=a*np.exp(roots[0]*t)+b*np.exp(roots[1]*t)
        y=solution(k,[0,0,theta0,0,0],t,**p)
        np.testing.assert_allclose(y[2],expected,rtol=1e-12,atol=1e-12)
        a_k=p['eta']+(1-p['eta'])/(1+(p['ell']*k)**2)
        omega=k*np.sqrt(p['C']*a_k/p['rho'])
        y=solution(k,[1,0,0,0,0],t,**p)
        np.testing.assert_allclose(y[0],np.cos(omega*t),rtol=1e-12,atol=1e-12)
    def test_periodic_series_energy_tail(self):
        # Exact Fourier energy of alpha=0, u=0, v=0, theta=cos(x), r=0.
        y=solution(1,[0,0,1,0,0],.5,**P)
        self.assertTrue(np.isfinite(y).all())
        self.assertLessEqual(energy(1,y,**P),energy(1,[0,0,1,0,0],**P)+1e-12)

if __name__=='__main__': unittest.main(verbosity=2)
