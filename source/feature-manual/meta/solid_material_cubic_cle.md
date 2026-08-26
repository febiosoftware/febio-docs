The material type for a conewise linear elastic (CLE) material with cubic symmetry is `cubic CLE`.

This bimodular elastic material is specialized from the orthotropic conewise linear elastic material described by Curnier et al. [^1], to the case of cubic symmetry. It is derived from the following hyperelastic strain-energy function:

\[
\Psi_{r}=\mu\mathbf{I}:\mathbf{E}^{2}+\sum\limits_{a=1}^{3}\frac{1}{2}\lambda_{1}\left[\mathbf{A}_{a}^{r}:\mathbf{E}\right]\left(\mathbf{A}_{a}^{r}:\mathbf{E}\right)^{2}+\frac{1}{2}\lambda_{2}\sum\limits_{\begin{array}{c}
b=1\\
b\ne a
\end{array}}^{3}\left(\mathbf{A}_{a}^{r}:\mathbf{E}\right)\left(\mathbf{A}_{b}^{r}:\mathbf{E}\right)\,,
\]

where

\[
\lambda_{1}\left[\mathbf{A}_{a}^{r}:\mathbf{E}\right]=\begin{cases}
\lambda_{+1} & \mathbf{A}_{a}^{r}:\mathbf{E}\geqslant0\\
\lambda_{-1} & \mathbf{A}_{a}^{r}:\mathbf{\,}.E<0
\end{cases}
\]

Here, $\mathbf{E}$ is the Lagrangian strain tensor and $\mathbf{A}_{a}^{r}=\mathbf{a}_{a}^{r}\otimes\mathbf{a}_{a}^{r}$, where $\mathbf{a}_{a}^{r} (a=1,2,3)$ are orthonormal vectors aligned with the material axes. This material response was originally formulated for infinitesimal strain analyses; its behavior under finite strains may not be physically realistic.

_Example:_
```xml
<material id="1" type="cubic CLE">
  <density>1</density>
  <lp1>13.01</lp1>
  <lm1>0.49</lm1>
  <l2>0.66</l2>
  <mu>0.16</mu>
</material>
```

[^1]: Curnier, A., Qi-Chang, He, and Zysset, P., "Conewise linear elastic materials", J Elasticity 37, 1 (1994), pp. 1-38.