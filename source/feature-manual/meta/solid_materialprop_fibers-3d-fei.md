The scheme type for the finite element integration rule is `fibers-3d-fei` for unconstrained and uncoupled continuous fiber distributions. This integration rule should only be used with 3D fiber density distributions. This scheme discretizes the unit sphere into a set of N spherical triangles of nearly identical surface areas. The unit normal $\mathbf{n}$ passes through the centroid of each surface element. The integration is performed as a summation over N. For each direction $\mathbf{n}$ the stress is evaluated only if the fiber bundle is in tension along that direction.

The parameter `resolution` must be one of the values 20, 34, 60, 74, 196, 210, 396, 410, 596, 610, 796, 810, 996, 1010, 1196, 1210, 1396, 1410, 1596, 1610, and 1796. A conservative choice for producing accurate results under general loading conditions is N=1610. Increasing values of N require increasing computational time.

![FigFiniteElementIntegration.png](figs/FigFiniteElementIntegration.png)
/// figure-caption
Illustration of the `fibers-3d-fei` integration scheme.
///

_Example:_
```xml
<scheme type="fibers-3d-fei">
  <resolution>1610</resolution>
</scheme>
```
