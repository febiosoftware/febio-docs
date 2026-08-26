The material type for the Holmes-Mow material [^1] is `Holmes-Mow`. This isotropic hyperelastic material has been used to represent the solid matrix of articular cartilage [^1][^2] and intervertebral disc [^3].

The coupled hyperelastic strain-energy function for this material is given by [^1]:

\[
W\left(I_{1},I_{2},J\right)=\frac{1}{2}c\left(e^{Q}-1\right),
\]

where $I_{1}$ and $I_{2}$ are the first and second invariants of the right Cauchy-Green tensor and Jis the jacobian of the deformation gradient. 

Furthermore,

\[
\begin{aligned}Q & =\frac{\beta}{\lambda+2\mu}\left[\left(2\mu-\lambda\right)\left(I_{1}-3\right)+\lambda\left(I_{2}-3\right)-\left(\lambda+2\mu\right)\ln J^{2}\right]\\
c & =\frac{\lambda+2\mu}{2\beta}
\end{aligned}
\,,
\]

and $\lambda$ and $\mu$ are the Lamé parameters which are related to the more familiar Young's modulus and Poisson's ratio in the usual manner:

\[
\begin{aligned}\lambda & =\frac{E\nu}{\left(1+\nu\right)\left(1-2\nu\right)}\\
\mu & =\frac{E}{2\left(1+\nu\right)}
\end{aligned}
\,.
\]

_Example:_
```xml
<material id="3" type="Holmes-Mow">
  <E>1</E>
  <v>0.35</v>
  <beta>0.25</beta>
</material>
```


[^1]: Holmes, M. H. and Mow, V. C., "The nonlinear characteristics of soft gels and hydrated connective tissues in ultrafiltration", J Biomech 23, 11 (1990), pp. 1145-56.

[^2]: Ateshian, G. A., Warden, W. H., Kim, J. J., Grelsamer, R. P., and Mow, V. C., "Finite deformation biphasic material properties of bovine articular cartilage from confined compression experiments", J Biomech 30, 11-12 (1997), pp. 1157-64.

[^3]: Iatridis, J. C., Setton, L. A., Foster, R. J., Rawlins, B. A., Weidenbaum, M., and Mow, V. C., "Degeneration affects the anisotropic and nonlinear behaviors of human anulus fibrosus in compression", J Biomech 31, 6 (1998), pp. 535-44.