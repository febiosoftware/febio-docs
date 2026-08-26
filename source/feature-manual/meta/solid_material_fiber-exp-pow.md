The material type for a single fiber family with an exponential-power law is `fiber-exp-pow`. Since fibers can only sustain tension, this material is not stable on its own. It must be combined with a stable compressible material that acts as a ground matrix, using a [solid mixture](solid_material_solid_mixture.md) container.

The fiber is oriented along the unit vector $\mathbf{e}_{1}$, where $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ are orthonormal basis vectors representing the local element coordinate system when specified, or else the global Cartesian coordinate system. The Cauchy stress for this fibrous material is given by

\[
\boldsymbol{\sigma}=H\left(I_{n}-I_{0}\right)\frac{2I_{n}}{J}\frac{\partial\Psi}{\partial I_{n}}\mathbf{n}\otimes\mathbf{n},
\]

where $I_{n}=\lambda_{n}^{2}=\mathbf{n}_{r}\cdot\mathbf{C}\cdot\mathbf{n}_{r}$ is the square of the fiber stretch, $\mathbf{n}=\mathbf{F}\cdot\mathbf{n}_{r}/\lambda_{n}$, $I_{0}=\lambda_{0}^{2}$ is the square of the stretch threshold for the tensile response ($\lambda_{0}=1$ by default) and $H\left(.\right)$ is the unit step function that enforces the tension-only contribution. The fiber strain energy density is given by

\[
\Psi=\frac{\xi}{\alpha\beta}\left(\exp\left[\alpha\left(I_{n}-I_{0}\right)^{\beta}\right]-1\right)\,,
\]

where $\xi>0$, $\alpha\geqslant0$, and $\beta\geqslant2$.

Note: In the limit when $\alpha\to0$, this expressions produces a power law,

\[
\lim\limits_{\alpha\to0}\,\Psi=\frac{\xi}{\beta}\left(I_{n}-I_{0}\right)^{\beta}
\]

Note: When $\beta>2$, the fiber modulus is zero at the strain origin ($I_{n}=I_{0}$). Therefore, use $\beta>2$ when a smooth transition in the stress is desired from compression to tension.

_Example 1:_
Single fiber oriented along $\mathbf{e}_{1}$, embedded in a neo-Hookean ground matrix.
```xml
<material id="1" type="solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="neo-Hookean">
    <E>1000.0</E>
    <v>0.45</v>
  </solid>
  <solid type="fiber-exp-pow">
    <ksi>5</ksi>
    <alpha>20</alpha>
    <beta>3</beta>
    <mat_axis type="angles">
        <theta>0</theta>
        <phi>90</phi>
    </mat_axis>
  </solid>
</material>
```

_Example 2:_

Two fibers in the plane orthogonal to $\mathbf{e}_{1}$, oriented at ±25 degrees relative to $\mathbf{e}_{3}$, embedded in a neo-Hookean ground matrix.

```xml
<material id="1" type="solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="neo-Hookean">
    <E>1000.0</E>
    <v>0.45</v>
  </solid>
  <solid type="fiber-exp-pow">
    <ksi>5</ksi>
    <alpha>20</alpha>
    <beta>3</beta>
    <fiber type="angles">
      <theta>90</theta>
      <phi>25</phi>
    </fiber>
  </solid>
  <solid type="fiber-exp-pow">
    <ksi>5</ksi>
    <alpha>20</alpha>
    <beta>3</beta>
    <fiber type="angles">
      <theta>-90</theta>
      <phi>25</phi>
    </fiber>
  </solid>
</material>
```

