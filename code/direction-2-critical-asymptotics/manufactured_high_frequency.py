"""Artificial forced high-frequency PDE–ODE verification; not physical data."""
import argparse
from pathlib import Path
import numpy as np

L=1.; T=1.; DELTA=.1; MU=.7; GAMMA=.4; KAPPA=1.; A0=1.

def coefficient(x, kind):
    x=np.asarray(x)
    if kind=='smooth':
        return 1+.2*np.cos(2*np.pi*x), -.4*np.pi*np.sin(2*np.pi*x), -.8*np.pi**2*np.cos(2*np.pi*x)
    if kind=='sobolev':
        # H^2, but not H^{2.1}; value at the isolated singular point is irrelevant a.e.
        z=x-.5; power=np.abs(z); dd=np.zeros_like(power)
        np.power(power,-.4,out=dd,where=power>0)
        return 1+.2*power**1.6, .32*np.sign(z)*power**.6, .192*dd
    raise ValueError(kind)

def fields(n,t,x,kind):
    q=2*np.pi*n; t=np.asarray(t);x=np.asarray(x);s,sx,sxx=coefficient(x,kind)
    phi=np.sqrt(2)*np.sin(q*x); phix=np.sqrt(2)*q*np.cos(q*x)
    a=np.exp(-MU*t);r=1-np.exp(-q*q*t); rt=q*q*np.exp(-q*q*t)
    v=s*phi/q**2+phi/q**3
    y=a*r*v;yt=a*(rt-MU*r)*v
    yxx=a*r*((sxx*phi+2*sx*phix-q*q*s*phi)/q**2-phi/q)
    p=a*phi;pt=-MU*p
    # M=1, B=0, S=s, kappa=1: deliberately forced manufactured equations.
    F=yt-KAPPA*yxx-s*p;G=pt+MU*p-GAMMA*y
    return y,p,F,G

def exact_flux(n,t,kind):
    q=2*np.pi*n;s0=float(coefficient(np.array([0.]),kind)[0][0]);t=np.asarray(t)
    return 2*np.sqrt(2)*np.exp(-MU*t)*(1-np.exp(-q*q*t))*(s0/q+1/q**2)

def leading(n,t,kind):
    s0=float(coefficient(np.array([0.]),kind)[0][0]);q=2*np.pi*n
    return 2*np.sqrt(2)*np.exp(-MU*np.asarray(t))*s0/q

def norm(t,v): return np.sqrt(np.trapezoid(v*v,t))

def numerical_flux(n,t,kind,cells,order):
    dx=L/cells; xs=dx*np.arange(0,5); y=fields(n,np.asarray(t)[:,None],xs[None,:],kind)[0]
    if order==2: derivative=(-3*y[:,0]+4*y[:,1]-y[:,2])/(2*dx)
    elif order==4: derivative=(-25*y[:,0]+48*y[:,1]-36*y[:,2]+16*y[:,3]-3*y[:,4])/(12*dx)
    else: raise ValueError('order must be 2 or 4')
    return 2*A0*KAPPA*derivative

def table(kind,ns,nt=401):
    t=np.linspace(DELTA,T,nt);out=[]
    for n in ns:
        q=2*np.pi*n;r=exact_flux(n,t,kind)-leading(n,t,kind)
        z=exact_flux(n,t,kind)-(n+1)/n*exact_flux(n+1,t,kind)
        out.append((n,q**1.5*norm(t,r),q**1.5*norm(t,z)))
    return out

def main():
    p=argparse.ArgumentParser();p.add_argument('--plot',default='code/direction-2-critical-asymptotics/manufactured-asymptotics.png');args=p.parse_args()
    ns=[1,2,4,8,16,32];print('ARTIFICIAL FORCED manufactured solutions (not an active base)')
    for kind in ('smooth','sobolev'):
        print('\n',kind,'n, q^1.5 ||rho||, q^1.5 ||T z||')
        for n,r,z in table(kind,ns): print(n,f'{r:.9e}',f'{z:.9e}')
        print('boundary-derivative error, n=8, time points=1001; 2nd and 4th order')
        t=np.linspace(DELTA,T,1001); exact=exact_flux(8,t,kind)
        for cells in (128,256,512,1024):
            print(cells,*(f'{norm(t,numerical_flux(8,t,kind,cells,o)-exact):.8e}' for o in (2,4)))
    print('observation quadrature convergence: n=8, smooth; time samples / scaled remainder')
    for nt in (11,21,41,81,161,321):print(nt,f'{table("smooth",[8],nt)[0][1]:.9e}')
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(7,4.5))
    for kind in ('smooth','sobolev'):
        rows=table(kind,ns,1001); ax.loglog(ns,[r[1] for r in rows],'-o',label=f'{kind}: scaled remainder')
        ax.loglog(ns,[r[2] for r in rows],'--s',label=f'{kind}: scaled neighbor response')
    ax.set(xlabel='mode n',ylabel='q_n^(3/2) delayed L2 norm',title='Exact manufactured forced PDE–ODE (not physical)')
    ax.legend(fontsize=8);ax.grid(True,which='both',alpha=.3);fig.tight_layout();Path(args.plot).parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.plot,dpi=160)
    print('wrote',args.plot)
if __name__=='__main__':main()
