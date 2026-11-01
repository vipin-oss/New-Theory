"""Independent manufactured algebra diagnostics, not a PDE or theorem proof."""
import unittest
import numpy as np
from scipy.linalg import expm
import sympy as sp
from experiments import matrices

class Integrated(unittest.TestCase):
    def test_mass_inverse_nonconstant(self):
        x=np.linspace(0,1,199)
        theta=2+np.sin(2*np.pi*x); c,d=.7,2.4
        f=np.cos(3*np.pi*x)+.7
        A=c+d*theta
        meanh=np.mean(f/A)/np.mean(c/A)
        h=(f+d*theta*meanh)/A
        np.testing.assert_allclose(c*h+d*theta*(h-np.mean(h)),f,atol=2e-15)
        weighted=np.mean((c*h+d*theta*(h-np.mean(h)))*h/theta)
        self.assertGreater(weighted,0)

    def test_characteristic_and_asymptotic_symbolic(self):
        x,d,t=sp.symbols('x d t', positive=True)
        delta=d*t-d**2*t**3+2*d**3*t**5
        residual=sp.expand(delta*(1/t+delta)-d)
        self.assertEqual(sp.series(residual,t,0,6).removeO(),0)
        M,S,gamma,mu,A,z=sp.symbols('M S gamma mu A z')
        mat=sp.Matrix([[-A,S/M],[gamma,-mu]])
        self.assertEqual(sp.expand((z*sp.eye(2)-mat).det()-(z+A)*(z+mu)+gamma*S/M),0)

    def test_modal_adjoint_duality(self):
        A,S,M,gamma,mu=4.3,.6,1.7,.8,.4
        mat=np.array([[-A,S/M],[gamma,-mu]])
        initial=np.array([.4,-.2]); terminal_dual=np.array([-.3,.9])
        t=.7
        self.assertAlmostEqual((expm(mat*t)@initial)@terminal_dual,
                               initial@(expm(mat.T*t)@terminal_dual))

    def test_terminal_moment_against_direct_exponential(self):
        mat=np.array([[-3.2,.4],[.7,-.6]])
        lam=np.linalg.eigvalsh(np.array([[-3.2,np.sqrt(.28)],[np.sqrt(.28),-.6]]))
        minus,plus=lam; C=2.1; t=.3
        actual=expm(mat*t)@np.array([C,0.])
        predicted=C/(plus-minus)*np.array([(plus+.6)*np.exp(plus*t)+(-minus-.6)*np.exp(minus*t),
                                            .7*(np.exp(plus*t)-np.exp(minus*t))])
        np.testing.assert_allclose(actual,predicted,rtol=1e-14,atol=1e-14)

    def test_energy_and_entropy_algebra(self):
        c,kappa,b,k,lam,a,theta,theta0,eps,w,eps_t,tx,txx=sp.symbols(
            'c kappa b k lam a theta theta0 eps w eps_t tx txx', nonzero=True)
        theta_t=(kappa*txx-b*theta*eps_t+k*lam*w**2)/c
        entropy_rate=c*theta_t/theta+b*eps_t
        flux_derivative=kappa*(txx/theta-tx**2/theta**2)
        production=kappa*tx**2/theta**2+k*lam*w**2/theta
        self.assertEqual(sp.simplify(entropy_rate-flux_derivative-production),0)
        e_rate=c*theta_t+a*eps*eps_t+k*w*(eps_t-lam*w)+b*theta0*eps_t
        stress=a*eps+k*w-b*(theta-theta0)
        self.assertEqual(sp.simplify(e_rate-kappa*txx-stress*eps_t),0)

    def test_mixed_nonlinear_variation(self):
        h,j=sp.symbols('h j')
        y1,y2,z1,z2,w1,w2,d,b,k,lam=sp.symbols('y1 y2 z1 z2 w1 w2 d b k lam')
        y=h*y1+j*y2; z=h*z1+j*z2; w=h*w1+j*w2
        source=-d*y*z-b*y*z+k*lam*w*w
        mixed=sp.diff(source,h,j).subs({h:0,j:0})
        expected=-(d+b)*(y1*z2+y2*z1)+2*k*lam*w1*w2
        self.assertEqual(sp.expand(mixed-expected),0)

    def test_joint_adjoint_branch_residue_invertibility(self):
        # Independent symbolic calculation: both branch residues force eta=h=0.
        delta,b,gamma=sp.symbols('delta b gamma', positive=True)
        residue=sp.Matrix([[delta,gamma],[b,-gamma]])
        self.assertEqual(sp.factor(residue.det()),-gamma*(delta+b))

    def test_one_sign_first_mode_kernel_strictly_positive(self):
        # Positive branch weights independently checked at two coupling signs.
        for gamma, S in ((.8,.35),(-.8,-.35)):
            A,mu,M=4.2,.7,2.
            d=gamma*S/M
            root=np.sqrt((A-mu)**2+4*d)
            plus=-(A+mu-root)/2
            minus=-(A+mu+root)/2
            t=np.linspace(0,1,101)
            kernel=(plus+mu)*np.exp(plus*t)+(-minus-mu)*np.exp(minus*t)
            self.assertTrue(np.all(kernel>0))

    def test_synthetic_basis_modes_distinct(self):
        a,b=matrices(4,'endpoint',count=10,quadrature=150)
        x,y=matrices(4,'flat',count=10,quadrature=150)
        self.assertEqual(a.shape,(4,10)); self.assertGreater(np.linalg.norm(a-x),1e-4)
        self.assertTrue(np.isfinite(b).all() and np.isfinite(y).all())

if __name__ == '__main__': unittest.main()
