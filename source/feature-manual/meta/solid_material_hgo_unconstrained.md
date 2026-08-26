The material type for the unconstrained Holzapfel-Gasser-Ogden material [^1] is `HGO unconstrained`. 

The strain-energy function is given by:

\[
\begin{aligned}\Psi_{r} & =\frac{c}{2}\left(I_{1}-3\right)-c\ln J+\frac{k_{1}}{2k_{2}}\sum_{\alpha}\left(\exp\left(k_{2}\left\langle E_{\alpha}\right\rangle ^{2}\right)-1\right)\\
 & +\frac{K_{0}}{2}\left(\frac{J^{2}-1}{2}-\ln J\right)
\end{aligned}
\]

The fiber strain is

\[
E_{\alpha}=\kappa\left(I_{1}-3\right)+\left(1-3\kappa\right)\left(I_{4\alpha}-1\right)
\]

where $I_{1}=tr\mathbf{C}$ and $I_{4\alpha}=\mathbf{a}_{\alpha r}\cdot\mathbf{C}\cdot\mathbf{a}_{\alpha r}$. The Macaulay brackets around $\left\langle \tilde{E}_{\alpha}\right\rangle$ indicate that this term is zero when $E_{\alpha}<0$ and equal to $E_{\alpha}$ when this strain is positive.

There are two fiber families along the vectors $\mathbf{a}_{\alpha r} (\alpha=1,2)$, lying in the $\left\{ \mathbf{e}_{1},\mathbf{e}_{2}\right\}$ plane of the local material axes $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$, making an angle $\pm\gamma$  with respect to $\mathbf{e}_{1}$. Each fiber family has a dispersion $\kappa$, where $0\le\kappa\le\frac{1}{3}$. When $\kappa=0$ there is no fiber dispersion, implying that all the fibers in that family act along the angle $\pm\gamma$; the value $\kappa=\frac{1}{3}$ represents an isotropic fiber dispersion. All other intermediate values of $\kappa$  produce a $\pi$-periodic von Mises fiber distribution, as described in [^1]. $c$ is the shear modulus of the ground matrix; $k_{1}$ is the fiber modulus and $k_{2}$ is the exponential coefficient.

Unlike the uncoupled Holzapfel-Gasser-Ogden material presented in Section [Holzapfel-Gasser-Ogden](solid_material_holzapfel-gasser-ogden.md), this unconstrained version does not enforce isochoric deformation. This unconstrained model may be used to describe the porous solid matrix of a biphasic or multiphasic tissue model, where pore volume may change in response to influx or efflux of interstitial fluid.

_Example:_
```
<material id="2" type="HGO unconstrained">
  <c>7.64</c>
  <k1>996.6</k1>
  <k2>524.6</k2>
  <gamma>49.98</gamma>
  <kappa>0.226</kappa>
  <k>7.64e3</k>
</material>
```

[^1]: Gasser, T Christian, Ogden, Ray W, and Holzapfel, Gerhard A, "Hyperelastic modelling of arterial layers with distributed collagen fibre orientations", J R Soc Interface 3, 6 (2006), pp. 15-35.