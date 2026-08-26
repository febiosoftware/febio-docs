This material type is `fiber-natural-NH`.

The fiber strain energy density is given by

\[
\Psi_{n}\left(\lambda_{n}\right)=\frac{\xi}{2}H\left(\ln\frac{\lambda_{n}}{\lambda_{0}}\right)\left(\ln\frac{\lambda_{n}}{\lambda_{0}}\right)^{2}\,,
\]

where $\xi>0$ and $\lambda_{0}\ge1$. The tensile response engages at the tensile stretch ratio $\lambda_{0}$ ($\lambda_{0}=1$ by default). The natural (logarithmic or Hencky) strain along the fiber is $\ln\lambda_{n}$, whereas $\ln\frac{\lambda_{n}}{\lambda_{0}}=\ln\lambda_{n}-\ln\lambda_{0}$ is the natural strain relative to the tensile stretch threshold. This model produces a stress response which varies linearly with the natural strain.

_Example:_
```xml
<material id="1" name="Material1" type="solid mixture">
  <density>1</density>
  <solid type="neo-Hookean">
    <E>0.13</E>
    <v>0.3</v>
  </solid>
  <solid type="fiber-natural-NH">
    <ksi>1</ksi>
    <lam0>1.25</lam0>
    <fiber type="vector">0,0,1</fiber>
  </solid>
</material>
```

