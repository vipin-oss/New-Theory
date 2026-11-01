# Independent referee package

**Request:** Please attempt to invalidate the theorem, not merely confirm it. No separate human or AI has certified the proof. The manuscript is a prereferee draft; no publication priority or nonlinear physical result is asserted.

## One-page research summary

For \(T,d>0\), positive \(b_n\asymp n^2\) with a uniform positive square-root gap, and \(H=L^2((0,T),t\,dt)\), let
\[H_d(t,s)=\sum_{j\ge0}\frac{(dts)^j}{j!(j+1)!},\quad
(\mathsf Tv)(t)=d\int_0^T H_d(t,s)v(s)s\,ds,\quad Q=(I+\mathsf T)^{-1}.\]
For k define \((\mathsf Bk)_n=\int_0^T te^{-b_nt}k(t)dt+\int_T^\infty te^{-b_nt}(\mathsf TQk)(t)dt\). The exact tail depends on k through Q. The claim is that, for every \(I\Subset(0,T)\), the space \(\{k\in C_c^\infty(I):\mathsf Bk=0,\ (Qk)(T)=0\}\) is infinite-dimensional. Thus all moment equations and the endpoint condition hold simultaneously, not merely approximately. The proof makes no assertion that \(b_n\asymp n^2\) alone implies the square-root gap.

The argument constructs smooth biorthogonals for the fast exponential family by reversing a positive-exponential estimate, shifting, and convolution. They define a right inverse S on a weighted sequence space Y. The coupled tail R maps the interior-support Hilbert space X compactly to Y because it begins at T and has subexponential Bessel growth. Then A=I+SR is Fredholm on X. The smooth fast-nullspace is infinite-dimensional by Müntz incompleteness and smoothing; it meets the closed finite-codimension range of A in infinitely many independent elements. Exact preimages are smooth because \(x=h-SRx\), and their span retains infinite dimension after the endpoint constraint. The constructed correction is compactly supported inside I; the resulting control \(f=e^{\mu t}tQk\) is not compactly supported in I and has no terminal switch-off gap.

## Assumptions and scope

- \(b_n>0\) strictly increasing, \(b_n\asymp n^2\), \(\inf_n(\sqrt{b_{n+1}}-\sqrt{b_n})>0\); \(d,T,\mu>0\); real function spaces.
- The source biorthogonal bound and away-from-zero Müntz theorem are invoked exactly as detailed below.
- PDE interpretation additionally assumes the frozen odd linear model, zero initial odd fields, compatible smooth opposite boundary data and a valid boundary-lift solution framework. It does not establish nonlinear preparation, the full system, prescribed Gevrey regularity or an explicit numerical control.

## Dependency map and exact sources

1. [Cannarsa–Martinez–Vancostenoble, Theorem 2.1, eqs. (2.1)–(2.6)](https://arxiv.org/html/1706.02435#S2.ThmTheorem1): positive-exponential biorthogonals with norm \(e^{-\ell b_n+O(\sqrt{b_n})}\); choose \(N_*=1\) and two distinct lower-gap constants smaller than or equal to the actual global gap.
2. [Almira, Theorem 29, §3.4](https://arxiv.org/html/0710.3570#Thmtheorem29): power-span nondensity away from zero for finite reciprocal sum. Change variables \(x=e^{-t}\); Hahn–Banach/Riesz and convolution give smooth nullspace seeds.
3. Bessel series and self-adjoint positivity → Q exists → tail bound → R is Hilbert–Schmidt X→Y.
4. [Fredholm alternative, Theorem A.D.5](https://people.tamu.edu/~phoward/m612/s20/elliptic4.pdf) → actual closed finite-codimension range of A → exact preimages.
5. Smooth support and bounded endpoint functional → v(T)=0; modal matrix and smooth lift → conditional temperature/memory conclusions.

## Five difficult points to challenge

1. Does the published positive-exponential estimate retain all factors under reversal and shift? Verify \(\int t e^{-b_mt}\psi_n=\delta_{mn}\) and normalization by the correct \(\rho_n\).
2. Does the single strict margin \(a+\epsilon<T-\eta\) guarantee convergence for every derivative with common compact support, including small n?
3. Does the dependent tail really map X into Y with coordinate bound \(Ce^{-Tb_n}\), and is its Hilbert–Schmidt conclusion justified?
4. Does the infinite-dimensional Müntz seed space meet the **actual** Fredholm range in infinite dimension, and are the resulting preimages smooth rather than just X-valued?
5. Is the endpoint imposed on \(v=Qk\), not k, and do the boundary input sign, normalizing factor and Duhamel memory formula agree with the frozen PDE?

## Requested report from reviewer

Identify the first invalid implication, if any; supply a counterexample or missing hypothesis where possible. Check source theorem statements and their normalizations, verify all infinite series and quantifiers, and assess whether the exact PDE terminal trace follows in the stated class. If correct, specify any implicit hypotheses and describe the result's overlap with existing coupled-moment literature. No priority conclusion is requested without a comprehensive literature check. The original Ivanov–Pandolfi proof has not been accessed.
