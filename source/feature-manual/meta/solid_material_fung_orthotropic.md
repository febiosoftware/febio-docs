The material type for orthotropic Fung elasticity [^1] [^2] is `Fung orthotropic`.

The hyperelastic strain energy function is given by [^3],

\[
\Psi=\frac{1}{2}c\left(e^{\tilde{Q}}-1\right)+U\left(J\right)\,,
\]

where,

\[
\tilde{Q}=c^{-1}\sum\limits_{a=1}^{3}\left[2\mu_{a}\mathbf{M}_{a}:\mathbf{\tilde{E}}^{2}+\sum\limits_{b=1}^{3}\lambda_{ab}\left(\mathbf{M}_{a}:\mathbf{\tilde{E}}\right)\left(\mathbf{M}_{b}:\mathbf{\tilde{E}}\right)\right].
\]

Here, $\mathbf{\tilde{E}}=\left(\mathbf{\tilde{C}}-\mathbf{I}\right)/2$ and $\mathbf{M}_{a}=\mathbf{V}_{a}\otimes\mathbf{V}_{a}$ where $\mathbf{V}_{a}$ defines the initial direction of material axis $a$. The Lamé constants $\mu_{a} (a=1,2,3)$ and $\lambda_{ab} (a,b=1,2,3, \lambda_{ba}=\lambda_{ab})$ are related to Young's moduli $E_{a}$, shear moduli $G_{ab}$ and Poisson's ratios $\nu_{ab}$ via

\[
\begin{aligned} & \left[\begin{array}{cccccc}
\lambda_{11}+2\mu_{1} & \lambda_{12} & \lambda_{13} & 0 & 0 & 0\\
\lambda_{12} & \lambda_{22}+2\mu_{2} & \lambda_{23} & 0 & 0 & 0\\
\lambda_{13} & \lambda_{23} & \lambda_{33}+2\mu_{3} & 0 & 0 & 0\\
0 & 0 & 0 & \frac{1}{2}\left(\mu_{1}+\mu_{2}\right) & 0 & 0\\
0 & 0 & 0 & 0 & \frac{1}{2}\left(\mu_{2}+\mu_{3}\right) & 0\\
0 & 0 & 0 & 0 & 0 & \frac{1}{2}\left(\mu_{1}+\mu_{3}\right)
\end{array}\right]^{-1}\\
 & =\left[\begin{array}{cccccc}
\frac{1}{E_{1}} & -\frac{\nu_{12}}{E_{1}} & -\frac{\nu_{13}}{E_{1}} & 0 & 0 & 0\\
-\frac{\nu_{21}}{E_{2}} & \frac{1}{E_{2}} & -\frac{\nu_{23}}{E_{2}} & 0 & 0 & 0\\
-\frac{\nu_{31}}{E_{3}} & -\frac{\nu_{32}}{E_{3}} & \frac{1}{E_{3}} & 0 & 0 & 0\\
0 & 0 & 0 & \frac{1}{G_{12}} & 0 & 0\\
0 & 0 & 0 & 0 & \frac{1}{G_{23}} & 0\\
0 & 0 & 0 & 0 & 0 & \frac{1}{G_{31}}
\end{array}\right]
\end{aligned}
.\]

The orthotropic Lamé parameters should produce a positive definite stiffness matrix.

_Example:_
```xml
<material id="3" type="Fung orthotropic">
  <E1>124</E1>
  <E2>124</E2>
  <E3>36</E3>
  <G12>67</G12>
  <G23>40</G23>
  <G31>40</G31>
  <v12>-0.075</v12>
  <v23>0.87</v23>
  <v31>0.26</v31>
  <c>1</c>
  <k>120000</k>
</material>
```

[^1]: Fung, Y. C., Fronek, K., and Patitucci, P., "Pseudoelasticity of arteries and the choice of its mathematical expression", Am J Physiol 237, 5 (1979), pp. H620-31.

[^2]: Fung, Y. C., Biomechanics : mechanical properties of living tissues 2nd (New York: Springer-Verlag, 1993).

[^3]: Ateshian, G. A. and Costa, K. D., "A frame-invariant formulation of Fung elasticity", J Biomech 42, 6 (2009), pp. 781-5.

