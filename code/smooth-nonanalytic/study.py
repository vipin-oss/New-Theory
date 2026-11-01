"""Nyström flat-correction diagnostics. Synthetic constants, not proof or measured data."""
import argparse
import numpy as np
from scipy.special import roots_legendre, iv
from numpy.polynomial.legendre import legvander
from scipy.linalg import solve, eigh

T=1.; MU=.7; M=2.; GAMMA=.8; S=.35; KAPPA=1.; L=1.
D=GAMMA*S/M; B=-GAMMA*S/MU

def H(t,s):
    x=D*np.outer(np.atleast_1d(t),np.atleast_1d(s))
    out=np.ones_like(x); m=x>0
    out[m]=iv(1,2*np.sqrt(x[m]))/np.sqrt(x[m])
    return out

def inputs(t,count,family):
    flat=np.exp(-.005/t)
    if family=='flat-polynomial':return flat[:,None]*(1-t[:,None])*legvander(2*t-1,count-1)
    if family=='flat-oscillatory':return flat[:,None]*np.sin(np.pi*np.outer(t,np.arange(1,count+1)))
    if family=='compact-bumps':
        centers=np.linspace(.12,.88,count); radius=max(.08,1.8/count)
        z=(t[:,None]-centers)/radius
        out=np.zeros_like(z); mask=np.abs(z)<1
        out[mask]=np.exp(-1/(1-z[mask]**2))
        return out
    raise ValueError(family)

def matrices(count,family,Q,nmax):
    z,w=roots_legendre(Q); t=(z+1)/2; w=w/2
    kval=inputs(t,count,family)
    # Nyström discretization of T in L2(t dt), solved simultaneously.
    mat=np.eye(Q)+D*H(t,t)*(w*t)[None,:]
    v=solve(mat,kval,assume_a='gen')
    # All chosen inputs vanish at T, hence v(T)=-(Tv)(T).
    vend=-(D*H([1.],t)*(w*t)[None,:])@v
    q=2*np.pi*np.arange(1,nmax+1)/L; A=(KAPPA*q*q-B)/M
    root=np.sqrt((A-MU)**2+4*D); delta=2*D/(root+(A-MU));b=A-MU+delta
    C=2*KAPPA*np.sqrt(2/L)*q/M
    fast=np.exp(-np.outer(b,t));slow=np.exp(np.outer(delta,t))
    fn=(fast*(w*t))@v;sn=(slow*(w*t))@v
    residual=fn+(D/b**2)[:,None]*sn
    memory=(C*GAMMA/(delta+b))[:,None]*(sn-fn)
    f=np.exp(MU*t)[:,None]*t[:,None]*v
    G=(f.T*w)@f
    return t,w,v,vend,residual,memory,G

def experiment(n,family,Q=240):
    count=2*n+8
    t,w,v,end,R,P,G=matrices(count,family,Q,n+10)
    eigen,U=eigh(G); keep=eigen>eigen[-1]*1e-13
    W=U[:,keep]/np.sqrt(eigen[keep]); A=np.vstack([R[:n],end,P[0]])@W
    target=np.r_[np.zeros(n+1),1.]
    c0,_,rank,sig=np.linalg.lstsq(A,target,rcond=1e-12);c=W@c0
    _,_,_,end2,R2,P2,_=matrices(count,family,2*Q,n+10)
    gram_cond=eigen[-1]/eigen[keep][0]
    jet=-D*np.dot((w*t)@v,c)
    return count,rank,sig[0],sig[-1],sig[0]/sig[-1],gram_cond,np.sqrt(max(c@G@c,0)),jet,np.linalg.norm(P@c),np.linalg.norm(R[:n]@c),abs((end@c)[0]),np.linalg.norm(R[n:]@c),abs(P[0]@c-1),np.linalg.norm((R2-R)@c),np.linalg.norm((P2-P)@c)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--modes',default='5,10,20,40');parser.add_argument('--quadrature',type=int,default=240);a=parser.parse_args()
    print('N,family,nbasis,rank,smax,smin,sv_condition,gram_condition,L2,fprime0,partial_memory_norm,fit,endpoint,withheld,memory_target,quad_R,quad_P')
    for n in map(int,a.modes.split(',')):
        for fam in ('flat-polynomial','flat-oscillatory','compact-bumps'):
            row=experiment(n,fam,a.quadrature)
            print(','.join([str(n),fam,str(row[0]),str(row[1])]+[f'{x:.5e}' for x in row[2:]]))
if __name__=='__main__':main()
