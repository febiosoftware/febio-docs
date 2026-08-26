A rigid spherical joint connects rigid bodies $a$ and $b$ at a point in space, allowing three degrees of freedom for rotation about that point.

The `tolerance` parameter defines the augmentation tolerance. That is, when the relative change in the constraint forces and moments (the Lagrange multipliers) are less than this value. The `gaptol` parameter defines the tolerance for spatial separation of the joint origin on the two bodies (in units of length). Setting either of these elements to zero disables the enforcement of that tolerance. The `force_penalty` parameter (with units of force per length) represents the stiffness that prevents the joint origin on the two bodies from separating. The `body_a` and `body_b` parameters are the material numbers of the two rigid bodies. The `joint_origin` parameter defines the position of the joint (the origin of the basis $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$) in world coordinates at the start of the analysis. Note that this point does not have to be inside or on the surface of either of the two bodies. The rotation_axis element defines the orientation of the joint rotation axis in world coordinates at the start of the analysis.

Optionally, the rotation of body b relative to body a may be prescribed using the additional tags.

```
<moment_penalty>1e0</moment_penalty>
<prescribed_rotation>1</prescribed_rotation>
<rotation_x lc="1">1</rotation_x>
<rotation_y lc="2">1</rotation_y>
<rotation_z>0</rotation_z>
```

The `prescribed_rotation` parameter is a flag that indicates that the motion of the joint is prescribed (1 for prescribed, 0 for free). The `rotation_x`, `rotation_y` and `rotation_z` parameters specify the components $\left(\theta_{1},\theta_{2},\theta_{3}\right)$ of rotation (with units of radians), with optional associated load curves. The rotation occurs about the axis directed along $\theta_{1}\mathbf{e}_{1}^{a}+\theta_{2}\mathbf{e}_{2}^{a}+\theta_{3}\mathbf{e}_{3}^{a}$, with a magnitude $\sqrt{\theta_{1}^{2}+\theta_{2}^{2}+\theta_{3}^{2}}$. Either all or none of the rotation components must be prescribed, since all rotation components are needed to define a rotation tensor. The moment_penalty parameter (with units of moment per radians) represents the torsional stiffness that enforces tracking of the prescribed rotations between the two bodies.

Optionally, moments may be prescribed on body b relative to body a, about the world coordinate axes, using the additional tag

```
<moment_x lc="3">1.e-3</moment_x>
<moment_y lc="4">3.e-3</moment_y>
<moment_z lc="5">2.e-3</moment_z>
```
The moment parameters specify the components of the moment vector in world coordinates, with optional associated load curves. The moment parameters should not be used simultaneously with a prescribed rotation.

_Example:_
```xml
<rigid_connector type="rigid spherical joint" name="Joint01">
  <tolerance>0.1</tolerance>
  <gaptol>0</gaptol>
  <force_penalty>1e0</force_penalty>
  <auto_penalty>1</auto_penalty>
  <body_a>1</body_a>
  <body_b>2</body_b>
  <joint_origin>0,0,0</joint_origin>
</rigid_connector>
```
