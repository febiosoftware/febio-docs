A rigid lock connects rigid bodies $a$ and $b$, preventing relative motion between them. It requires the specification of a joint origin and two orthogonal axes $\mathbf{e}_{1}$ and $\mathbf{e}_{2}$.

The `tolerance` parameter defines the augmentation tolerance. That is, when the relative change in the constraint forces and moments (the Lagrange multipliers) are less than this value. The `gaptol` parameter defines the tolerance for spatial separation of the joint origin on the two bodies (in units of length). The `angtol` parameter defines the tolerance for angular separation of the joint axes on the two bodies (in units of radians). Setting any of these three elements to zero disables the enforcement of that tolerance. The `force_penalty` parameter (with units of force per length) represents the stiffness that prevents the joint origin on the two bodies from separating along the rotation axis. The `moment_penalty` parameter (with units of moment per radians) represents the torsional stiffness that enforces parallelism of the joint rotation axis on the two bodies. The `body_a` and `body_b` parameters are the material numbers of the two rigid bodies. The `joint_origin` parameter defines the position of the joint (the origin of the basis $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$) in world coordinates at the start of the analysis. Note that this point does not have to be inside or on the surface of either of the two bodies. The first_axis element defines the orientation of the axis $\mathbf{e}_{1}$ in world coordinates at the start of the analysis. The second_axis element defines the orientation of the second axis $\mathbf{e}_{2}$ in world coordinates at the start of the analysis.

_Example:_
```xml
<rigid_connector type="rigid lock" name="Joint01">
  <tolerance>0</tolerance>
  <gaptol>1e-4</gaptol>
  <angtol>1e-4</angtol>
  <force_penalty>1e0</force_penalty>
  <moment_penalty>1e0</moment_penalty>
  <auto_penalty>1</auto_penalty>
  <body_a>1</body_a>
  <body_b>2</body_b>
  <joint_origin>0,0,0</joint_origin>
  <first_axis>1,0,0</first_axis>
  <second_axis>0,1,0</second_axis>
</rigid_connector>
```