The material type for a porous neo-Hookean solid is `porous neo-Hookean`. This material describes a porous neo-Hookean material with referential solid volume fraction $\varphi_{r}^{s}$ (i.e., porosity $\varphi_{r}^{w}=1-\varphi_{r}^{s}$). The pores are compressible but the skeleton is intrinsically incompressible. Thus, upon pore closure, the material behavior needs to switch from compressible to incompressible. This material may be used to model the porous solid matrix of a biphasic or multiphasic material, in which case it inherits the value of $\varphi_{r}^{s}$ from that parent material.

This model is derived from the following hyperelastic strain-energy function:

\[
W=\frac{\mu}{2}\left(\bar{I}_{1}-3\right)-\mu\ln\bar{J}\,,
\]

where $\bar{J}$ represents the pore volume ratio, evaluated from

\[
\bar{J}=\frac{J-\varphi_{r}^{s}}{1-\varphi_{r}^{s}}\,,
\]

and $\bar{I}_{1}=\text{tr}\bar{\mathbf{C}},$ with

\[
\bar{\mathbf{F}}=\left(\frac{\bar{J}}{J}\right)^{1/3}\mathbf{F}\,,\quad\bar{\mathbf{C}}=\bar{\mathbf{F}}^{T}\cdot\bar{\mathbf{F}}=\left(\frac{\bar{J}}{J}\right)^{2/3}\mathbf{C}\,,
\]

and \bar{J}=\det\bar{\mathbf{F}}. The porosity \varphi^{w} in the current configuration evolves with the volume ratio J according to

\[
\varphi^{w}=\frac{J-1+\varphi_{r}^{w}}{J}=\frac{J-\varphi_{r}^{s}}{J}=\bar{J}\left(1-\varphi_{r}^{s}\right)\,.
\]

Thus, pore closure occurs when $J=\varphi_{r}^{s}$ and $\bar{J}=0$.

By comparison to a standard neo-Hookean material, this porous neo-Hookean material has an effective Young's modulus equal to

\[
E=\frac{3\mu}{1+\frac{1}{2}\left(\varphi_{r}^{w}\right)^{2}}\,,
\]

and an effective Poisson's ratio equal to

\[
\nu=\frac{1-\left(\varphi_{r}^{w}\right)^{2}}{2+\left(\varphi_{r}^{w}\right)^{2}}\,.
\]

Therefore, the two material properties that need to be provided are $E$ and the referential porosity $\varphi_{r}^{s}=1-\varphi_{r}^{w}$. Poisson's ratio in the limit of infinitesimal strains is dictated by the porosity according to the above formula. In particular, a highly porous material ($\varphi_{r}^{w}\to1$) has an effective Poisson ratio that approaches zero ($\nu\to0$) and $E\to2\mu$  in the range of infinitesimal strains. A low porosity material ($\varphi_{r}^{w}\to0$) has $\nu\to\frac{1}{2}$ and $E\to3\mu$, which is the expected behavior of an incompressible neo-Hookean solid. Note that setting $\varphi_{r}^{w}=0$ ($\varphi_{r}^{s}=1$) would not produce good numerical behavior, since the Cauchy stress in an incompressible material would need to be supplemented by a hydrostatic pressure term (a Lagrange multiplier that enforces the incompressibility constraint). Nevertheless, this compressible porous neo-Hookean material behaves well even for values of $\varphi^{w}$ as low as $\sim0.015$.

_Example:_
```xml
<material id="1" type="porous neo-Hookean">
  <density>1.0</density>
  <E>1.0</E>
  <phi0>0.2</phi0>
</material>
```