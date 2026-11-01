#!/usr/bin/env python3
"""Abstract moment tests and optional Galerkin solver for supplied active coefficients.

No physical values or active base are supplied; see README for data contract.
"""
import argparse
import json
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import RegularGridInterpolator
from scipy.linalg import lstsq
from scipy.special import zeta


def vector_v(m):
    # Infinite vector: v_n=n^-2 (n>=2), v_1=-sum_{n>=2}n^-3.
    # Normalization is for the infinite vector, not a finite truncated one.
    v1 = -(zeta(3.0, 1.0) - 1.0)
    norm = np.sqrt(v1*v1 + zeta(4.0, 1.0)-1.0)
    v = np.arange(1, m+1, dtype=float)**-2
    v[0] = v1
    return v/norm


def abstract_columns(n, m, noninjective=False):
    """Output l2 coordinates 0..m; inputs 1..n. The infinite model is exact."""
    if m < n:
        raise ValueError('m must be at least n')
    j = np.arange(1, m+1, dtype=float)
    d = j**-2
    a = np.zeros(m+1); a[0] = 1
    R = np.zeros((m+1, n)); R[1:n+1, :] = np.diag(d[:n])
    if noninjective:
        v = vector_v(m)
        R[1:, :] -= np.outer(d*v, v[:n])
    K = R + np.outer(a, 1/j[:n])
    return K, a


def distance_and_control(K, a, n):
    """Least-squares Schur distance; 0-based n. Returns residual and control norm.

    Works on weighted output columns, avoids forming or inverting K.T @ K.
    Rank checks and roundoff are diagnostic, not certificates.
    """
    others = np.column_stack((a, np.delete(K, n, axis=1)))
    coef, _, rank, _ = lstsq(others, K[:, n], cond=None, lapack_driver='gelsd')
    r = K[:, n] - others @ coef
    distance = np.linalg.norm(r)
    return distance, (1/distance if distance else np.inf), int(rank)


def abstract_demo(ns, m):
    for N in ns:
        for bad in (False, True):
            K, a = abstract_columns(N, m, bad)
            dist, control, rank = distance_and_control(K, a, 0)
            print(f'{"kernel" if bad else "injective":9s} N={N:3d} M={m:5d} '
                  f'dist={dist:.8e} control={control:.8e} '
                  f'N^-0.9*control={control*N**(-0.9):.8e} rank={rank}')


def load_coefficients(path):
    """NPZ: t, x, M, B, S (time x space), and gamma, mu, kappa, A0, L, delta."""
    with np.load(path, allow_pickle=False) as f:
        data = {k: np.array(f[k]) for k in f.files}
    required = ['t','x','M','B','S','gamma','mu','kappa','A0','L','delta']
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError('missing keys: '+', '.join(missing))
    t, x = data['t'], data['x']
    if t.ndim != 1 or x.ndim != 1 or len(t)<2 or len(x)<3:
        raise ValueError('t and x must be one-dimensional grids')
    if not np.all(np.isfinite(t)) or not np.all(np.isfinite(x)):
        raise ValueError('grids must be finite')
    if not np.all(np.diff(t)>0) or not np.all(np.diff(x)>0):
        raise ValueError('grids must be strictly increasing')
    if abs(t[0])>1e-12 or abs(x[0])>1e-12 or not np.isclose(x[-1], float(data['L'])):
        raise ValueError('grids must cover t=0 and x=[0,L]')
    for key in ('M','B','S'):
        if data[key].shape != (len(t),len(x)) or not np.all(np.isfinite(data[key])):
            raise ValueError(f'{key} must be finite with shape (len(t),len(x))')
    for key in ('gamma','mu','kappa','A0','L','delta'):
        if data[key].ndim != 0 or not np.isfinite(data[key]):
            raise ValueError(f'{key} must be a finite scalar')
    if min(float(data[k]) for k in ('mu','kappa','A0','L')) <= 0 or float(data['gamma']) == 0:
        raise ValueError('positive physical constants and nonzero gamma required')
    if np.min(data['M'])<=0 or not 0<float(data['delta'])<t[-1]:
        raise ValueError('M must be positive and delta must lie inside t grid')
    return data


