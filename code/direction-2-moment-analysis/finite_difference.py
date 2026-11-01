"""Independent Crank-Nicolson centered-difference PDE-ODE diagnostic.

Accepts supplied coefficient fields; manufactured sources are optional. This is
not an existence theorem or evidence about the physical active base.
"""
import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.sparse import diags, bmat, eye
from scipy.sparse.linalg import splu


def solve_fd(data, h, steps, sources=None):
    x=np.asarray(data['x'],float); times=np.asarray(data['t'],float)
    dx=np.diff(x)
    if len(x)<5 or not np.allclose(dx,dx[0]):
        raise ValueError('finite differences require a uniform spatial grid')
    L=float(data['L']); kap=float(data['kappa']); mu=float(data['mu'])
    gamma=float(data['gamma']); A0=float(data['A0'])
    h=np.asarray(h,float)
    if h.ndim==1: h=h[:,None]
    if h.shape[0]!=len(x): raise ValueError('h must have one row per grid point')
    if np.max(np.abs(h[[0,-1],:]))>1e-10:
        raise ValueError('this diagnostic assumes h endpoints vanish; not a condition on the model')
    ni=len(x)-2; ncol=h.shape[1]; interior=x[1:-1]
    get={k:RegularGridInterpolator((times,x),np.asarray(data[k]),bounds_error=True) for k in ('M','B','S')}
    lap=diags([np.ones(ni-1),-2*np.ones(ni),np.ones(ni-1)],[-1,0,1],format='csc')/dx[0]**2
    ident=eye(ni,format='csc')
    state=np.vstack([np.zeros((ni,ncol)),h[1:-1,:]])
    out_y=[state[:ni].copy()]; out_p=[state[ni:].copy()]; out_t=[times[0]]
    delta=float(data['delta'])
    # Construct a uniform integrator grid that contains delta only if the caller
    # chooses a compatible step count; interpolate output separately below.
    tgrid=np.linspace(times[0],times[-1],steps+1)
    for t0,t1 in zip(tgrid[:-1],tgrid[1:]):
        dt=t1-t0; mid=(t0+t1)/2
        pts=np.column_stack([np.full(ni,mid),interior])
        M,B,S=(get[k](pts) for k in ('M','B','S'))
        if np.min(M)<=0: raise ValueError('M must be positive')
        A=bmat([[diags(1/M)@(kap*lap+diags(B)),diags(S/M)],
                [gamma*ident,-mu*ident]],format='csc')
        force=np.zeros_like(state)
        if sources is not None:
            f,g=sources(mid,interior)
            f=np.asarray(f);g=np.asarray(g)
            if f.ndim==1:f=f[:,None]
            if g.ndim==1:g=g[:,None]
            force=np.vstack([np.broadcast_to(f/M[:,None],(ni,ncol)),np.broadcast_to(g,(ni,ncol))])
        state=splu(eye(2*ni,format='csc')-dt*A/2).solve((eye(2*ni,format='csc')+dt*A/2)@state+dt*force)
        out_y.append(state[:ni].copy());out_p.append(state[ni:].copy());out_t.append(t1)
    Y=np.array(out_y); P=np.array(out_p); tt=np.array(out_t)
    # One-sided second-order derivative; do not replace it with Y[1]/dx.
    flux=2*A0*kap*(4*Y[:,0,:]-Y[:,1,:])/(2*dx[0])
    # include delta and final time in the observation grid by interpolation
    out_times=np.unique(np.r_[delta,tt[tt>delta],tt[-1]])
    out_flux=np.column_stack([np.interp(out_times,tt,flux[:,j]) for j in range(ncol)])
    return {'t':tt,'x':x,'Y':Y,'P':P,'flux_t':out_times,'flux':out_flux}

if __name__=='__main__':
    import argparse,json
    from moments import load_coefficients,trapezoid_weights
    p=argparse.ArgumentParser(description='Independent FD diagnostic, user-supplied active coefficients')
    p.add_argument('--input',required=True);p.add_argument('--modes',type=int,required=True);p.add_argument('--steps',type=int,required=True)
    args=p.parse_args(); d=load_coefficients(args.input)
    if args.modes<1 or args.steps<1: p.error('modes and steps must be positive')
    x=d['x'];L=float(d['L']);q=2*np.pi*np.arange(1,args.modes+1)/L
    if len(x)<2*args.modes+2: p.error('insufficient grid for chosen modes')
    h=np.sqrt(2/L)*np.sin(np.outer(x,q));r=solve_fd(d,h,args.steps)
    weighted=np.sqrt(trapezoid_weights(r['flux_t']))[:,None]*r['flux']
    print(json.dumps({'label':'supplied coefficients, finite-difference diagnostic only',
                      'modes':args.modes,'steps':args.steps,
                      'singular_values':np.linalg.svd(weighted,compute_uv=False).tolist()},indent=2))
