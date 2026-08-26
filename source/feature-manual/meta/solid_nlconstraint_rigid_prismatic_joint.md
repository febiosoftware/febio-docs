The `rigid prismatic joint` connector allows the user to connect two rigid bodies $a$ and $b$ at a point in space and allow translation along a single prescribed axis.

The `tolerance` parameter defines the augmentation tolerance. That is, when the relative change in the constraint forces and moments (the Lagrange multipliers) are less than this value. The `gaptol` parameter defines the tolerance for spatial separation of the joint origin on the two bodies (in units of length). The `angtol` parameter defines the tolerance for angular separation of the joint axis on the two bodies (in units of radians). Setting any of these three elements to zero disables the enforcement of that tolerance. The `force_penalty` parameter (with units of force per length) represents the stiffness that prevents the joint origin on the two bodies from separating. The `moment_penalty` parameter (with units of moment per radians) represents the torsional stiffness that enforces parallelism of the joint axis on the two bodies. The `body_a` and `body_b` elements are the material numbers of the two rigid bodies. The `joint_origin` parameter defines the position of the joint (the origin of the basis $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ ) in world coordinates at the start of the analysis. Note that this point does not have to be inside or on the surface of either of the two bodies. The translation_axis element defines the orientation $\mathbf{e}_{1}$ of the joint translation axis in world coordinates at the start of the analysis.

Optionally, the translation of body b relative to body a may be prescribed using the additional tags

```
<prescribed_translation>1</prescribed_translation>
<translation lc="1">5.0</translation>
```

The `prescribed_translation` parameter is a flag that indicates that the motion of the joint is prescribed (1 for prescribed, 0 for free). The `translation` parameter specifies the amount of translation (with units of length) with an optional associated load curve.

Optionally, a force may be prescribed on body b relative to body a, along the joint axis using the additional tag

```
<force lc="1">5.e-3</force>
```

The `force` element specifies the magnitude of the force, with an optional associated load curve. The `force` element should not be used simultaneously with a prescribed translation.

_Example:_
```xml
<rigid_connector type="rigid prismatic joint" name="Joint02 ">
  <tolerance>0</tolerance>
  <gaptol>1e-4</gaptol>
  <angtol>1e-4</angtol>
  <force_penalty>1e0</force_penalty>
  <moment_penalty>1e0</moment_penalty>
  <auto_penalty>1</auto_penalty>
  <body_a>4</body_a>
  <body_b>1</body_b>
  <joint_origin>-150,0,2</joint_origin>
  <translation_axis>1,0,0</translation_axis>
  <prescribed_translation>150</prescribed_translation>
  <translation lc="1">1</translation>
</rigid_connector>
```