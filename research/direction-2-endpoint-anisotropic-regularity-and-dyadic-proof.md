# Endpoint: anisotropic interpolation, exact dyadic threshold, and delay

**Actual endpoint classification: OPEN.** This report proves a sharp obstruction for the inherited isotropic-corrector approximation route, not failure of the physical square function. It uses the fixed actual feedback and strong/weak estimates conditional on `direction-2-active-base-dependency-audit.md`.

## 1. Consequences of the actual positive-time gain

On \(Q_\varepsilon=(\varepsilon,T)\times I\), \(S\in L^2_tH^3_x\cap H^1_tH^1_x\). By compatible bounded extension in each variable and Fourier multipliers, for every \(0\le\theta\le1\),
\[S\in H^\theta_t H^{3-2\theta}_x,\quad
\|S\|_{H^\theta_tH^{3-2\theta}_x}^2\le C_\varepsilon(\|S\|_{L^2H^3}^2+\|S\|_{H^1H^1}^2).\tag{1}\]
Indeed, with \(X=1+|\xi|^2\), \(W=1+|\omega|^2\), \(W^\theta X^{3-2\theta}=(X^3)^{1-\theta}(WX)^\theta\le(1-\theta)X^3+\theta WX\). Extension operators on a rectangle are bounded simultaneously in the indicated integer spaces; restriction gives (1). In particular \(S\in H^{1/2}_tH^2_x\). This is real fractional time regularity, not \(S_t\in H^\eta_tL^2_x\). Sobolev embedding in time gives \(S\in C^{0,\theta-1/2}_tH^{3-2\theta}_x\) for \(1/2<\theta\le1\); at \(\theta=1\) take any Hölder exponent at most \(1/2\). These bounds depend on \(\varepsilon\); they do not establish initial-corner bounds.

Write \(\mathcal A=H^1_tL^2_x\cap L^2_tH^2_x\), with the sum-of-squares Hilbert norm. Spatial mollification with a simultaneous \(H^1,H^2,H^3\) extension gives
\[\|S-S^{(x)}_r\|_{\mathcal A(Q_\varepsilon)}\le Cr(\|S_t\|_{L^2H^1}+\|S\|_{L^2H^3}).\tag{2}\]
This is quantitative, but spatial smoothing **alone** does not generally make \(S^{(x)}_r\in H^3(Q_\varepsilon)\): it creates no \(\partial_t^2\) or \(\partial_t^3\). Here \(H^3(Q)\) is the isotropic norm \(\sum_{a+b\le3}\|\partial_t^a\partial_x^bf\|_{L^2(Q)}^2\), not \(L^2H^3_x\).

After a bounded time extension of \(H^1_tH^1_x\cap L^2_tH^3_x\), time mollification \(S_\tau\) obeys
\[\|S-S_\tau\|_{\mathcal A}\le C[\omega_2(S_t,\tau;L^2_x)+\tau^{1/2}\|S\|_{H^{1/2}_tH^2_x}],\quad
\|S_\tau\|_{H^3(Q_\varepsilon)}\le C(1+\tau^{-2})\|S\|_{L^2H^3\cap H^1H^1}.\tag{3}\]
Here \(\omega_2\) is the translation modulus of the extended \(S_t\) in \(L^2_{t,x}\); standard convolution can be followed by a spatial smoothing limit without changing the bounds. For the cost, \(\partial_t^3S_\tau\) uses two derivatives of the mollifier on \(S_t\); \(\partial_t^2\partial_xS_\tau\) uses one; \(\partial_t\partial_x^2S_\tau\) follows from the half-time derivative in (1); \(\partial_x^3S_\tau\) is already in \(L^2\). For any \(0<\alpha<1/4\), \(\tau_j=2^{-\alpha j}\) makes the displayed \(H^3\) cost and the \(H^2\)-part of the error summable. A sufficient remaining condition is
\[\sum_j\omega_2(S_t,2^{-\alpha j};L^2_x)^2<\infty.\tag{4}\]
This is a square-Dini time-translation condition; mere \(S_t\in L^2\) gives convergence of the modulus, not (4). For example \(S_t\in H^\eta_tL^2_x\), any \(\eta>0\), suffices. This statement is local to \(Q_\varepsilon\); the original full-time corrector needs a separate early-time argument.

## 2. Exact criterion for this dyadic approximation route

