The material type for the uncoupled Holzapfel-Gasser-Ogden material [^1] is `Holzapfel-Gasser-Ogden`.

This material model uncouples deviatoric and volumetric behaviors. The deviatoric strain-energy function is given by:

\[
\Psi_{r}=\tilde{\Psi}_{r}\left(\tilde{\mathbf{C}}\right)+U\left(J\right)
\]

where

\[
\tilde{\Psi}_{r}=\frac{c}{2}\left(\tilde{I}_{1}-3\right)+\frac{k_{1}}{2k_{2}}\sum_{\alpha=1}^{2}\left(\exp\left(k_{2}\left\langle \tilde{E}_{\alpha}\right\rangle ^{2}\right)-1\right)
\]

and the default volumetric strain energy function is

\[
U\left(J\right)=\frac{k}{2}\left(\frac{J^{2}-1}{2}-\ln J\right)
\]

The fiber strain is

\[
\tilde{E}_{\alpha}=\kappa\left(\tilde{I}_{1}-3\right)+\left(1-3\kappa\right)\left(\tilde{I}_{4\alpha}-1\right)
\]

where $\tilde{I}_{1}=tr\tilde{\mathbf{C}}$ and $\tilde{I}_{4\alpha}=\mathbf{a}_{\alpha r}\cdot\tilde{\mathbf{C}}\cdot\mathbf{a}_{\alpha r}$. The Macaulay brackets around $\left\langle \tilde{E}_{\alpha}\right\rangle$ indicate that this term is zero when $\tilde{E}_{\alpha}<0$ and equal to $\tilde{E}_{\alpha}$ when this strain is positive.

There are two fiber families along the vectors $\mathbf{a}_{\alpha r} (\alpha=1,2)$, lying in the $\left\{ \mathbf{e}_{1},\mathbf{e}_{2}\right\}$ plane of the local material axes $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$, making an angle $\pm\gamma$ with respect to $\mathbf{e}_{1}$. Each fiber family has a dispersion $\kappa$, where $0\le\kappa\le\frac{1}{3}$. When $\kappa=0$ there is no fiber dispersion, implying that all the fibers in that family act along the angle $\pm\gamma$; the value $\kappa=\frac{1}{3}$ represents an isotropic fiber dispersion. All other intermediate values of $\kappa$ produce a $\pi$-periodic von Mises fiber distribution, as described in [^1]. $c$ is the shear modulus of the ground matrix; $k_{1}$ is the fiber modulus and $k_{2}$ is the exponential coefficient.

_Example:_
```xml
<material id="2" type="Holzapfel-Gasser-Ogden">
  <c>7.64</c>
  <k1>996.6</k1>
  <k2>524.6</k2>
  <gamma>49.98</gamma>
  <kappa>0.226</kappa>
  <k>1e5</k>
</material>
```

[^1]: Gasser, T Christian, Ogden, Ray W, and Holzapfel, Gerhard A, "Hyperelastic modelling of arterial layers with distributed collagen fibre orientations", J R Soc Interface 3, 6 (2006), pp. 15-35.