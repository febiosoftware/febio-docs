The material type for for a constrained mixture of uncoupled solids is `uncoupled solid mixture`. This material describes a mixture of quasi-incompressible elastic solids. It is a container for any combination of the uncoupled materials.

The mixture may consist of any number of solids. The stress tensor for the solid mixture is the sum of the stresses for all the solids.

Material axes may be optionally specified within the `material` level. If the `solid` also defines material axes, they are properly compounded to produce local material axes relative to the global coordinate system. Material axes specified in the `ElementData` section are equivalent to a specification at the `material` level: they correspond to local element axes relative to the global system.

_Example:_
```xml
<material id="1" type="uncoupled solid mixture">
  <k>30e3</k>
  <mat_axis type="vector">
    <a>1,0,0</a>
    <d>0,1,0</d>
  </mat_axis>
  <solid type="Mooney-Rivlin">
    <c1>2.0</c1>
    <c2>0.0</c2>
  </solid>
  <solid type="EFD uncoupled">
    <mat_axis type="vector">
      <a>0.8660254,0.5,0</a>
      <d>0,0,1</d>
    </mat_axis>
    <ksi>5, 1, 1</ksi>
    <beta>2.5, 3, 3</beta>
  </solid>
  <solid type="EFD uncoupled">
    <mat_axis type="vector">
      <a>0.8660254,-0.5,0</a>
      <d>0,0,1</d>
    </mat_axis>
    <ksi>5, 1, 1</ksi>
    <beta>2.5, 3, 3</beta>
  </solid>
</material>
```