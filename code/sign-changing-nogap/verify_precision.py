"""Independent 60-digit oscillatory-basis moment verification of float64 fits."""
import mpmath as mp
from study import solve, M,MU,GAMMA,S,KAPPA,L,B
mp.mp.dps=60

def coefficients(n):
    q=2*mp.pi*n/mp.mpf(str(L)); m=mp.mpf(str(M)); mu=mp.mpf(str(MU))
    k=mp.mpf(str(KAPPA)); gamma=mp.mpf(str(GAMMA)); s=mp.mpf(str(S)); b0=mp.mpf(str(B))
    A=(k*q*q-b0)/m; d=gamma*s/m
    delta=2*d/(mp.sqrt((A-mu)**2+4*d)+(A-mu)); b=A-mu+delta
    return q,delta,b

def transform(z,k):
    omega=mp.pi*k
    return mp.sqrt(2)*omega*(1-(-1)**k*mp.exp(z))/(z*z+omega*omega)

def main():
    print('nfit,mode,high_precision_temp_moment,high_precision_p1,control_norm')
    n=5; c,_,_,_=solve(n,'oscillatory',count=18,points=1000)
    cc=[mp.mpf(float(x)) for x in c]
    vals=[]; p1=None
    for j in range(1,16):
        q,d,b=coefficients(j); mu=mp.mpf(str(MU)); m=mp.mpf(str(M)); kappa=mp.mpf(str(KAPPA)); gamma=mp.mpf(str(GAMMA))
        Fp=sum(v*transform(-mu+d,i+1) for i,v in enumerate(cc)); Fm=sum(v*transform(-mu-b,i+1) for i,v in enumerate(cc))
        C=2*kappa*mp.sqrt(2/mp.mpf(str(L)))*q/m
        y=C*(d*Fp+b*Fm)/(d+b); p=C*gamma*(Fp-Fm)/(d+b)
        vals.append(y)
        if j==1:p1=p
    norm=mp.sqrt(sum(x*x for x in cc))
    print(n,'train',mp.nstr(mp.sqrt(sum(x*x for x in vals[:n])),8),mp.nstr(p1,8),mp.nstr(norm,8))
    print(n,'unseen',mp.nstr(mp.sqrt(sum(x*x for x in vals[n:])),8),mp.nstr(p1,8),mp.nstr(norm,8))
if __name__=='__main__': main()
