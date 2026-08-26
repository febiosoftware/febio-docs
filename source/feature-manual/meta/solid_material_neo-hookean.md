This model describes an unconstrained Neo-Hookean material [^1]. It has a non-linear stress-strain behavior, but reduces to the classical linear elasticity model for small strains and small rotations. It is derived from the following hyperelastic strain-energy function: 

\[
\begin{equation}
W=\frac{\mu}{2}\left(I_{1}-3\right)-\mu\ln J+\frac{\lambda}{2}\left(\ln J\right)^{2}.
\end{equation}
\]

Here, $I_{1}$ and $I_{2}$ are the first and second invariants of the right Cauchy-Green deformation tensor $\mathbf{C}$ and $J$ is the determinant of the deformation gradient tensor. The relationship between the material parameters, E, and v, and the parameters used in the strain-energy function, is as follows. 

\[
\begin{equation}
\mu=\dfrac{E}{2(1+\nu)},\,
\lambda=\dfrac{\nu E}{(1+\nu)(1-2\nu)}
\end{equation}
\]

This material model uses a standard displacement-based element formulation, so care must be taken when modeling materials with nearly-incompressible material behavior to avoid element locking. For this case, use the Mooney-Rivlin material instead.

_Example_:
```
<material id="1" type="neo-Hookean">
  <E>1000.0</E>
  <v>0.45</v>
</material>
```

[^1]: Bonet, Javier and Wood, Richard D., Nonlinear continuum mechanics for finite element analysis (Cambridge University Press, 1997).
