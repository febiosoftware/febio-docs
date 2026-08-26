The `rigid_fixed` rigid constraint fixes one or multiple rigid degrees of freedom.

The name of the rigid material is defined in the `Material` section. The referenced material must be a "rigid body" material. 

The following example fixes the displacement degrees of freedom. 

```
<rigid_bc type="rigid_fixed">
  <rb>RigidMaterial1</rb>
  <Rx_dof>1</Rx_dof>
  <Ry_dof>1</Ry_dof>
  <Rz_dof>1</Rz_dof>
</rigid_bc>
```
