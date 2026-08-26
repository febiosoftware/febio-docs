This material model implements the constitutive model developed by Silvia S. Blemker [^1]. The material type for the muscle material is muscle material. The model is designed to simulate the passive and active material behavior of skeletal muscle.

The main difference between this material formulation compared to other transversely hyperelastic materials is that it is formulated using a set of new invariants, originally due to Criscione [^2], instead of the usual five invariants proposed by A.J.M. Spencer [^3]. For this particular material, only two of the five Criscione invariants are used. The strain energy function is defined as follows:

\[
\Psi\left(B_{1},B_{2},\lambda\right)=G_{1}\tilde{B}_{1}^{2}+G_{2}\tilde{B}_{2}^{2}+F_{m}\left(\tilde{\lambda}\right)+U\left(J\right).
\]

The function $F_{m}$ is the strain energy contribution of the muscle fibers. It is defined as follows:

\[
\lambda\frac{\partial F_{m}}{\partial\lambda}=\sigma_{\max}\left(f_{m}^{\text{passive}}\left(\lambda\right)+\alpha f_{m}^{\text{active}}\left(\lambda\right)\right)\frac{\lambda}{\lambda_{ofl}},
\]

where,

\[
f_{m}^{\text{passive}}\left(\lambda\right)=\begin{cases}
0 & \lambda\leqslant\lambda_{ofl}\\
P_{1}\left(e^{P_{2}\left(\lambda/\lambda_{ofl}-1\right)}-1\right) & \lambda_{ofl}<\lambda<\lambda^{\ast}\\
P_{3}\lambda/\lambda_{ofl}+P_{4} & \lambda\geqslant\lambda^{\ast}
\end{cases}\,,
\]

and

\[
f_{m}^{\text{active}}\left(\lambda\right)=\begin{cases}
9\left(\lambda/\lambda_{ofl}-0.4\right)^{2} & \lambda\leqslant0.6\lambda_{ofl}\\
9\left(\lambda/\lambda_{ofl}-1.6\right)^{2} & \lambda\geqslant1.4\lambda_{ofl}\\
1-4\left(1-\lambda/\lambda_{ofl}\right)^{2} & 0.6\lambda_{ofl}<\lambda<1.4\lambda_{ofl}
\end{cases}\,.
\]

The values $P_{3}$ and $P_{4}$ are determined by requiring $C^{0}$ and $C^{1}$ continuity at $\lambda=\lambda^{\ast}$.

The parameter $\alpha$ is the activation level and can be specified using the activation element. You can specify a loadcurve using the lc attribute. The value is interpreted as a scale factor when a loadcurve is defined or as the constant activation level when no loadcurve is defined.

The muscle fiber direction is specified similarly to the transversely isotropic Mooney-Rivlin model.

_Example:_
```xml
<material id="1" type="muscle material">
  <g1>500</g1>
  <g2>500</g2>
  <p1>0.05</p1>
  <p2>6.6</p2>
  <smax>3e5</smax>
  <Lofl>1.07</Lofl>
  <lambda>1.4</lambda>
  <k>1e6</k>
  <fiber type="vector">1,0,0</fiber>
</material>
```

[^1]: Blemker, SS, 3D Modeling of Complex Muscle Architecture and Geometry (2004).

[^2]: Criscione, JC, Douglas, SA, and Hunter, WC, "Physically based strain invariant set for materials exhibiting transversely isotropic behavior", J. Mech. Phys. Solids 49 (2001), pp. 871-897.

[^3]: Spencer, Anthony James Merril, Continuum Theory of the Mechanics of Fibre-Reinforced Composites (New York: Springer-Verlag, 1984).