This material type is `fiber-pow-linear`.

The fiber strain energy density is given by

\[
\Psi_{n}\left(I_{n}\right)=\begin{cases}
0 & I_{n}<1\\
\frac{\xi}{\beta}\left(I_{n}-1\right)^{\beta} & 1\leqslant I_{n}\leqslant I_{0}\\
B\left(I_{n}-I_{0}\right)-E\left(I_{n}^{1/2}-I_{0}^{1/2}\right)+\frac{\xi}{\beta}\left(I_{0}-1\right)^{\beta} & I_{0}<I_{n}
\end{cases}\,,
\]

where $I_{0}=\lambda_{0}^{2}$,

\[
\xi=\frac{E}{4\left(\beta-1\right)}I_{0}^{-3/2}\left(I_{0}-1\right)^{2-\beta},\,B=\xi\left(I_{0}-1\right)^{\beta-1}+\frac{E}{2}I_{0}^{-1/2}
\]

For this material type, the fiber elasticity at the strain origin reduces to zero unless $\beta=2$. 

_Example:_

```xml
<solid type="fiber-pow-linear">
  <fiber type="angles">
    <theta>20</center>
    <phi>90</phi>
  </fiber>
  <E>1</E>
  <beta>2.5</beta>
  <lam0>1.06</lam0>
</solid>
```
