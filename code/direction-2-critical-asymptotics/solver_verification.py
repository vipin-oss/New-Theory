"""Independent FD PDE–ODE solve against forced high-frequency analytic fields."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'direction-2-moment-analysis'))
import numpy as np
from finite_difference import solve_fd
from manufactured_high_frequency import coefficient,fields,exact_flux,norm,DELTA,T

def run(kind,n,cells,steps,with_state=False):
    x=np.linspace(0,1,cells+1);t=np.linspace(0,1,21);s=coefficient(x,kind)[0]
    d=dict(x=x,t=t,M=np.ones((len(t),len(x))),B=np.zeros((len(t),len(x))),
           S=np.tile(s,(len(t),1)),L=1.,kappa=1.,mu=.7,gamma=.4,A0=1.,delta=DELTA)
    h=np.sqrt(2)*np.sin(2*np.pi*n*x)
    def source(tt,xx): return fields(n,tt,xx,kind)[2:]
    r=solve_fd(d,h,steps,source);ex=exact_flux(n,r['flux_t'],kind)
    ye,pe,_,_=fields(n,T,x[1:-1],kind)
    result=(norm(r['flux_t'],r['flux'][:,0]-ex),np.sqrt(np.mean((r['Y'][-1,:,0]-ye)**2)),np.sqrt(np.mean((r['P'][-1,:,0]-pe)**2)))
    return (result,r) if with_state else result
if __name__=='__main__':
    print('ARTIFICIAL forced problem; FD solver vs exact, n=4')
    for kind in ('smooth','sobolev'):
        for cells in (128,256,512):print(kind,cells,2048,*[f'{v:.8e}' for v in run(kind,4,cells,2048)])
        for steps in (256,512,1024,2048):print(kind,'time',256,steps,*[f'{v:.8e}' for v in run(kind,4,256,steps)])

    print('temporal self-convergence, cells=128, reference=4096 steps')
    for kind in ('smooth','sobolev'):
        _,ref=run(kind,4,128,4096,True)
        for steps in (128,256,512,1024):
            _,z=run(kind,4,128,steps,True)
            diff=z['flux'][:,0]-np.interp(z['flux_t'],ref['flux_t'],ref['flux'][:,0])
            state=np.sqrt(np.mean((z['Y'][-1]-ref['Y'][-1])**2+(z['P'][-1]-ref['P'][-1])**2))
            print(kind,steps,f'{norm(z["flux_t"],diff):.8e}',f'{state:.8e}')
