"""Artificial time-series quadrature demonstration, not a physical model."""
import numpy as np
from moments import trapezoid_weights
from moment_diagnostics import diagnostics

def main():
    print('ARTIFICIAL time-series quadrature; finite columns only')
    for m in (8,16,32,64,256):
        t=np.linspace(.1,1,m); w=np.sqrt(trapezoid_weights(t));a=w*np.exp(-t)
        K=np.column_stack([a/n+w*np.sin(n*np.pi*t)/(n*n) for n in range(1,7)])
        out=diagnostics(K,a,4,1)
        print(m,'distance',f"{out['distance']:.8e}",'condition',f"{out['condition']:.8e}",
              'leakage to columns 5-6',f"{out['leakage']:.8e}")
if __name__=='__main__':main()
