# Cycle 9: preparation-to-memory map and its linearization

For an admissible positive unique solution of (1) in `direction-2-cycle9-preparation-protocol.md`, define the unconstrained terminal map \(\widetilde{\mathcal P}(g_p)=z(0)\in L^2(I)\). The exact Volterra formula is
\[\widetilde{\mathcal P}(g_p)=\lambda\int_{-T_p}^0 e^{\lambda s}u_x(s)\,ds
=\lambda\int_{-T_p}^0e^{\lambda s}[m(s)+rp(s)+\beta Qy(s)]ds.\tag{1}\]
Equivalently, using the *coupled* heat solution,
\[v(0)=\lambda\int_{-T_p}^0e^{\lambda s}m(s)ds,\qquad p(0)=\gamma\int_{-T_p}^0e^{\mu s}Qy(s)ds.\tag{2}\]
The physically terminal-compatible map \(\mathcal P\) is the restriction to controls for which \(y(0)=0\). Equations (1)–(2) are identities for actual solutions, not independent specifications of \(y,p\).

For a direction \(g_p=\epsilon Lm_1\), \(Y=\partial_\epsilon y|_0\), \(P=\partial_\epsilon p|_0\), \(V=\partial_\epsilon v|_0\), the equilibrium-base tangent system is
\[(cI+d\theta_*Q)Y_s-\kappa Y_{xx}=-b\theta_*[m_1'+rP_s],\quad P_s=-\mu P+\gamma QY,\quad V_s=\lambda(m_1-V),\tag{3}\]
with \(Y=P=V=0\) initially and homogeneous thermal boundaries. The scalar boundary-displacement control enters as the spatially uniform distributed term \(-b\theta_*m_1'\) **after exact equilibrium elimination**; it is not an added heat source. Equations (3) are justified as a directional derivative where the fixed-point map is \(C^1\); its linear forcing is bounded for \(m_1\in H^1(-T_p,0)\), with endpoint-compatible smooth controls dense in the chosen norm only as appropriate. The linear strong-energy estimates from the base report give \(Y\in H^1_sL^2\cap L^2_s(H^2\cap H^1_0)\), \(P\in H^1_sL^2\) and a bounded terminal \(L^2\) trace. With zero initial memory and \(Y\in L^2_sH^2_x\), the Volterra formula gives \(P\in H^1_sH^2_x\), hence an \(H^2\) terminal trace; this does not give higher spatial regularity.

Let \(R f(x)=f(L-x)\), \(\Pi_o=(I-R)/2\). Since \(m_1\) and \(1\) are reflection-even and \(Q,R,\partial_{xx}\) commute, the odd tangent obeys
\[(c+d\theta_*)Y_{o,s}-\kappa Y_{o,xx}=-b\theta_*rP_{o,s},\quad P_{o,s}=-\mu P_o+\gamma Y_o,\quad(Y_o,P_o)(-T_p)=0.\tag{4}\]
The inherited homogeneous linear energy estimate gives \(Y_o=P_o=0\). Thus \(D(\Pi_o\widetilde{\mathcal P})(0)=0\), indeed the full nonlinear odd component is identically zero in the unique-solution class by the symmetry proof in the obstruction report.

For the specified scalar input space the odd derivative has **range \(\{0\}\)**, not dense in \(H_o\); it contains no nonzero \(V_N\) element; its projection onto \(V_N\) is zero, not surjective for \(N\ge1\); and its kernel is the whole (nontrivial) unconstrained control tangent space. This is the kernel of the **odd** map, not a claim that the full \(D\widetilde{\mathcal P}(0)\) is zero. The final-temperature constraint may make the admissible control set non-open; no unconstrained derivative is silently identified with a tangent space to that constrained set. On any differentiable path of terminal-compatible controls the odd derivative is also zero. No submersion or locally reachable odd projected neighborhood follows.
