"""Illustrative dimensionless periodic thermoelastic material; not calibrated."""
import numpy as np
from scipy.linalg import expm

def symbol(k, ell, eta):
    return eta+(1-eta)/(1+(ell*k)**2)

def matrix(k, *, rho, C, beta, T0, c, kappa, h, kr, tau, ell, eta):
    """Fourier state [displacement,velocity,temperature,thermal displacement,r]."""
    a=symbol(k,ell,eta); j=1j
    return np.array([[0,1,0,0,0],[-C*k*k*a/rho,0,-j*k*beta/rho,0,0],
     [0,-j*k*T0*beta/c,-kappa*k*k/c,-h*k*k/c,-j*k/c],
     [0,0,1,0,0],[0,0,-j*k*kr/tau,0,-1/tau]],complex)

def metric(k, *, rho, C, beta, T0, c, kappa, h, kr, tau, ell, eta):
    return np.diag([C*k*k*symbol(k,ell,eta),rho,c/T0,h*k*k/T0,tau/(kr*T0)]).astype(complex)

def solution(k,initial,t,**parameters):
    return expm(t*matrix(k,**parameters)) @ np.asarray(initial,complex)

def energy(k,state,**parameters):
    H=metric(k,**parameters); y=np.asarray(state,complex)
    return float(np.real(np.vdot(y,H@y))/2)
