The material type for a quintic polynomial c.d.f. is `CDF quintic`.

For this material the c.d.f. is given by

\[
F\left(\Xi\right)=\begin{cases}
0 & \Xi\leqslant\mu_{\min}\\
x^{3}\left(10-15x+6x^{2}\right) & \mu_{\min}<\Xi\leqslant\mu_{\max}\\
1 & \mu_{\max}<\Xi
\end{cases}\,,\quad x=\frac{\Xi-\mu_{\min}}{\mu_{\max}-\mu_{\min}}\,.
\]

Note that

\[
F\left(\frac{1}{2}\left(\mu_{\min}+\mu_{\max}\right)\right)=\frac{1}{2}\,,
\]

which shows that $\left(\mu_{\min}+\mu_{\max}\right)/2$ is the value of $\Xi$ at which half of the bonds break. The range $\mu_{\max}-\mu_{\min}$ regulates the rate at which damage increases with increasing $\Xi$, with a narrower range producing a more rapid increase.

![FigDamageCDFQuintic.png](figs/FigDamageCDFQuintic.png)
/// figure-caption
Illustration of the `CDF quintic` cumulative distribution function.
///

_Example:_
```xml
<damage type="CDF quintic">
  <mumin>0.3</mumin>
  <mumax>1.7</mumax>
  <Dmax>1</Dmax>
</damage>
```