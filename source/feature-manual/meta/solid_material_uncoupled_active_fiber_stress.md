An active fiber stress, based on a Hill formulation, can be added via the material `uncoupled active fiber stress`. This material must be combined with a stable compressible material that acts as a passive matrix, using a `uncoupled solid mixture` container as described in  [uncoupled solid mixture](solid_material_uncoupled_solid_mixture.md). The stress is given by,

\[
\boldsymbol{\sigma}^{a}=J^{-1}T\left(\tilde{\lambda}\right)\mathbf{\mathrm{dev}A}.
\]

Here, $\mathbf{A=a\otimes a}$,with a the unit vector describing the fiber direction in the spatial frame, $\tilde{\lambda}$ is the deviatoric fiber stretch, $J$ is the jacobian of the deformation, and

\[
T\left(\tilde{\lambda}\right)=s_{max}a\left(t\right)s_{TL}\left(\tilde{\lambda}\right)s_{TV}\left(\dot{\tilde{\lambda}}\right)
\]

The parameters $s_{TL}$ and $s_{TV}$ are functions that need to be defined in place. There are currently two ways of defining these functions, either via a mathematical expression or a list of sample points. An example is given below. If these parameters are omitted, they are replaced by the constant $1$ in the equation for the stress above. 

_Example 1:_

An example defining the stl parameter via a mathematical expression.
```xml
<material id="1" type="uncoupled solid mixture">
  <k>100.0</k>
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="Mooney-Rivlin">
    <c1>1.0</c1>
    <c2>0</c2>
  </solid>
  <solid type="uncoupled active fiber stress">
    <smax>1.5</smax>
    <a lc="1">0.1</a>
    <stl type="math">
      <math>(l-1)^2</math>
    </stl>
  </solid>
</material>
```

_Example 2:_

An example defining the stl parameter via a point list.

```xml
<material id="1" type="uncoupled solid mixture">
  <k>100.0</k>
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="Mooney-Rivlin">
    <c1>1.0</c1>
    <c2>0</c2>
  </solid>
  <solid type="uncoupled active fiber stress">
    <smax>1.5</smax>
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
