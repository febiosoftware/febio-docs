The material type for maximum normal Lagrange strain damage criterion is `DC max normal Lagrange strain`. For this criterion,

\[
\Xi\left(\mathbf{F}\right)=\max\left(E_{1},E_{2},E_{3}\right)
\]

where $E_{1},E_{2},E_{3}$ are the principal values of $\mathbf{E}=\left(\mathbf{F}^{T}\cdot\mathbf{F}-\mathbf{I}\right)/2$.

_Example:_
```xml
<criterion type="DC max normal Lagrange strain"/>
```