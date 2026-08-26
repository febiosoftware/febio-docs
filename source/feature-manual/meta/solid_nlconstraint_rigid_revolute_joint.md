The rigid revolute joint connector allows the user to connect two rigid bodies $a$ and $b$ at a point in space and allow rotation about a single prescribed axis.

The `tolerance` parameter defines the augmentation tolerance. That is, when the relative change in the constraint forces and moments (the Lagrange multipliers) are less than this value. The `gaptol` parameter defines the tolerance for spatial separation of the joint origin on the two bodies (in units of length). The `angtol` parameter defines the tolerance for angular separation of the joint axis on the two bodies (in units of radians). Setting any of these three elements to zero disables the enforcement of that tolerance. The `force_penalty` parameter (with units of force per length) represents the stiffness that prevents the joint origin on the two bodies from separating. The `moment_penalty` parameter (with units of moment per radians) represents the torsional stiffness that enforces parallelism of the joint axis on the two bodies. The `body_a` and `body_b` parameters are the material numbers of the two rigid bodies. The `joint_origin` parameter defines the position of the joint origin (the origin of the basis $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$) in world coordinates at the start of the analysis. Note that this point does not have to be inside or on the surface of either of the two bodies. The `rotation_axis` parameter defines the orientation of the joint rotation axis $\mathbf{e}_{1}$ in world coordinates at the start of the analysis.

Optionally, the rotation of body b relative to body a may be prescribed using the additional tags

```
<prescribed_rotation>1</prescribed_rotation>
<rotation lc="1">3.14159</rotation>
```

The `prescribed_rotation` parameter is a flag that indicates that the motion of the joint is prescribed (1 for prescribed, 0 for free). The `rotation` parameter specifies the amount of rotation (with units of radians) with an optional associated load curve.

Optionally, a moment may be prescribed on body b relative to body a, about the joint axis, using the additional tag

```
<moment lc="1">5.e-3</moment>
```

The `moment` parameter specifies the magnitude of the moment, with an optional associated load controller. The `moment` parameter should not be used simultaneously with a prescribed rotation.

_Example:_
```xml
<rigid_connector type="rigid revolute joint" name="Joint 1">
  <tolerance>0</tolerance>
  <gaptol>1e-4</gaptol>
  <angtol>1e-4</angtol>
  <force_penalty>1e0</force_penalty>
  <moment_penalty>1e0</moment_penalty>
  <auto_penalty>1</auto_penalty>
  <body_a>1</body_a>
  <body_b>3</body_b>
  <joint_origin>-150,0,2</joint_origin>
  <rotation_axis>0,0,1</rotation_axis>
</rigid_connector>
```