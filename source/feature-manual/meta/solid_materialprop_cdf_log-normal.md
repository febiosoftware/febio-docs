The material type for a log-normal c.d.f. is `CDF log-normal`.

For this material the c.d.f. is given by

\[
F\left(\Xi\right)=\frac{1}{2}\text{erfc}\left[-\frac{\ln\left(\Xi/\mu\right)}{\sigma\sqrt{2}}\right]\,.
\]

Note that

\[
F\left(\mu\right)=1/2,
\]

which shows that $\mu$ is the value of $\Xi$ at which half of the bonds break. Here, $\sigma$ regulates the rate at which damage increases with increasing $\Xi$, with smaller values of $\sigma$ producing a more rapid increase.

![FigDamageCDFLogNormal.png](figs/FigDamageCDFLogNormal.png)
/// figure-caption
Illustration of the `CDF log-normal` cumulative distribution function.
///

_Example:_
```xml
<damage type="CDF log-normal">
  <mu>1</mu>
  <sigma>0.5</sigma>
  <Dmax>1</Dmax>
</damage>
```