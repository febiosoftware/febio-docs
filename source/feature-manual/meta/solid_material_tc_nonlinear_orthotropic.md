The material type for the tension-compression nonlinear orthotropic material is `TC nonlinear orthotropic`.

This material is based on the following uncoupled hyperelastic strain energy function [^1]:

\[
\Psi\left(\mathbf{C},\lambda_{1},\lambda_{2},\lambda_{3}\right)=\tilde{\Psi}_{iso}\left(\mathbf{\tilde{C}}\right)+\sum\limits_{i=1}^{3}\tilde{\Psi}_{i}^{TC}\left(\tilde{\lambda}_{i}\right)+U\left(J\right)\,.
\]

The isotropic strain energy $\tilde{\Psi}_{iso}$ and the dilatational energy $U$ are the same as for the Mooney-Rivlin material. The tension-compression term is defined as follows:

\[
\tilde{\Psi}_{i}^{TC}\left(\tilde{\lambda}_{i}\right)=\begin{cases}
\xi_{i}\left(\tilde{\lambda}_{i}-1\right)^{\beta_{i}} & \tilde{\lambda}_{i}>1\\
0 & \tilde{\lambda}_{i}\leqslant1
\end{cases}\quad\xi_{i}\geqslant0\quad\left(\text{no sum over }i\right)\,.
\]

The $\tilde{\lambda}_{i}$ parameters are the deviatoric fiber stretches of the local material fibers:

\[
\tilde{\lambda}_{i}=\left(\mathbf{a}_{i}^{0}\cdot\mathbf{\tilde{C}}\cdot\mathbf{a}_{i}^{0}\right)^{1/2}\,.
\]

The local material fibers are defined (in the reference frame) as an orthonormal set of vectors $\mathbf{a}_{i}^{0}$. As with all uncoupled materials, this material uses the three-field element formulation.

A complete example for this material follows.
```
<material id="7" name="cartilage" type="TC nonlinear orthotropic">
  <c1>1.0</c1>
  <c2>0.0</c2>
  <k>100</k>
  <beta>4.3,4.3,4.3</beta>
  <ksi>4525, 4525, 4525</ksi>
  <mat_axis type="local">0,0,0</mat_axis>
</material>
```

[^1]: Ateshian, Gerard A, Ellis, Benjamin J, and Weiss, Jeffrey A, "Equivalence between short-time biphasic and incompressible elastic material responses", J Biomech Eng 129, 3 (2007), pp. 405-12.