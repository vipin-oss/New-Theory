"""Dimensionless manufactured periodic-wave illustration; NOT experiment/data validation."""
import numpy as np
from model import solution, energy
P=dict(rho=2.,C=3.,beta=.4,T0=1.5,c=2.2,kappa=.3,h=.7,kr=.8,tau=.6,ell=.4,eta=.35)

def partial(n,t,x):
    ans=np.zeros_like(x,dtype=complex)
    for k in range(1,n+1):
        state=solution(k,[0,0,np.exp(-k),0,0],t,**P)
        ans+=state[2]*np.exp(1j*k*x)+state[2].conjugate()*np.exp(-1j*k*x)
    return ans.real

if __name__=='__main__':
    x=np.linspace(0,2*np.pi,513,endpoint=False); t=.5
    ref=partial(32,t,x)
    for n in (4,8,16,24):
        print(f'N={n:2d} max_sampled_error_vs_N32={np.max(np.abs(partial(n,t,x)-ref)):.12e}')
    before=energy(1,[0,0,1,0,0],**P)
    after=energy(1,solution(1,[0,0,1,0,0],t,**P),**P)
    print(f'k1_energy_initial={before:.12g} final={after:.12g}')
