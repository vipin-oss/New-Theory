"""Synthetic truncated moment experiments; no physical constants or theorem inference."""
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander


def matrices(n, mode, count=48, quadrature=500):
    # Synthetic physically consistent M,B,S,mu,gamma values: B=-S*gamma/mu.
    M, mu, gamma, S, kappa, L = 2., .7, .8, .35, 1., 1.
    B = -S*gamma/mu
    nodes, weights = leggauss(quadrature)
    t = (nodes+1)/2
    weights = weights/2
    V = legvander(2*t-1,count-1)
    if mode == 'endpoint':
        V *= t[:,None]  # f(0)=0, generally nonzero terminal derivative
    elif mode == 'flat':
        V *= np.exp(-.0025/t**2)[:,None] # flat at terminal but no gap
    elif mode == 'gap':
        V *= np.where(t > .2, np.exp(-.0025/np.maximum(t-.2,1e-100)**2), 0)[:,None]
    else:
        raise ValueError(mode)
    q=2*np.pi*np.arange(1,n+1)/L
    A=(kappa*q*q-B)/M
    d=gamma*S/M
    root=np.sqrt((A-mu)**2+4*d)
    # Stable calculation of slow root avoids subtracting nearly equal numbers.
    delta=2*d/(root+(A-mu))
    fast=-A-delta
    diff=A-mu+2*delta
    C=2*kappa*np.sqrt(2/L)*q/M
    slow=np.exp(np.outer(-mu+delta,t))
    fastv=np.exp(np.outer(fast,t))
    heat=C[:,None]/diff[:,None]*(delta[:,None]*slow+(-fast-mu)[:,None]*fastv)
    memory=C[:,None]*gamma/diff[:,None]*(slow-fastv)
    return (heat*weights)@V,(memory*weights)@V


def run():
    print('synthetic moment experiment: numpy float64; 500 point Gauss-Legendre, 48 basis functions')
    print('N mode sigma_min heat/memory-target control_norm residual')
    for n in (3,6,10,15,20):
        for mode in ('endpoint','flat','gap'):
            heat, mem=matrices(n,mode)
            mat=np.vstack((heat,mem[0]))
            rhs=np.r_[np.zeros(n),1.]
            coeff, _, rank, singular=np.linalg.lstsq(mat,rhs,rcond=1e-13)
            print(n,mode, f'{singular[-1]:.3e}', rank,
                  f'{np.linalg.norm(coeff):.3e}',f'{np.linalg.norm(mat@coeff-rhs):.3e}')
if __name__ == '__main__': run()
