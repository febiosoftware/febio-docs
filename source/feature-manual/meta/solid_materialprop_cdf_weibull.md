The material type for a Weibull c.d.f. is `CDF Weibull`.

For this material the c.d.f. is given by

\[
F\left(\Xi\right)=1-\exp\left[-\left(\Xi/\mu\right)^{\alpha}\right]\,.
\]

Note that

\[
F\left(\mu\right)=1-e^{-1}\approx0.63\,,
\]

which shows that $\mu$ is the value of $\Xi$ at which the fraction $1-e^{-1}$ of bonds break. Here, $\alpha$ regulates the rate at which damage increases with increasing $\Xi$, with higher values of $\alpha$ producing a more rapid increase.

![FigDamageCDFWeibull.png](figs/FigDamageCDFWeibull.png)
/// figure-caption
Illustration of the `CDF Weibull` cumulative distribution function.
///

_Example:_
```xml
<damage type="CDF Weibull">
  <mu>1</mu>
  <alpha>5.0</alpha>
  <Dmax>1</Dmax>
</damage>
```
