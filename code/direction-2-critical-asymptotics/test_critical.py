import unittest
import numpy as np
from manufactured_high_frequency import coefficient,exact_flux,leading,numerical_flux,norm,fields,table,DELTA,T
class CriticalNumerics(unittest.TestCase):
    def test_boundary_derivatives_refine(self):
        t=np.linspace(DELTA,T,401)
        for kind in ('smooth','sobolev'):
            truth=exact_flux(8,t,kind)
            for order in (2,4):
                e1=norm(t,numerical_flux(8,t,kind,256,order)-truth)
                e2=norm(t,numerical_flux(8,t,kind,512,order)-truth)
                self.assertGreater(e1/e2,3 if order==2 else 10)
    def test_trends_and_finite_forcing(self):
        for kind in ('smooth','sobolev'):
            a=table(kind,[4,8,16,32],801)
            self.assertGreater(a[0][1],a[-1][1]); self.assertGreater(a[0][2],a[-1][2])
            x=np.array([.1,.25,.75,.9]); y,p,f,g=fields(3,.2,x,kind)
            self.assertTrue(np.isfinite(np.r_[y,p,f,g]).all())
    def test_time_quadrature(self):
        a=table('smooth',[8],41)[0][1];b=table('smooth',[8],161)[0][1];c=table('smooth',[8],641)[0][1]
        self.assertGreater(abs(a-c),abs(b-c)*10)
if __name__=='__main__':unittest.main()
