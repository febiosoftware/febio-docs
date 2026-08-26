The material type for Damage Fiber Exponential is `damage fiber exponential`.

The effective strain-energy function is given by,

\[
\Psi^{0}=\kappa I_{1}+(1-3\kappa)I_{4}
\]

and

\[
m(P)=\frac{k_{1}}{2k_{2}}\left\{ \exp\left(k_{2}\left\langle P\right\rangle ^{2}\right)-1\right\},
\]

where $a$ denotes the direction of the fibers.
So that,

\[
\Psi=\frac{k_{1}}{2k_{2}}\left\{ \exp\left(k_{2}\left\langle \left(1-D_{a}\right)\left(\kappa I_{1}-\left(1-3\kappa\right)I_{4}\right)-1\right\rangle ^{2}\right)-1\right\} .
\]

The Cauchy stress then takes on the following form,

\[
\sigma=\frac{2}{J}(1-D)\frac{dm}{dP}\left[\kappa b+(1-3\kappa)I_{4}m\right].
\]

_Example:_
```xml
<solid type="damage fiber exponential"> 
  <k1>1288.97</k1> 
  <k2>400</k2> 
  <kappa>0.2</kappa> 
  <t0>0.9</t0> 
  <Dmax>0.99</Dmax> 
  <beta_s>0.001</beta_s> 
  <gamma_max>6.67</gamma_max> 
  <fiber type="angles"> 
    <theta>-54.94</theta> 
    <phi>90</phi> 
  </fiber> 
</solid>
```