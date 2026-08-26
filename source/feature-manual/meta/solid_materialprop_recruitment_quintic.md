The material type for a quintic polynomial bond recruitment function is `recruitment quintic`.

For this material the bond recruitment function is given by

\[
F\left(\Xi\right)=\begin{cases}
1 & \Xi\leqslant\mu_{\min}\\
1+rx^{3}\left(10-15x+6x^{2}\right) & \mu_{\min}<\Xi\leqslant\mu_{\max}\\
1+r & \mu_{\max}<\Xi
\end{cases}\,,\quad x=\frac{\Xi-\mu_{\min}}{\mu_{\max}-\mu_{\min}}\,.
\]

Its minimum value is $1$ and its maximum value is $1+r$ when $\Xi\ge\mu_{\text{max}}$.

_Example:_
```xml
<recruitment type="recruitment quintic">
  <mumin>0.2</mumin>
  <mumax>0.4</mumax>
  <Dmax>4</Dmax>
</recruitment>
```