def trapezoid_weights(x):
    dx = np.diff(x)
    w = np.empty_like(x)
    w[0] = dx[0]/2; w[-1] = dx[-1]/2
    w[1:-1] = (dx[:-1]+dx[1:])/2
    return w


def galerkin(data, n, rtol=1e-8, atol=1e-10):
    """Linearized odd Galerkin with supplied active M,B,S and physical constants.

    The coefficient arrays must themselves come from the nonzero-loaded base;
    the code does not verify their provenance, symmetry, or forward admissibility.
    No physical initial state outside the sine trial space is assumed.
    """
    t,x = data['t'],data['x']; L=float(data['L']); kap=float(data['kappa'])
    gamma=float(data['gamma']); mu=float(data['mu']); A0=float(data['A0'])
    if n < 1 or len(x)<2*n+2:
        raise ValueError('need N>=1 and more than 2*N spatial cells to avoid sine aliasing')
    w=trapezoid_weights(x); q=2*np.pi*np.arange(1,n+1)/L
    Phi=np.sqrt(2/L)*np.sin(np.outer(x,q))
    ip={key:RegularGridInterpolator((t,x), data[key],bounds_error=True) for key in ('M','B','S')}
    def rhs(tt,state):
        y=state[:n*n].reshape(n,n); p=state[n*n:].reshape(n,n)
        points=np.column_stack((np.full_like(x,tt),x))
        coeff={key:ip[key](points) for key in ip}
        mass=Phi.T@((w*coeff['M'])[:,None]*Phi)
        bmat=Phi.T@((w*coeff['B'])[:,None]*Phi)
        smat=Phi.T@((w*coeff['S'])[:,None]*Phi)
        dy=np.linalg.solve(mass, bmat@y+smat@p-kap*(q*q)[:,None]*y)
        dp=-mu*p+gamma*y
        return np.r_[dy.ravel(),dp.ravel()]
    init=np.r_[np.zeros(n*n),np.eye(n).ravel()]
    sol=solve_ivp(rhs,(t[0],t[-1]),init,t_eval=t,method='BDF',rtol=rtol,atol=atol)
    if not sol.success:
        raise RuntimeError(sol.message)
    ym=sol.y[:n*n,:].T.reshape(len(t),n,n)
    flux=2*A0*kap*np.sqrt(2/L)*np.einsum('j,tji->ti',q,ym)
    return flux


def generate_base(params, cells, steps, rtol=1e-8, atol=1e-10):
    """Finite-difference active base (not validated until real data are supplied)."""
    keys=('a','k','b','c','kappa','lambda','L','A0','theta_star','g_star')
    missing=[k for k in keys if k not in params]
    if missing: raise ValueError('missing physical inputs: '+', '.join(missing))
    a,k,b,c,kap,lam,L,A0,theta0,g=(float(params[key]) for key in keys)
    if not np.all(np.isfinite([a,k,b,c,kap,lam,L,A0,theta0,g])) or min(a,k,c,kap,lam,L,A0,theta0)<=0 or b==0 or g==0:
        raise ValueError('positive material inputs and nonzero b, g_star required')
    if cells<4 or steps<10: raise ValueError('cells>=4 and steps>=10 required')
    alpha=a/(a+k); r=k/(a+k); beta=b/(a+k); d=b*b/(a+k)
    gamma=lam*beta; mu=lam*alpha; T=10/lam; delta=T/100
    x=np.linspace(0,L,cells+1); weights=trapezoid_weights(x)/L
    xi=x[1:-1]; ni=len(xi); dx=L/cells
    Qint=np.eye(ni)-np.outer(np.ones(ni),weights[1:-1])
    lap=(np.diag(np.full(ni,-2.))+np.diag(np.ones(ni-1),1)+np.diag(np.ones(ni-1),-1))/dx**2
    def evaluate(t,state):
        y=np.r_[0.,state[:ni],0.]; p=state[ni:ni+cells+1]; v=state[-1]
        m=g/L*np.sin(np.pi*t/T)**2; mt=g/L*(np.pi/T)*np.sin(2*np.pi*t/T)
        qy=y-(weights@y); pd=-mu*p+gamma*qy; theta=theta0+y
        w=m-v-alpha*p+beta*qy; E=mt+r*pd
        mass=c*np.eye(ni)+d*theta[1:-1,None]*Qint
        yd=np.linalg.solve(mass,kap*(lap@y[1:-1])-b*theta[1:-1]*E[1:-1]+k*lam*w[1:-1]**2)
        yt=np.r_[0.,yd,0.]; qyt=yt-(weights@yt)
        M=c+d*theta; S=lam*alpha*(b*r*theta-2*k*w)
        B=-d*qyt-b*E-b*r*gamma*theta+2*k*gamma*w
        return np.r_[yd,pd,lam*(m-v)], M,B,S,theta
    def rhs(t,state): return evaluate(t,state)[0]
    times=np.unique(np.r_[np.linspace(0,T,steps+1),delta])
    sol=solve_ivp(rhs,(0,T),np.zeros(ni+cells+1+1),t_eval=times,method='BDF',rtol=rtol,atol=atol)
    if not sol.success: raise RuntimeError(sol.message)
    arrays=[evaluate(tt,sol.y[:,i]) for i,tt in enumerate(times)]
    M=np.array([a_[1] for a_ in arrays]); B=np.array([a_[2] for a_ in arrays]); S=np.array([a_[3] for a_ in arrays])
    theta=np.array([a_[4] for a_ in arrays])
    return dict(t=times,x=x,M=M,B=B,S=S,gamma=gamma,mu=mu,kappa=kap,A0=A0,L=L,delta=delta,theta=theta,
                provenance=np.array('finite-difference approximation of active nonzero-loaded base; not a certificate'))


