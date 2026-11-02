"""Manufactured finite-mode diagnostic; NOT a density or reachability proof."""
import time
import mpmath as mp

def run(n, prec):
    mp.mp.dps = prec
    d=mp.mpf(1); T=mp.mpf(1); kcount=2*n+6
    def moment(s,k):
        z=s+mp.j*k*mp.pi
        return mp.im(((z-2)*mp.exp(z)+z+2)/z**3)
    # Auxiliary b_n=n² and f=t(1-t) sum x_k sin(k*pi*t); mu=0
    # This is a manufactured diagnostic, not a claim about material parameters.
    A=mp.matrix(n+3,kcount); y=mp.matrix(n+3,1)
    for i in range(n):
        b=mp.mpf((i+1)**2); delta=d/b
        for k in range(1,kcount+1): A[i,k-1]=moment(-b,k)+(d/b**2)*moment(delta,k)
    for j in range(3):
        delta=d/mp.mpf((j+1)**2); y[n+j]=[1,0,-1][j]
        for k in range(1,kcount+1): A[n+j,k-1]=moment(delta,k)
    gram=A*A.T
    x=A.T*mp.lu_solve(gram,y)
    residual=mp.norm(A*x-y, p=mp.inf)
    l2=mp.sqrt(sum(x[k]*x[k] for k in range(kcount)))
    return residual,l2

if __name__=='__main__':
    start=time.monotonic()
    for n in (6,12):
        for prec in (100,160):
            try:
                res,norm=run(n,prec)
                print(f'N={n} basis={2*n+6} digits={prec} max_residual={mp.nstr(res,7)} coefficient_norm={mp.nstr(norm,7)}')
            except (ValueError,ZeroDivisionError) as e:
                print(f'N={n} digits={prec} failure={type(e).__name__}: {e}')
    print(f'elapsed_seconds={time.monotonic()-start:.3f}; finite constraints only, not a proof')
