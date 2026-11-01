# Fast nullspace, tail, Fredholm range, endpoint

**Status: VERIFIED UNDER EXPLICIT ASSUMPTIONS** for the frozen abstract operator, using the external Müntz and biorthogonal theorems. These are same-agent checks, not external certification.

## A. Infinite smooth fast nullspace from a source theorem

Almira, *Müntz Type Theorems I*, [Theorem 29, §3.4](https://arxiv.org/html/0710.3570#Thmtheorem29): for distinct real exponents \(\lambda_n\) and \(0<u<v\), the span of \(x^{\lambda_n}\) is dense in \(C[u,v]\) iff \(\sum_{\lambda_n\ne0}1/|\lambda_n|=\infty\). The version needed here has \(\lambda_n=b_n>0\) and the sum finite. This is the stated theorem; its proof appears in the cited section. We do not assert a new priority result.

Fix a closed interval \(J\) strictly inside any one of countably many disjoint subintervals of I. Under \(x=e^{-t}\), the fast exponentials on J correspond to \(x^{b_n}\) on a positive interval. Hahn–Banach and Riesz therefore give a nonzero finite real signed measure \(\nu\), supported in J, with \(\int e^{-b_nt}\,d\nu(t)=0\) for all n. Convolution with a nonzero real \(C_c^\infty\) bump of sufficiently small support produces \(w\in C_c^\infty(I)\), with
\[\int e^{-b_nt}w(t)dt=\left(\int e^{-b_nt}d\nu(t)\right)\left(\int e^{-b_nt}\rho(t)dt\right)=0.\]
The convolution is not zero: the Fourier transforms of two nonzero compactly supported distributions extend to nonzero entire functions, and their product cannot be identically zero. Choosing disjoint output supports yields independent \(h=w/t\), because t is bounded away from 0. Thus \(N=\{h\in C_c^\infty(I):Eh=0\}\) is infinite-dimensional. No approximation or finite list of moment equations is used.

## B. Verify the coupled tail and its norm

Let \(H=L^2((0,T),t\,dt)\), \(X=L^2(I,t\,dt)\), and extend X elements by zero. The kernel series proves self-adjointness and
\[\langle \mathsf Tv,v\rangle_H=d\sum_{j\ge0}\frac{d^j}{j!(j+1)!}\left|\int_0^T s^{j+1}v(s)ds\right|^2\ge0.\]
It is compact; hence \(Q=(I+\mathsf T)^{-1}\) exists and \(\|Q\|\le1\). For \(t\ge T\),
\[|\mathsf TQx(t)|\le d\|Qx\|_H\Big(\int_0^T s |H_d(t,s)|^2ds\Big)^{1/2}
\le (dT/\sqrt2)e^{2\sqrt{dTt}}\|x\|_X.\]
The last inequality follows from the positive series and \(\sum z^j/(j!)^2\le e^{2\sqrt z}\). Fix \(b_1>0\); for every n,
\[|(Rx)_n|\le C\|x\|_X e^{-Tb_n}\int_T^\infty t e^{-b_1(t-T)}e^{2\sqrt{dTt}}dt
\le C' e^{-Tb_n}\|x\|_X.\tag{1}\]
The integral is finite. In \(Y\), the coordinate functionals are thus dominated by \(C'e^{-\eta b_n}\); their squared norms sum. Hence R is Hilbert–Schmidt X→Y and S R is compact X→X. This uses the actual dependent Q and does not posit an independent tail.

## C. Closed range and smooth preimages

For a bounded compact K on a Hilbert space, the standard Riesz–Schauder theorem states that \(I+K\) is Fredholm of index zero: its range is closed, its kernel and adjoint kernel are finite-dimensional, and \(\operatorname{ran}(I+K)=(\ker(I+K)^*)^\perp\). Applying it to \(K=SR\), let \(m=\dim\ker A^*\). The algebraic quotient of N by \(N\cap\operatorname{ran}A\) has dimension at most m. Since N is infinite-dimensional, the intersection is infinite-dimensional. This is the **actual closed range**, not merely its closure.

For independent \(h_i\) in this intersection, solve \(Ax_i=h_i\). Solutions exist by the preceding equality; choosing the unique solution orthogonal to \(\ker A\) gives a bounded inverse on that complement. From \(x_i=h_i-SRx_i\), both terms are smooth and compactly supported in I, with the infinite series converging in every C^j. Applying E gives \(Ex_i=-Rx_i\) coordinatewise because \(ES=I\) on Y. A sends independent x_i to independent h_i, so x_i are independent.

## D. Endpoint functional on the correct space

The resolvent \(Qx=x-\mathsf TQx\) as an H identity has no point value for a general H class. For \(x\in X\) extended by zero, however, define the smooth representative near T by \(-\mathsf TQx\); it is canonical because x vanishes a.e. in a neighborhood of T. Define
\[L(x)=-\mathsf TQx(T)=-d\int_0^T H_d(T,s)(Qx)(s)sds.\]
The row \(dH_d(T,\cdot)\in H\), so \(|L(x)|\le C\|x\|_X\). For smooth x this equals the actual value of \(v=Qx\) at T. The kernel of a single scalar functional on an infinite-dimensional solution space has codimension at most one, hence remains infinite-dimensional. This enforces **v(T)=0**, not k(T)=0 (the latter already holds because x has interior support).