def run_physical(args):
    data=load_coefficients(args.input); t=data['t']; x=data['x']
    flux=galerkin(data,args.modes,args.rtol,args.atol)
    mask=t>=float(data['delta']); tj=t[mask]
    if len(tj)<2 or tj[0] != float(data['delta']):
        raise ValueError('time grid must include delta exactly and a later time')
    kw=trapezoid_weights(tj)
    lead=2*float(data['A0'])*np.sqrt(2/float(data['L']))*np.exp(-float(data['mu'])*tj)*data['S'][mask,0]
    K=np.sqrt(kw)[:,None]*flux[mask,:]; a=np.sqrt(kw)*lead
    dist,control,rank=distance_and_control(K,a,args.target-1)
    singular=np.linalg.svd(K,compute_uv=False)
    aug_singular=np.linalg.svd(np.column_stack((K,a)),compute_uv=False)
    cond=float(aug_singular[0]/aug_singular[-1]) if aug_singular[-1]>0 else float('inf')
    print(json.dumps({'label':'supplied coefficients, diagnostic only','N':args.modes,
                      'target':args.target,'distance':dist,'control_norm':control,
                      'others_rank':rank,'singular_values':singular.tolist(),
                      'augmented_singular_values':aug_singular.tolist(),'augmented_condition':cond},indent=2))


def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='command',required=True)
    a=sub.add_parser('abstract'); a.add_argument('--sizes',type=int,nargs='+',default=[4,8,16,32,64]); a.add_argument('--output-dim',type=int,default=4096)
    b=sub.add_parser('base'); b.add_argument('--params',required=True); b.add_argument('--cells',type=int,required=True); b.add_argument('--steps',type=int,required=True); b.add_argument('--output',required=True); b.add_argument('--rtol',type=float,default=1e-8); b.add_argument('--atol',type=float,default=1e-10)
    g=sub.add_parser('galerkin'); g.add_argument('--input',required=True); g.add_argument('--modes',type=int,required=True); g.add_argument('--target',type=int,default=1); g.add_argument('--rtol',type=float,default=1e-8); g.add_argument('--atol',type=float,default=1e-10)
    args=p.parse_args()
    if args.command=='abstract': abstract_demo(args.sizes,args.output_dim)
    elif args.command=='base':
        with open(args.params,encoding='utf8') as fp: params=json.load(fp)
        data=generate_base(params,args.cells,args.steps,args.rtol,args.atol)
        np.savez(args.output,**data)
        print('saved approximate active-base coefficients; no existence or accuracy certificate')
    else:
        if not 1<=args.target<=args.modes: p.error('target must be between 1 and modes')
        run_physical(args)

if __name__=='__main__': main()
