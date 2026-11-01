"""Artificial manufactured sine-expansion boundary-trace truncation test."""
import numpy as np
from manufactured_high_frequency import coefficient

def derivative(n,kind,modes,cells=8192):
    x=np.linspace(0,1,cells+1);q=2*np.pi*n
    s=coefficient(x,kind)[0]; v=np.sqrt(2)*np.sin(q*x)*(s/q**2+1/q**3)
    j=np.arange(1,modes+1);basis=np.sqrt(2)*np.sin(np.outer(x,2*np.pi*j))
    coeff=np.trapezoid(v[:,None]*basis,x,axis=0)
    approx=coeff@(np.sqrt(2)*2*np.pi*j)
    true=np.sqrt(2)*(s[0]/q+1/q**2)
    return approx,true
if __name__=='__main__':
    print('ARTIFICIAL manufactured spatial mode truncation, n=4, cells=8192')
    for kind in ('smooth','sobolev'):
        for m in (8,16,32,64,128,256):
            a,b=derivative(4,kind,m);print(kind,m,f'{abs(a-b):.9e}')
