The material type for a single fiber family with an exponential-power law, in an uncoupled strain energy formulation, is `fiber-exp-pow-uncoupled`. Since fibers can only sustain tension, this material is not stable on its own. It must be combined with a stable uncoupled material that acts as a ground matrix, using a [uncoupled solid mixture](solid_material_uncoupled_solid_mixture.md) container.

The fiber is oriented along the unit vector $\mathbf{e}_{1}, where \left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ are orthonormal basis vectors representing the local element coordinate system when specified, or else the global Cartesian coordinate system. The stress $\tilde{\boldsymbol{\sigma}}$ for this fibrous material is given by

\[
\tilde{\boldsymbol{\sigma}}=H\left(\tilde{I}_{n}-1\right)\frac{2\tilde{I}_{n}}{J}\frac{\partial\tilde{\Psi}}{\partial\tilde{I}_{n}}\mathbf{n}\otimes\mathbf{n},
\]

where $\tilde{I}_{n}=\tilde{\lambda}_{n}^{2}=\mathbf{n}_{r}\cdot\mathbf{\tilde{C}}\cdot\mathbf{n}_{r}$ is the square of the fiber stretch, $\mathbf{n}=\mathbf{\tilde{F}}\cdot\mathbf{n}_{r}/\tilde{\lambda}_{n}$, and $H\left(.\right)$ is the unit step function that enforces the tension-only contribution. The fiber strain energy density is given by

\[
\tilde{\Psi}=\frac{\xi}{\alpha\beta}\left(\exp\left[\alpha\left(\tilde{I}_{n}-1\right)^{\beta}\right]-1\right)\,,
\]

where $\xi>0$, $\alpha\geqslant0$, and $\beta\geqslant2$.

Note: In the limit when $\alpha\to0$, this expressions produces a power law,

\[
\lim\limits_{\alpha\to0}\tilde{\Psi}=\frac{\xi}{\beta}\left(\tilde{I}_{n}-1\right)^{\beta}.
\]

Note: When $\beta>2$, the fiber modulus is zero at the strain origin ($\tilde{I}_{n}=1$). Therefore, use $\beta>2$ when a smooth transition in the stress is desired from compression to tension.

_Example 1:_

Single fiber oriented along $\mathbf{e}_{1}$, embedded in a Mooney-Rivlin ground matrix.

```xml
<material id="1" type="uncoupled solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <k>10e3</k>
  <solid type="Mooney-Rivlin">
    <c1>10.0</c1>
    <c2>0</c2>
  </solid>
  <solid type="fiber-exp-pow-uncoupled">
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

Two fibers in the plane orthogonal to $\mathbf{e}_{1}$, oriented at ±25 degrees relative to $\mathbf{e}_{3}$, embedded in a Mooney-Rivlin ground matrix.

```xml
<material id="1" type="uncoupled solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <k>10e3</k>
  <solid type="Mooney-Rivlin">
    <c1>10.0</c1>
    <c2>0</c2>
  </solid>
  <solid type="fiber-exp-pow-uncoupled">
    <ksi>5</ksi>
    <alpha>20</alpha>
    <beta>3</beta>
    <mat_axis type="angles">
        <theta>90</theta>
        <phi>25</phi>
    </mat_axis>
  </solid>
  <solid type="fiber-exp-pow-uncoupled">
    <ksi>5</ksi>
    <alpha>20</alpha>
    <beta>3</beta>
    <mat_axis type="angles">
        <theta>-90</theta>
        <phi>25</phi>
    </mat_axis>
  </solid>
</material>
```

