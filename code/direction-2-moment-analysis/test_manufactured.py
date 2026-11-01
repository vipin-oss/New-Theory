import unittest
import numpy as np
from manufactured import errors, data, sources, exact, spectral_reference
from finite_difference import solve_fd
from moments import galerkin
from moment_diagnostics import diagnostics

class ManufacturedTests(unittest.TestCase):
    def test_fd_spatial_and_boundary_convergence(self):
        # Artificial coefficients and forcing: software verification only.
        a=errors(24,512); b=errors(48,512)
        for j in (0,1,2): self.assertGreater(a[j]/b[j],3.7)
    def test_temporal_convergence(self):
        d=data(48);h=exact(0,d['x'])[3]
        baseline=solve_fd(d,h,512,sources)
        def err(steps):
            out=solve_fd(d,h,steps,sources)
            return np.linalg.norm(out['Y'][-1]-baseline['Y'][-1])+np.linalg.norm(out['P'][-1]-baseline['P'][-1])
        self.assertGreater(err(16)/err(32),3.8)
    def test_independent_spectral(self):
        sol,q,_=spectral_reference();x=np.linspace(0,1,129);y,_,_,p,_=exact(1,x)
        phi=np.sqrt(2)*np.sin(np.outer(x,q));z=sol(1)
        np.testing.assert_allclose(phi@z[:len(q)],y,atol=1e-10)
        np.testing.assert_allclose(phi@z[len(q):],p,atol=1e-10)
        self.assertLess(errors(48,256,(sol,q,phi))[3],5e-4)
    def test_original_galerkin_vs_independent_fd(self):
        # Same artificial coefficients, unforced PDE-ODE and sine input.
        d=data(48);d['t']=np.linspace(0,1,101)
        for key in ('M','B','S'): d[key]=np.repeat(d[key][0:1],101,axis=0)
        h=np.sqrt(2)*np.sin(2*np.pi*d['x']);fd=solve_fd(d,h,512)
        g=galerkin(d,4,rtol=1e-9,atol=1e-11)[:,0]
        difference=fd['flux'][:,0]-np.interp(fd['flux_t'],d['t'],g)
        self.assertLess(np.sqrt(np.trapezoid(difference**2,fd['flux_t'])),.003)
    def test_alias_grid_rejected(self):
        with self.assertRaises(ValueError): galerkin(data(16),8)
    def test_moment_control(self):
        from moments import abstract_columns
        K,a=abstract_columns(16,64,False);out=diagnostics(K,a,8,1)
        self.assertAlmostEqual(out['distance'],1.)
        self.assertLess(out['constraint_error'],1e-10)
        self.assertLess(out['leakage'],1e-10)
if __name__=='__main__': unittest.main()
