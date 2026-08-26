The material type for a conewise linear elastic (CLE) material with orthtropic symmetry is `orthotropic CLE`.

This bimodular elastic material is the orthotropic conewise linear elastic material described by Curnier et al. [^1]. It is derived from the following hyperelastic strain-energy function:

\[
\Psi_{r}=\sum\limits_{a=1}^{3}\mu_{a}\mathbf{A}_{a}^{r}:\mathbf{E}^{2}+\frac{1}{2}\lambda_{aa}\left[\mathbf{A}_{a}^{r}:\mathbf{E}\right]\left(\mathbf{A}_{a}^{r}:\mathbf{E}\right)^{2}+\sum\limits_{\begin{array}{c}
b=1\\
b\ne a
\end{array}}^{3}\frac{1}{2}\lambda_{ab}\left(\mathbf{A}_{a}^{r}:\mathbf{E}\right)\left(\mathbf{A}_{b}^{r}:\mathbf{E}\right)
\]

where $\lambda_{ba}=\lambda_{ab}$ and

\[
\lambda_{aa}\left[\mathbf{A}_{a}^{r}:\mathbf{E}\right]=\begin{cases}
\lambda_{+aa} & \mathbf{A}_{a}^{r}:\mathbf{E}\geqslant0\\
\lambda_{-aa} & \mathbf{A}_{a}^{r}:\mathbf{E}<0
\end{cases},\quad a=1,2,3
\]

Here, $\mathbf{E}$ is the Lagrangian strain tensor and $\mathbf{A}_{a}^{r}=\mathbf{a}_{a}^{r}\otimes\mathbf{a}_{a}^{r}$, where $\mathbf{a}_{a}^{r} (a=1,2,3)$ are orthonormal vectors aligned with the material axes. This material response was originally formulated for infinitesimal strain analyses; its behavior under finite strains may not be physically realistic.

_Example:_
```xml
<material id="1" type=" orthotropic CLE">
  <density>1</density>
  <lp11>13.01</lp11>
  <lp22>13.01</lp22>
  <lp33>13.01</lp33>
  <lm11>0.49</lm11>
  <lm22>0.49</lm22>
  <lm33>0.49</lm33>
  <l12>0.66</l12>
  <l23>0.66</l23>
  <l31>0.66</l31>
  <mu1>0.16</mu1>
  <mu2>0.16</mu2>
  <mu3>0.16</mu3>
</material>
```

[^1]: Curnier, A., Qi-Chang, He, and Zysset, P., "Conewise linear elastic materials", J Elasticity 37, 1 (1994), pp. 1-38.