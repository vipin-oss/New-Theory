"""Local MGT layered-rod pilot; e^{-i omega t}. Dimensionless illustrative units."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar, brentq
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
# Each layer is (C, rho, thickness), common c, K, Kstar, beta, T0.
A=(1.,1.,1.); B=(4.,1.,2.); C_HEAT=1.; K=.2; KSTAR=.1; T0=1.

def layers(n=4, defect=2.):
    return [v for _ in range(n) for v in (A,B)] + [(1.,1.,defect)] + [v for _ in range(n) for v in (B,A)]

def matrix(w, tau, beta, layer):
    c,rho,_=layer; s=-1j*w
    h=(K+KSTAR/s)/(1+tau*s)
    return np.array([[0,1/c,beta/c,0], [rho*s*s,0,0,0], [0,0,0,-1/h], [0,-s*beta*T0/c,-s*(C_HEAT+beta*beta*T0/c),0]],complex)

def transfer(w,tau,beta,items):
    P=np.eye(4,dtype=complex)
    for lay in items: P=expm(matrix(w,tau,beta,lay)*lay[2])@P
    return P

def solve(w,tau,beta,items,states=False):
    # identical elastic A leads; incident displacement amplitude 1, outgoing only.
    # Multiple shooting avoids multiplying exponentially growing thermal modes.
    from scipy.linalg import solve as linear_solve
    m=len(items); mat=np.zeros((4*(m+1),4*(m+1)),complex); rhs=np.zeros(4*(m+1),complex)
    z=w
    mat[0,0]=1j*z; mat[0,1]=1; rhs[0]=2j*z
    mat[1,3]=1
    for j,lay in enumerate(items):
        row=2+4*j; mat[row:row+4,4*j:4*j+4]=-expm(matrix(w,tau,beta,lay)*lay[2]); mat[row:row+4,4*j+4:4*j+8]=np.eye(4)
    mat[-2,4*m]=-1j*z; mat[-2,4*m+1]=1; mat[-1,4*m+3]=1
    ys=linear_solve(mat,rhs,assume_a='gen').reshape(m+1,4)
    r=ys[0,0]-1; t=ys[-1,0]
    return (abs(t)**2,abs(r)**2,ys) if states else abs(t)**2

def elastic_matrix(w, lay):
    c,rho,d=lay; k=w*np.sqrt(rho/c); z=c*k
    return np.array([[np.cos(k*d),np.sin(k*d)/z],[-z*np.sin(k*d),np.cos(k*d)]],complex)

def elastic(w,items):
    P=np.eye(2,dtype=complex)
    for lay in items: P=elastic_matrix(w,lay)@P
    z=w; inc=np.array([1,1j*z]); ref=np.array([1,-1j*z]); out=np.array([1,1j*z]); r,t=np.linalg.solve(np.column_stack((P@ref,-out)),-P@inc)
    return abs(t)**2

def bloch(w): return np.trace(elastic_matrix(w,B)@elastic_matrix(w,A)).real/2

def peak(n,tau,beta):
    items=layers(n); res=minimize_scalar(lambda x:-solve(x,tau,beta,items),bounds=(1.51,1.63),method='bounded', options={'xatol':1e-12})
    w=res.x; height=-res.fun
    half=lambda x: solve(x,tau,beta,items)-height/2
    # Require half-height crossings on both sides before using a FWHM.
    left=brentq(half,1.35,w,xtol=1e-12); right=brentq(half,w,1.8,xtol=1e-12)
    return dict(n=n,tau=tau,beta=beta,omega=w,T=height,fwhm=right-left,left=left,right=right)

def balance(w,tau,beta,items):
    T,R,ys=solve(w,tau,beta,items,True); total=0.; s=-1j*w
    h=(K+KSTAR/s)/(1+tau*s)
    for j,lay in enumerate(items):
        Q=matrix(w,tau,beta,lay); start=ys[j]
        def integrand(x):
            q=(expm(Q*x)@start)[3]
            return .5*np.real(1/h)*abs(q)**2/T0
        total+=quad(integrand,0,lay[2],epsabs=1e-10,epsrel=1e-9)[0]
    incoming=.5*w*w # lead C=rho=1
    return dict(T=T,R=R,absorption=total/incoming,residual=1-T-R-total/incoming,terminal_q=abs(ys[-1,3]))

def profile(w,tau,beta,items):
    _,_,ys=solve(w,tau,beta,items,True); xs=[]; us=[]; x0=0
    for j,lay in enumerate(items):
        y=ys[j]; Q=matrix(w,tau,beta,lay)
        for x in np.linspace(0,lay[2],25,endpoint=False):
            xs.append(x0+x); us.append(abs((expm(Q*x)@y)[0]))
        y=expm(Q*lay[2])@y; x0+=lay[2]
    xs.append(x0); us.append(abs(ys[-1,0]))
    return np.array(xs),np.array(us)

def main():
    band=[brentq(lambda x:bloch(x)+1,.8,1.55),brentq(lambda x:bloch(x)+1,1.58,2.3)]
    cases=[peak(4,t,b) for b in (0,.1,.25) for t in (.1,.5,1.)]
    conv=[peak(n,.5,.1) for n in (2,3,4,5,6)]
    checks=[balance(p['omega'],p['tau'],p['beta'],layers(p['n'])) for p in cases]
    rng=np.linspace(.9,2.25,400)
    fig,ax=plt.subplots(figsize=(8,4.5)); ax.axvspan(*band,color='0.9',label='elastic infinite-cell stop band')
    for defect,label in ((1.,'periodic (no defect)'),(2.,'central A thickness doubled')):
        ax.plot(rng,[solve(w,.5,.1,layers(4,defect)) for w in rng],label=label)
    pk=peak(4,.5,.1); ax.plot(pk['omega'],pk['T'],'o',color='tab:orange',markersize=5,label='optimized defect peak')
    ax.set(xlabel='angular frequency ω (dimensionless)',ylabel='mechanical power transmission',ylim=(0,1.05)); ax.legend(); fig.tight_layout(); fig.savefig(HERE/'transmission.png',dpi=160); plt.close(fig)
    fig,ax=plt.subplots(figsize=(8,4.5))
    for beta in (0,.1,.25):
        for tau in (.1,1.):
            ax.plot(rng,[solve(w,tau,beta,layers(4)) for w in rng],label=f'β={beta}, τ={tau}',alpha=.8)
    ax.set(xlim=(1.3,1.85),xlabel='angular frequency ω',ylabel='mechanical power transmission'); ax.legend(ncol=2,fontsize=8); fig.tight_layout(); fig.savefig(HERE/'sensitivity.png',dpi=160); plt.close(fig)
    fine=np.linspace(1.55,1.63,650); fig,ax=plt.subplots(figsize=(8,4.5))
    for tau in (.1,.5,1.):
        ax.plot(fine,[solve(w,tau,.1,layers(4)) for w in fine],label=f'τ={tau}')
    ax.set(xlabel='angular frequency ω',ylabel='mechanical power transmission',title='Thermal relaxation sensitivity, β=0.1'); ax.legend(); fig.tight_layout(); fig.savefig(HERE/'zoom.png',dpi=160); plt.close(fig)
    p=peak(4,.5,.1); xs,us=profile(p['omega'],.5,.1,layers(4)); fig,ax=plt.subplots(figsize=(8,3.5)); ax.plot(xs,us); ax.axvspan(12,14,color='orange',alpha=.25,label='defect layer'); ax.set(xlabel='position',ylabel='|displacement|',title='Resonant response (N=4 per side)'); ax.legend(); fig.tight_layout(); fig.savefig(HERE/'localization.png',dpi=160); plt.close(fig)
    result=dict(band=band,cases=cases,convergence=conv,balance=checks)
    (HERE/'data.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
