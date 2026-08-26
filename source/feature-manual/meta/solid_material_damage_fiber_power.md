The material type for Damage Fiber Power is `damage fiber power`.

By setting, 

\[
\Psi^{0}=\kappa\mathit{I_{1}}+\left(1-\frac{3}{2}\kappa\right)\mathit{K_{3}}
\]

and $\mathit{m(P)=\alpha_{1}(P)^{\alpha_{2}},}$ the strain-energy form above can be made suitable for modeling damage,

\[
\varPsi(C,D)=\alpha_{1}\left(\left(1-D\right)\left[\kappa I_{1}+\left(1-\frac{3}{2}\kappa\right)K_{3}\right]-c\right)^{\alpha_{2}}
\]

The Cauchy stress takes on the following form,

\[
\sigma=\frac{2}{J}(1-D)\frac{dm}{dP}\left[\kappa b+\left(1-\frac{3}{2}\kappa\right)\left[bI_{4}+I_{1}I_{4}m-I_{4}a\bigodot ba\right]\right]
\]

_Example:_
```xml
<solid type="damage fiber power">
  <a1>1400</a1>
  <a2>2.2</a2>
  <kappa>1e-08</kappa>
  <t0>0.98</t0>
  <Dmax>0.96</Dmax>
  <beta_s>0.06</beta_s>
  <gamma_max>17.98</gamma_max>
  <fiber type="angles">
    <theta>-39.87</theta>
    <phi>90</phi>
  </fiber>
</solid>
```