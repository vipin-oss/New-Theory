# Function-space and regularity theorems

Assume the hypotheses and exact operators of `FLAT_KERNEL_CONSTRUCTION_OR_NO_GO.md`. These statements are mathematical consequences of the exact equations; they are not numerical observations.

## 1. Support, smoothness, analytic and quasianalytic consequences

For each interior I the construction gives infinitely many real \(k\in C_c^\infty(I)\). Thus flatness at t=0 is not merely an asymptotic constraint: there are exact solutions whose flat correction actually vanishes near both endpoints, although their **control** \(f=e^{\mu t}t(I+\mathsf T)^{-1}k\) does not vanish near t=0. The resulting f is analytic in neighborhoods of both endpoints, because \(v=-\mathsf Tv\) where k=0, but cannot be analytic on a connected neighborhood of the whole interval. It is not terminal-flat. These facts do not claim Gevrey bounds on the interior of I.

The prior quasianalytic-control uniqueness theorem is consistent: the new f cannot belong to a quasianalytic vector class on [0,T] containing the entire jet extension and having the flat-jet uniqueness property. Analytic smoothing of \(\mathsf Tv\) does not make \(v=k-\mathsf Tv\) analytic on I. No conclusion is made for a prescribed Gevrey order \(s>1\), since the inverse construction's derivative bounds were not shown to have a specified Gevrey rate.

## 2. Leading support-edge oscillation and exponential cancellation

Let \(k\in C[0,T]\) be real, \(k\ne0\), \(v=(I+\mathsf T)^{-1}k\), and \(\mathsf Bk=0\). Flatness and endpoint compatibility are not needed for this lemma. Set \(a=\inf\operatorname{supp}k<T\). Then **both signs of k occur in every interval** \((a,a+\varepsilon)\cap(0,T)\). In particular k has infinitely many sign changes and zeros accumulating at its left support edge.

*Proof.* The tail estimate from Step 2 of the construction gives
\[\left|\int_0^T t e^{-b_nt}k(t)dt\right|\le C e^{-Tb_n}.\tag{1}\]
Suppose k has one sign on \((a,a+\varepsilon)\), with \(a+\varepsilon<T\). By definition of a, there is a closed interval \([u,v]\subset(a,a+\varepsilon)\) on which \(|k|\) is bounded below by a positive constant. Its one-signed contribution has magnitude at least \(c e^{-vb_n}\), whereas the absolute contribution from \([a+\varepsilon,T]\) is at most \(C'e^{-(a+\varepsilon)b_n}\). For large n the first dominates, contradicting (1), since \(v<T\). This excludes either sign, so both occur arbitrarily close to a. Continuity gives alternating zeros. ∎

More quantitatively, put \(P_n=\int t e^{-b_nt}k_+(t)dt\), \(N_n=\int t e^{-b_nt}k_-(t)dt\). For any \(\varepsilon>0\) with \(a+\varepsilon<T\), the sign property supplies intervals before \(a+\varepsilon\) where each sign is bounded away from zero. Hence \(P_n,N_n\ge c_\varepsilon e^{-(a+\varepsilon)b_n}\), and (1) yields
\[\left|P_n/N_n-1\right|\le C_\varepsilon e^{-(T-a-\varepsilon)b_n}.\tag{2}\]
Thus a hypothetical or constructed nonzero kernel element requires exponentially precise signed cancellation in the sampled fast transform. A one-sign near-edge assumption is a **sufficient condition for injectivity**, not a necessary condition for an arbitrary control. In particular, any correction with finitely many sign changes is excluded. This does not contradict the construction: its compactly supported corrections oscillate infinitely often at their left support edge.

## 3. Exact entire tail expansion and eventual nonzero fast moments

For any \(v\in H\), let \(q(t)=t\mathsf Tv(t)\), entire in t. Its growth satisfies \(|q(z)|\le C(1+|z|)e^{2\sqrt{dT|z|}}\). Cauchy estimates with circles of radius \(j^2\) about T imply \(\limsup_{j\to\infty}|q^{(j)}(T)|^{1/j}=0\). Consequently
\[A_v(z)=\sum_{j=0}^\infty q^{(j)}(T)z^{j+1}\tag{3}\]
is entire. For every \(b>0\), absolute termwise integration of the Taylor series at T gives the **convergent**, not merely asymptotic, identity
\[\int_T^\infty e^{-bt}q(t)dt=e^{-bT}A_v(1/b).\tag{4}\]
Indeed \(\sum_j |q^{(j)}(T)|b^{-(j+1)}<\infty\) exactly bounds the integrated absolute Taylor series.

If \(v\ne0\), then \(q\not\equiv0\): otherwise \(\mathsf Tv=0\), and expanding \(\langle v,\mathsf Tv\rangle_H\) as a positive sum of squared weighted polynomial moments shows all those moments vanish; polynomial density in H gives v=0. Therefore there is a finite smallest m with \(q^{(m)}(T)\ne0\). For any nonzero exact solution, (4) gives
\[\int_0^T t e^{-b_nt}k(t)dt=-e^{-Tb_n}A_v(1/b_n)
\sim-q^{(m)}(T)e^{-Tb_n}b_n^{-(m+1)}.\tag{5}\]
In particular the fast correction moment is nonzero for **all but finitely many n**. If the exact endpoint condition holds, \(q(T)=T k(T)\), because \(k=v+\mathsf Tv\) and \(v(T)=0\). For the constructed compact-interior k, \(q(T)=0\), so \(m\ge1\); m is still finite.

This proves an exact no-go for the naive construction: an exact nonzero k cannot itself annihilate the fast family at infinitely many sampled b_n. It does not prevent correcting a fast annihilator: the Fredholm construction changes the seed, and its correction necessarily has the nonzero fast moments prescribed by (5).
