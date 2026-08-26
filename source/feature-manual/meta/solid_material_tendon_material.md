The material type for the tendon material is tendon material. The tendon material is similar to the muscle material [^1] (also see [muscle material](solid_material_muscle_material.md)). The only difference is the fiber function. For tendon material this is defined as:

\[
\lambda\frac{\partial F_{t}}{\partial\lambda}=\sigma\left(\lambda\right),
\]

where

\[
\sigma\left(\lambda\right)=\begin{cases}
0 & \lambda\leqslant1\\
L_{1}\left(e^{L_{2}\left(\lambda-1\right)}-1\right) & 1<\lambda<\lambda^{\ast}\\
L_{3}\lambda+L_{4} & \lambda\geqslant\lambda^{\ast}
\end{cases}\,.
\]

The parameters $L_{3}$ and $L_{4}$ are determined by requiring $C^{0}$ and $C^{1}$ continuity at $\lambda^{\ast}$.

The tendon fiber direction is specified similarly to the transversely isotropic Mooney-Rivlin model.

_Example:_
```xml
<material id="1" type="tendon material">
  <g1>5e4</g1>
  <g2>5e4</g2>
  <l1>2.7e6/l1>
  <l2>46.4</l2>
  <lambda>1.03</lambda>
  <k>1e7</k>
  <fiber type="vector">1,0,0</fiber>
</material>
```

[^1]: Blemker, SS, 3D Modeling of Complex Muscle Architecture and Geometry (2004).
