"""Finite-moment diagnostic. Synthetic parameters, no physical or infinite-mode claims."""
import argparse
import numpy as np
from scipy.special import roots_legendre
from numpy.polynomial.legendre import legvander

# Synthetic parameters satisfy the physical relation mu*B + gamma*S = 0.
M, MU, GAMMA, S, KAPPA, L, T = 2., .7, .8, .35, 1., 1., 1.
B=-GAMMA*S/MU
D=GAMMA*S/M


def basis(t, count, family):
    if family=='oscillatory':
        return np.sqrt(2.)*np.sin(np.pi*np.outer(t,np.arange(1,count+1)))
    v=legvander(2*t-1,count-1)*t[:,None]*(1-t[:,None])
    if family=='smooth-flat':
        v*=np.exp(-.0025/(t*(1-t)))[:,None]
    elif family!='polynomial':
        raise ValueError(family)
    return v


def spectral(n):
    q=2*np.pi*np.arange(1,n+1)/L
    A=(KAPPA*q*q-B)/M
    root=np.sqrt((A-MU)**2+4*D)
    delta=2*D/(root+(A-MU))
    b=A-MU+delta
    return q,delta,b


def maps(n, count, family, points):
    nodes,w=roots_legendre(points); t=(nodes+1)/2; w=w/2
    V=basis(t,count,family); q,delta,b=spectral(n)
    delta=delta[:,None]; b=b[:,None]; t=t[None,:]
    pref=(2*KAPPA*np.sqrt(2/L)*q/M)[:,None]/(delta+b)
    slow=np.exp((-MU+delta)*t); fast=np.exp((-MU-b)*t)
    y=pref*(delta*slow+b*fast)
    p=pref*GAMMA*(slow-fast)
    return (y*w)@V,(p*w)@V,(V.T*w)@V


def solve(n, family, count=None, points=600):
    count=count or 2*n+8
    Y,P,G=maps(n,count,family,points)
    # SVD whitening G = U diag(s) U.T; discard directions below numerical precision.
    g,U=np.linalg.eigh(G); keep=g>g[-1]*1e-13
    W=U[:,keep]/np.sqrt(g[keep]); A=np.vstack([Y,P[0]])@W
    target=np.r_[np.zeros(n),1.]
    z,_,rank,svals=np.linalg.lstsq(A,target,rcond=1e-12)
    c=W@z
    return c,rank,svals,G


def run():
    ap=argparse.ArgumentParser(); ap.add_argument('--modes',default='5,10,20,40,80'); ap.add_argument('--points',type=int,default=600)
    args=ap.parse_args()
    print('N,family,dim,rank,smax,smin,condition,gram_norm,endpoint_fprime,partial_memory_norm,train_resid,unseen_y,quad_diff')
    for n in map(int,args.modes.split(',')):
        for fam in ('polynomial','smooth-flat','oscillatory'):
            count=2*n+8
            c,rank,sv,G=solve(n,fam,count,args.points)
            y,p,_=maps(n+10,count,fam,args.points)
            y2,p2,_=maps(n+10,count,fam,args.points*2)
            residual=np.linalg.norm(np.r_[y[:n]@c,p[0]@c-1])
            unseen=np.linalg.norm(y[n:]@c)
            qdiff=np.linalg.norm(np.r_[(y2-y)@c,(p2[0]-p[0])@c])
            if fam=='oscillatory':
                jet=np.sqrt(2)*np.pi*np.dot(np.arange(1,count+1),c)
            elif fam=='polynomial':
                jet=np.dot((-1.)**np.arange(count),c)
            else: jet=0.0
            pmem=np.linalg.norm(p2@c)
            print(f'{n},{fam},{count},{rank},{sv[0]:.3e},{sv[-1]:.3e},{sv[0]/sv[-1]:.3e},{np.sqrt(max(c@G@c,0)):.3e},{jet:.3e},{pmem:.3e},{residual:.3e},{unseen:.3e},{qdiff:.3e}')
if __name__=='__main__': run()