Let \(Q=(0,T)\times I\), restrict to functions even in \(x\), take \(A=\mathcal A(Q)\), and \(B=H^3(Q)\) with its isotropic norm multiplied by a fixed constant so \(\|f\|_B\ge\|f\|_A\). The dense compact embedding \(B\hookrightarrow A\) defines a positive self-adjoint operator \(L\) on \(A\) with form domain \(B\); choose an \(A\)-orthonormal eigenbasis \(e_\ell\), eigenvalues \(\lambda_\ell\ge1\), and write \(S=\sum c_\ell e_\ell\). For the exact squared K-functional
\[K_j(S)^2=\inf_{f\in B}\{\|S-f\|_A^2+2^{-j}\|f\|_B^2\}
=\sum_\ell|c_\ell|^2\frac{2^{-j}\lambda_\ell}{1+2^{-j}\lambda_\ell}.\tag{5}\]
The minimizer has coefficient \(c_\ell/(1+2^{-j}\lambda_\ell)\); the formula follows by completing the square and monotone limits. Since \(\sum_{j\ge0}\min(1,2^{-j}\lambda)\asymp1+\log\lambda\),
\[\boxed{\exists f_j\in H^3_{\rm even}:\ \sum_j(\|S-f_j\|_A^2+2^{-j}\|f_j\|_B^2)<\infty
\iff\sum_\ell(1+\log\lambda_\ell)|c_\ell|^2<\infty.}\tag{6}\]
Smooth even functions are dense in \(B\), so each minimizer can be approximated to a summable additional cost. This is the precise logarithmic interpolation threshold for **this sufficient proof route**, not a necessary condition for the actual PDE endpoint. It is weaker than any positive power of \(L\). If (6) holds, the inherited fixed-feedback column estimate gives the required dyadic square sum: on \(2^j\le n<2^{j+1}\), \(\sum q_n^{-1}=O(1)\), \(\sum q_n^{-2}=O(2^{-j})\), with a single coefficient-dependent constant, independent of \(j,n,f_j\).

## 3. Lacunary obstruction, including nonperiodic time and exact norm

On \(\mathbb T=(0,2\pi)\), use \(\widehat f(m)=(2\pi)^{-1}\int f(t)e^{-imt}dt\), so Parseval is \(\|f\|_2^2=2\pi\sum|\hat f(m)|^2\). Let
\[g(t)=\sum_{k\ge1}\frac{\sin(2^kt)}{2^kk},\qquad \hat g(2^k)=\frac{1}{2i\,2^kk}.\]
Thus \(g\in H^1(\mathbb T)\) since \(\sum k^{-2}<\infty\). With smooth even nonzero \(\psi(x)\), \(g\psi\in H^1_tH^m_x\cap L^2_tH^m_x\) for every \(m\). For any periodic approximant \(f\), project against \(\psi\): the full \(\mathcal A\) error controls its scalar \(H^1_t\) error and isotropic \(H^3(Q)\) controls its scalar \(H^3_t\) norm. For each frequency \(\omega=2^k\), minimizing \(A|c-b|^2+2^{-j}B|b|^2\), \(A\asymp\omega^2\), \(B\asymp\omega^6\), gives \(AB2^{-j}|c|^2/(A+2^{-j}B)\). For \(k\ge j/4+C\), this is at least \(c/k^2\); summing modes gives \(K_j^2\ge c\sum_{k\ge j/4+C}k^{-2}\ge c'/j\). Hence \(\sum K_j^2=\infty\). Constants include the factor \(2\pi\), \(\psi\) normalization and the two conjugate frequencies, none affect divergence.

The obstruction survives a finite nonperiodic time interval and the **exact** norms: choose a smooth time cutoff \(\chi\) compactly supported in a subinterval of \((\delta/2,T)\), with positive integral, after an affine rescaling of time to a circle, and set \(S_{\rm abs}=\chi g\psi\). Its \(2^k\)-frequency coefficients equal \(\hat\chi(0)/(2i2^kk)+o(2^{-k}/k)\): the remaining lacunary frequencies are separated by at least \(2^{k-1}\), and Fourier coefficients of smooth \(\chi\) decay faster than any power. Multiplying any interval approximant by another cutoff equal to one on \(\operatorname{supp}\chi\), and periodizing, is bounded on both \(\mathcal A\) and \(H^3\); spatial pairing with \(\psi\) is bounded as above. The same lower bound follows. Thus even a source supported strictly after the positive time cutoff, smooth to all spatial orders and in the established anisotropic intersection, can violate (6). It is an abstract function, **not** a base-generated coefficient or an actual-model counterexample.

## 4. Early/late decomposition and direct alternatives

At \(t_0=\delta/2\), linear superposition gives the exact restart state \((Y(t_0),P(t_0))\), with
\[P(t_0)=e^{-\mu t_0}h+\gamma\int_0^{t_0}e^{-\mu(t_0-s)}Y(s)ds.\]
The second term maps \(H_o\) boundedly into \(H^2\) (see graph structure report); the first term is an unsmoothed identity. Thus the positive gap can smooth the parabolic evolution of a separately identified early heat component, but it does not erase early memory or make its subsequent forcing smooth. Nor does the inherited \(\mathcal A\to q^{-3/2}\) trace estimate yield a summable block just from the gap. A cut-off proof must propagate **both** components and obtain an actual block estimate for the restart terms.

Direct block strategy: construct the vector map on a dyadic family, prove a uniform operator/trace estimate for the complete variable-coefficient parabolic evolution and Volterra feedback, and sum its Hilbert–Schmidt block norms. The inherited pointwise \(q^{-3/2}\) bound alone gives \(O(1)\) per block. Scalar resolvent or Gaussian upper bounds do not automatically give the needed boundary derivative square function, and rough \(B\), nonautonomous \(M\), feedback and the initial cutoff must remain in the estimate. No such direct block bound is proved here.

**Decision:** the established anisotropic spaces do not imply the exact logarithmic approximation criterion, even with support after the time gap. The actual source may nevertheless satisfy it by additional PDE structure; proving (6), the concrete local condition (4) plus a summable early-history estimate, or a direct block trace estimate is the exact missing step. This is a rigorous obstruction to this approximation inference, not a proof of endpoint failure.
