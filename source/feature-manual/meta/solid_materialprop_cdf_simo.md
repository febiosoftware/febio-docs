The material type for Simo's c.d.f. [#Simo87] is `CDF Simo`.

For this material the c.d.f. is given by

\[
F\left(\Xi\right)=1-\beta-\left(1-\beta\right)\frac{\alpha}{\Xi}\left(1-e^{-\Xi/\alpha}\right)\,.
\]

Note that

\[
\lim\limits_{\Xi\to\infty}F\left(\Xi\right)=1-\beta 
\]

represents the maximum allowable damage. Therefore, $\beta$ regulates the maximum allowable damage, whereas $\alpha$ controls the rate at which $F\left(\Xi\right)$ increases with increasing $\Xi$.

![FigDamageCDFSimo.png](figs/FigDamageCDFSimo.png)
/// figure-caption
Illustration of the `CDF Simo` cumulative distribution function.
///

_Example:_
```xml
<damage type="CDF Simo">
  <a>0.1</a>
  <b>0</b>
  <Dmax>1</Dmax>
</damage>
```