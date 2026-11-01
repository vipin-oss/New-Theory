# Model, mass invertibility and solution setting

Starting with \(\sigma_x=0\), integrate the stress law and the displacement endpoints. Denoting spatial means by a bar, \(Q=I-\bar{\cdot}\), the constitutive equation yields \(\sigma=Dm-b\bar y-kv\) and \(u_x=m+rp+\beta Qy\). Thus \(w=m-v-\alpha p+\beta Qy\). Averaging \(z_s=\lambda w\), and subtracting the average, gives \(v_s=\lambda(m-v)\), \(p_s=-\mu p+\gamma Qy\). Differentiating \(u_x\) in time in the heat equation gives exactly
\[(cI+d(\theta_*+y)Q)y_s=\kappa y_{xx}-b(\theta_*+y)(m'+rp_s)+k\lambda w^2.\]
All boundary and initial conditions are specified in Cycle 10's asymmetric-preparation model; the reconstructed displacement is the integral from the fixed endpoint. \(Q\) commutes with time differentiation, not with multiplication by a nonconstant temperature. No such commutation is used above.

## Exact nonlinear mass inverse

Let \(\vartheta=\theta_*+y\in L^\infty(0,L)\), \(\vartheta\ge\vartheta_{\min}>0\). For \(f\in L^2\), solve \((cI+d\vartheta Q)h=f\). Define \(A(x)=c+d\vartheta(x)\). Then
\[h(x)=\frac{f(x)+d\vartheta(x)\bar h}{A(x)},\qquad \bar h=\frac{\overline{f/A}}{\overline{c/A}}.\tag{1}\]
Because \(A\ge c\) and \(\overline{c/A}\ge c/(c+d\|\vartheta\|_\infty)>0\), this defines a bounded inverse on \(L^2\); direct substitution verifies it. Weighted coercivity also holds:
\[\langle (cI+d\vartheta Q)h,h/\vartheta\rangle=c\int h^2/\vartheta+d\|Qh\|_2^2>0\quad(h\ne0).\]
So bounded strict positivity, rather than a smallness assumption on \(y\), suffices for invertibility. Smallness can still be useful to establish a positive solution and contraction estimates. Uniformity requires uniform upper/lower bounds; ordinary unweighted positivity of the nonsymmetric mass quadratic form is not assumed.

For smooth endpoint-compatible boundary controls, lift \(y=X+\tau_s+(1-2x/L)\tau_a\). A candidate strong space is \(X\in H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)\cap C_tH^1_0\), \(p\in H^1_tH^2_x\), \(v\in H^1\). The zero-start Volterra formula produces the memory regularity from \(y\in L^2_tH^2_x\). The inverse (1) alone is not a nonlinear existence or differentiability theorem: product, initial/boundary compatibility and quasilinear estimates remain to be proved. Weak solutions and rough boundary data require their own transposition theory. Zero controls give an exact positive equilibrium solution; no nontrivial nonlinear preparation is asserted.
