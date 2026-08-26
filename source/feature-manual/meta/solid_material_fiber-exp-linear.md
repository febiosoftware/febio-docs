This material type is `fiber-exp-linear`. This constitutive fiber model has an initial exponential rise and then grows linearly after a user-specified stretch transition point. This fiber material is based on the trans-iso Mooney-Rivlin model introduced in [^1]. This material by itself is not stable, so it is recommend to use it as part of a solid mixture. 

The strain energy is as follows:

\[
F_{2}\left(\lambda\right)=\begin{cases}
0 & \lambda<1\\
C_{3}\left(e^{-C_{4}}\left(\text{Ei}\left(C_{4}\lambda\right)-\text{Ei}\left(C_{4}\right)\right)-\ln\lambda\right) & 1\le\lambda<\lambda_{m}\\
C_{5}\left(\lambda-\lambda_{m}\right)+C_{6}\ln\frac{\lambda}{\lambda_{m}}+C_{3}\left(e^{-C_{4}}\text{Ei}\left(C_{4}\lambda_{m}\right)-\text{Ei}\left(C_{4}\right)-\ln\lambda_{m}\right) & \lambda_{m}\le\lambda
\end{cases}\,
\]

where $\text{Ei}\left(\cdot\right)$ is the exponential integral function. The resulting fiber stress is evaluated from

\[
\lambda\frac{\partial F_{2}}{\partial\lambda}=\begin{cases}
0 & \tilde{\lambda}\leqslant1\\
C_{3}\left(e^{C_{4}\left(\lambda-1\right)}-1\right) & 1<\tilde{\lambda}<\lambda_{m}\\
C_{5}\lambda+C_{6} & \tilde{\lambda}\geqslant\lambda_{m}
\end{cases}\,.
\]

Here, $\lambda_{m}$ is the stretch at which the fibers are straightened, $C_{3}$ scales the exponential stresses, $C_{4}$ is the rate of uncrimping of the fibers, and $C_{5}$ is the modulus of the straightened fibers. $C_{6}$ is determined from the requirement that the stress is continuous at $\lambda_{m}$ (see below).

While this material enforces continuity of the strain energy density and stress at $\lambda_{m}$, it does not guarantee continuity of the elasticity. The continuity of the elasticity is only satisfied if the parameter $C_{3}$ satisfies

\[
C_{3}=\frac{C_{5}}{C_{4}}e^{-C_{4}\left(\lambda_{m}-1\right)}
\]

The parameter $C_{6}$ is chosen so that the stress defined above is continuous $\lambda_{m}$ and is determined by,

\[
C_{6}=C_{3}\left(e^{C_{4}\left(\lambda_{m}-1\right)}-1\right)-C_{5}\lambda_{m}
\]

To use the form of $F_{2}$ that satisfies continuity of the elasticity at $\lambda_{m}$ the user may set $C_{3}=0$ in the input file, and specify $C_{4}$ and $C_{5}$ as explained above. When $C_{3}=0$ the code will automatically recalculate $C_{3}$ internally using the formula above.

_Example:_
```xml
<material id="1" name="Material" type="solid mixture">
  <solid type="neo-Hookean">
    <E>1e-6</E>
    <v>0</v>
  </solid>
  <solid type="fiber-exp-linear">
    <c3>0.0023</c3>
    <c4>43</c4>
    <c5>3</c5>
    <lambda>1.05</lambda>
    <fiber type="vector">1,0,0</fiber>
  </solid>
</material>
```

[^1]: Weiss, J.A., Maker, B.N., and Govindjee, S., "Finite element implementation of incompressible, transversely isotropic hyperelasticity", Computer Methods in Applications of Mechanics and Engineering 135 (1996), pp. 107-128