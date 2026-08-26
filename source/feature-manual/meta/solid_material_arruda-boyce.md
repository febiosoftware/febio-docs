This material describes an incompressible Arruda-Boyce model [^1].

The uncoupled strain energy function for the Arruda-Boyce material is given by:

\[
\Psi=\mu\sum\limits_{i=1}^{5}\frac{C_{i}}{N^{i-1}}\left(\tilde{I}_{1}^{i}-3^{i}\right)+U\left(J\right),
\]

where, $C_{1}=\frac{1}{2}$, $C_{2}=\frac{1}{20}$, $C_{3}=\frac{11}{1050}$, $C_{4}=\frac{19}{7000}$, $C_{5}=\frac{519}{673750}$ and $I_{1}$ the first invariant of the right Cauchy-Green tensor. The volumetric strain function $U$ is defined as follows,

\[
U\left(J\right)=\frac{1}{2}k\left(\ln J\right)^{2}\,.
\]

This material model was proposed by Arruda and Boyce [^1] and is based on an eight-chain representation of the macromolecular network structure of polymer chains. The strain energy form represents a truncated Taylor series of the inverse Langevin function, which arises in the statistical treatment of non-Gaussian chains. The parameter $N$ is related to the locking stretch $\lambda_{L}$, the stretch at which the chains reach their full extended state, $by \lambda_{L}=\sqrt{N}$.

_Example:_
```xml
<material id="1" type="Arruda-Boyce">
  <mu>0.09</mu>
  <N>26.5</N>
  <k>100</k>
</material>
```

[^1]: Arruda, E.M. and Boyce, M.C., "A Three-Dimensional Constitutive Model for the Large Stretch Behavior of Rubber Elastic Materials", J. Mech. Phys. Solids 41, 2 (1993), pp. 389-412.