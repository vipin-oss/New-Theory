"""Finite, weighted output diagnostics; leakage is only to available columns."""
import argparse
import numpy as np
from scipy.linalg import lstsq
from moments import abstract_columns

def diagnostics(K,a,N,target):
    if not (1<=target<=N<=K.shape[1]): raise ValueError('invalid block or target')
    kn=K[:,target-1]; others=np.column_stack((a,np.delete(K[:,:N],target-1,axis=1)))
    coef,_,rank,s=lstsq(others,kn,lapack_driver='gelsd'); residual=kn-others@coef
    d=np.linalg.norm(residual); sing=np.linalg.svd(np.column_stack((K[:,:N],a)),compute_uv=False)
    # This control is unreliable when d is near roundoff: explicitly report residual.
    f=residual/d**2 if d>0 else np.full_like(residual,np.nan)
    leakage=np.linalg.norm(K[:,N:].T@f) if N<K.shape[1] else np.nan
    constraint=np.linalg.norm(np.r_[others.T@f,kn@f-1])
    return dict(N=N,target=target,distance=d,control=1/d if d else np.inf,
                rank=rank,condition=sing[0]/sing[-1] if sing[-1]>0 else np.inf,
                leakage=leakage,constraint_error=constraint)

def main():
    p=argparse.ArgumentParser();p.add_argument('--columns',type=int,default=80);p.add_argument('--outputs',type=int,default=512)
    p.add_argument('--kind',choices=['injective','kernel'],default='kernel');p.add_argument('--blocks',type=int,nargs='+',default=[4,8,16,32])
    a=p.parse_args();K,lead=abstract_columns(a.columns,a.outputs,a.kind=='kernel')
    print('ARTIFICIAL sequence-space diagnostic; leakage excludes uncomputed infinite tail')
    for N in a.blocks:
        for target in (1,N): print(diagnostics(K,lead,N,target))
if __name__=='__main__':main()
