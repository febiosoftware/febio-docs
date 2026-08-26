An active fiber stress, based on a Hill formulation, can be added via the material `active fiber stress`. This material must be combined with a stable compressible material that acts as a passive matrix, using a [solid mixture](solid_material_solid_mixture.md) container. The stress is given by,

\[
\boldsymbol{\sigma}^{a}=J^{-1}T\left(\lambda\right)\mathbf{A}.
\]

Here, $\mathbf{A=a\otimes a}$, with a the unit vector describing the fiber direction in the spatial frame, $\lambda$ is the fiber stretch, $J$ is the jacobian of the deformation, and

\[
T\left(\lambda\right)=s_{max}a\left(t\right)s_{TL}\left(\lambda\right)s_{TV}\left(\dot{\lambda}\right)
\]

The parameters `stl` and `stv` are functions that need to be defined in place. There are currently two ways of defining these functions, either via a mathematical expression or a list of sample points. An example is given below. If these parameters are omitted, they are replaced by the constant $1$ in the equation for the stress above. 

_Example 1:_

An example defining the `stl` parameter via a mathematical expression.

```xml
<material id="1" type="solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="neo-Hookean">
    <E>1.0</E>
    <v>0</v>
  </solid>
  <solid type="active fiber stress">
    <smax>150</smax>
    <a lc="1">0.1</a>
    <stl type="math">
      <math>(l-1)^2</math>
    </stl>
  </solid>
</material>
```

_Example 2:_

An example defining the `stl` parameter via a point list.

```xml
<material id="1" type="solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="neo-Hookean">
    <E>1.0</E>
    <v>0</v>
  </solid>
  <solid type="active fiber stress">
    <smax>150</smax>
    <a lc="1">0.1</a>
    <stl type="point">
      <interpolate>linear</interpolate>
      <points>
        <pt>0,0</pt>
        <pt>1,0</pt>
        <pt>2,1</pt>
      </points>
    </stl>
  </solid>
</material>
```
