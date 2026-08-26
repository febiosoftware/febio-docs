A rigid planar joint connects rigid bodies $a$ and $b$, allowing one degree of freedom for rotation about the axis $\mathbf{e}_{1}$ through that point, and two degrees of freedom for translations in the plane perpendicular to that axis, along $\mathbf{e}_{2}^{a}$ and $\mathbf{e}_{3}^{a}$.

The `tolerance` parameter defines the augmentation tolerance. That is, when the relative change in the constraint forces and moments (the Lagrange multipliers) are less than this value. The `gaptol` parameter defines the tolerance for spatial separation of the joint origin on the two bodies (in units of length). The `angtol` parameter defines the tolerance for angular separation of the joint axes on the two bodies (in units of radians). Setting any of these three elements to zero disables the enforcement of that tolerance. The `force_penalty` parameter (with units of force per length) represents the stiffness that prevents the joint origin on the two bodies from separating along the rotation axis. The `moment_penalty` parameter (with units of moment per radians) represents the torsional stiffness that enforces parallelism of the joint rotation axis on the two bodies. The `body_a` and `body_b` elements are the material numbers of the two rigid bodies. The joint_origin element defines the position of the joint (the origin of the basis $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ ) in world coordinates at the start of the analysis. Note that this point does not have to be inside or on the surface of either of the two bodies. The `rotation_axis` parameter defines the orientation of the joint rotation axis $\mathbf{e}_{1}$ in world coordinates at the start of the analysis. The `translation_axis_1` element defines the orientation of the joint translation axis $\mathbf{e}_{2}^{a}$ in the plane perpendicular to the joint rotation axis, in world coordinates at the start of the analysis.

Optionally, the rotation of body b relative to body a may be prescribed using the additional tags

```
<prescribed_rotation>1</prescribed_rotation>
<rotation lc="1">1.570796327</rotation>
```

The `prescribed_rotation` parameter is a flag that indicates that the motion of the joint is prescribed (1 for prescribed, 0 for free). The `rotation` element specifies the amount of rotation (with units of radians) with an optional associated load curve.

Optionally, the translation of body b relative to body a may be prescribed along $\mathbf{e}_{2}^{a}$ using the additional tags

```
<prescribed_translation_1>1</prescribed_translation_1>
<translation_1 lc="2">10.0</translation_1>
```

Optionally, the translation of body b relative to body a may be prescribed along $\mathbf{e}_{3}^{a}$ using the additional tags

```
<prescribed_translation_2>1</prescribed_translation_2>
<translation_2 lc="2">10.0</translation_2>
```

_Example:_
```xml
<rigid_connector type="rigid planar joint" name="Joint01">
  <tolerance>0</tolerance>
  <gaptol>1e-4</gaptol>
  <angtol>1e-4</angtol>
  <force_penalty>1e0</force_penalty>
  <moment_penalty>1e0</moment_penalty>
  <auto_penalty>1</auto_penalty>
  <body_a>1</body_a>
  <body_b>2</body_b>
  <joint_origin>0,0,0</joint_origin>
  <rotation_axis>0,-0.5,0.8660254</rotation_axis>
  <translation_axis_1>1,0,0</translation_axis_1>
</rigid_connector>
```