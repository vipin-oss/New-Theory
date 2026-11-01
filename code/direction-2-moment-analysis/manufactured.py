"""Manufactured forced example; arbitrary dimensionless software-verification data."""
import numpy as np
from scipy.integrate import solve_ivp
from finite_difference import solve_fd

L=1.; kap=.6; gamma=.4; mu=.7; A0=1.; T=1.; delta=.1

def exact(t,x):
    x=np.asarray(x); e=np.exp(-t); s1=np.sin(2*np.pi*x);s2=np.sin(4*np.pi*x)
    y=e*(t*s1+.15*t*t*s2)
    yt=e*((1-t)*s1+.15*(2*t-t*t)*s2)
    yxx=-e*((2*np.pi)**2*t*s1+.15*(4*np.pi)**2*t*t*s2)
    p=e*((1+t)*s1+.2*s2)
    pt=e*(-t*s1-.2*s2)
    return y,yt,yxx,p,pt

def coeff(x): return 1+.2*np.cos(2*np.pi*x)
def sources(t,x):
    y,yt,yxx,p,pt=exact(t,x)
    return yt-kap*yxx-.3*y-coeff(x)*p,pt+mu*p-gamma*y

def data(cells):
    x=np.linspace(0,L,cells+1);t=np.linspace(0,T,11);shape=(len(t),len(x))
    return dict(x=x,t=t,M=np.ones(shape),B=np.full(shape,.3),S=np.broadcast_to(coeff(x),shape).copy(),
                L=L,kappa=kap,gamma=gamma,mu=mu,A0=A0,delta=delta)

def spectral_reference(modes=8):
    # Independently solve the forced spectral semidiscretization by adaptive BDF.
    from moments import trapezoid_weights
    x=np.linspace(0,L,513);w=trapezoid_weights(x);q=2*np.pi*np.arange(1,modes+1)/L
    phi=np.sqrt(2/L)*np.sin(np.outer(x,q)); Sm=phi.T@((w*coeff(x))[:,None]*phi)
    initp=phi.T@(w*exact(0,x)[3]); initial=np.r_[np.zeros(modes),initp]
    def rhs(t,z):
        f,g=sources(t,x);y=z[:modes];p=z[modes:]
        return np.r_[-kap*q*q*y+.3*y+Sm@p+phi.T@(w*f),-mu*p+gamma*y+phi.T@(w*g)]
    out=solve_ivp(rhs,(0,T),initial,method='BDF',rtol=1e-11,atol=1e-13,dense_output=True)
    if not out.success: raise RuntimeError(out.message)
    return lambda t: out.sol(t),q,phi

def errors(cells,steps,ref=None):
    d=data(cells); x=d['x']; h=exact(0,x)[3]; r=solve_fd(d,h,steps,sources)
    ye,_,_,pe,_=exact(T,x[1:-1]); dx=x[1]-x[0]
    yerr=np.sqrt(dx*np.sum((r['Y'][-1,:,0]-ye)**2)); perr=np.sqrt(dx*np.sum((r['P'][-1,:,0]-pe)**2))
    tt=r['flux_t']; exactflux=2*A0*kap*np.exp(-tt)*(tt*2*np.pi+.15*tt**2*4*np.pi)
    ferr=np.sqrt(np.trapezoid((r['flux'][:,0]-exactflux)**2,tt))
    if ref:
        sol,q,_=ref
        # Evaluate spectral state directly on this grid.
        ph=np.sqrt(2/L)*np.sin(np.outer(x[1:-1],q)); z=sol(T)
        agreement=np.sqrt(dx*np.sum((r['Y'][-1,:,0]-ph@z[:len(q)])**2))
    else: agreement=float('nan')
    return yerr,perr,ferr,agreement

def main():
    ref=spectral_reference(); print('ARTIFICIAL manufactured problem; no physical data')
    print('spatial refinement, steps=2048')
    for n in (24,48,96,192):
        print(n,2048,*[f'{v:.8e}' for v in errors(n,2048,ref)])
    print('temporal refinement, cells=192; errors vs exact (spatial error floor)')
    for st in (16,32,64,128,256):
        print(192,st,*[f'{v:.8e}' for v in errors(192,st,ref)])
    # temporal difference to a fixed-space reference isolates time discretization
    print('temporal self-convergence, cells=96: L2 final state difference from steps=2048')
    d=data(96);h=exact(0,d['x'])[3];baseline=solve_fd(d,h,2048,sources)
    for st in (16,32,64,128,256):
        a=solve_fd(d,h,st,sources); dy=a['Y'][-1,:,0]-baseline['Y'][-1,:,0];dp=a['P'][-1,:,0]-baseline['P'][-1,:,0]
        print(st,f'{np.sqrt((dy@dy+dp@dp)/96):.8e}')
if __name__=='__main__':main()
