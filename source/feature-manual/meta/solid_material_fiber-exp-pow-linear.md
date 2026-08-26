This material type is `fiber-exp-pow-linear`.

The fiber strain energy density is given by

\[
\Psi_{n}=\begin{cases}
0 & I_{n}<1\\
\frac{\xi}{\alpha\beta}\left(\exp\left[\alpha\left(I_{n}-1\right)^{\beta}\right]-1\right) & 1\le I_{n}\le I_{0}\\
B\left(I_{n}-I_{0}\right)-E\left(I_{n}^{1/2}-I_{0}^{1/2}\right)+\frac{\xi}{\alpha\beta}\left(\exp\left[\alpha\left(I_{0}-1\right)^{\beta}\right]-1\right) & I_{n}>I_{0}
\end{cases}
\]

where $I_{0}=\lambda_{0}^{2}$,

\[
\xi=\frac{E\left(I_{0}-1\right)^{2-\beta}\exp\left[-\alpha\left(I_{0}-1\right)^{\beta}\right]}{4I_{0}^{3/2}\left(\beta-1+\alpha\beta\left(I_{0}-1\right)^{\beta}\right)}
\]

and

\[
B=E\frac{2I_{0}\left(\beta-\frac{1}{2}+\alpha\beta\left(I_{0}-1\right)^{\beta}\right)-1}{4I_{0}^{3/2}\left(\beta-1+\alpha\beta\left(I_{0}-1\right)^{\beta}\right)}
\]

For this material type, the fiber elasticity at the strain origin reduces to zero unless $\beta=2$. This model reduces to \fiber-pow-linear\ when $\alpha=0$. Alternatively, in the limit when $I_{0}=1$, the above parameters reduce to $\xi=0$ and $B=E/2$ and the strain energy density takes the quadratic form 

\[
\Psi_{n}=\begin{cases}
0 & I_{n}<1\\
\frac{E}{2}\left(I_{n}^{1/2}-1\right)^{2} & I_{n}>1
\end{cases}
\]

where $I_{n}^{1/2}=\lambda_{n}$ is the stretch ratio along the fiber.

_Example:_
```xml
<solid type="fiber-exp-pow-linear">
 <E>1080</E>
 <alpha>1400</alpha>
 <beta>2.73</beta>
 <lam0>1.012</lam0>
 <fiber type="vector">0,0,1</fiber>
</solid>
```
