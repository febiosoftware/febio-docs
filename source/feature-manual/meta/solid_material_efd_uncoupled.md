The material type for an ellipsoidal continuous fiber distribution in an uncoupled formulation is `EFD uncoupled`. Since fibers can only sustain tension, this material is not stable on its own. It must be combined with a stable uncoupled material that acts as a ground matrix, using a `uncoupled solid mixture` container as described in [uncoupled solid mixture](solid_material_uncoupled_solid_mixture.md). 

The stress $\tilde{\boldsymbol{\sigma}}$ for this material is given by [^1][^2][^3]: 

\[
\tilde{\boldsymbol{\sigma}}=\int_{0}^{2\pi}\int_{0}^{\pi}H\left(\tilde{I}_{n}-1\right)\tilde{\sigma}_{n}\left(\mathbf{n}\right)\sin\varphi\,d\varphi\,d\theta.
\]

$\tilde{I}_{n}=\tilde{\lambda}_{n}^{2}=\mathbf{N}\cdot\mathbf{\tilde{C}}\cdot\mathbf{N}$ is the square of the fiber stretch $\tilde{\lambda}_{n}$, $\mathbf{N}$ is the unit vector along the fiber direction (in the reference configuration), which in spherical angles is directed along $\left(\theta,\varphi\right)$, $\mathbf{n}=\mathbf{\tilde{F}}\cdot\mathbf{N}/\tilde{\lambda}_{n}$, and $H\left(.\right)$ is the unit step function that enforces the tension-only contribution. The fiber stress is determined from a fiber strain energy function in the usual manner,

\[
\tilde{\sigma}_{n}=\frac{2\tilde{I}_{n}}{J}\frac{\partial\tilde{\Psi}}{\partial\tilde{I}_{n}}\mathbf{n}\otimes\mathbf{n}\,,
\]

where in this material,

\[
\tilde{\Psi}\left(\mathbf{n},\tilde{I}_{n}\right)=\xi\left(\mathbf{n}\right)\left(\tilde{I}_{n}-1\right)^{\beta\left(\mathbf{n}\right)}\,.
\]

The materials parameters $\beta$ and $\xi$ are determined from:

\[
\begin{aligned}\xi\left(\mathbf{n}\right) & =\left(\frac{\cos^{2}\theta\sin^{2}\varphi}{\xi_{1}^{2}}+\frac{\sin^{2}\theta\sin^{2}\varphi}{\xi_{2}^{2}}+\frac{\cos^{2}\varphi}{\xi_{3}^{2}}\right)^{-1/2}\\
\beta\left(\mathbf{n}\right) & =\left(\frac{\cos^{2}\theta\sin^{2}\varphi}{\beta_{1}^{2}}+\frac{\sin^{2}\theta\sin^{2}\varphi}{\beta_{2}^{2}}+\frac{\cos^{2}\varphi}{\beta_{3}^{2}}\right)^{-1/2}
\end{aligned}
\,.
\]

_Example:_
```xml
<material id="1" type="uncoupled solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <k>1000</k>
  <solid type="Mooney-Rivlin">
    <c1>1</c1>
    <c2>0</c2>
  </solid>
  <solid type="EFD uncoupled">
    <ksi>10, 12, 15</ksi>
    <beta>2.5, 3, 3</beta>
  </solid>
</material>
```
[^1]: Lanir, Y., "Constitutive equations for fibrous connective tissues", J Biomech 16, 1 (1983), pp. 1-12.

[^2]: Ateshian, G. A., "Anisotropy of fibrous tissues in relation to the distribution of tensed and buckled fibers", J Biomech Eng 129, 2 (2007), pp. 240-9.

[^3]: Ateshian, G. A., Rajan, V., Chahine, N. O., Canal, C. E., and Hung, C. T., "Modeling the matrix of articular cartilage using a continuous fiber angular distribution predicts many observed phenomena", J Biomech Eng 131, 6 (2009), pp. 061003.

