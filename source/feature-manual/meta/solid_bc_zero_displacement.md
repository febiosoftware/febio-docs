To fix the nodal displacement degrees of freedom (dof) use the `zero displacement` boundary condition. This element has two required attributes: the type is set to `zero displacement` and the node set to which this boundary condition applies is defined via `node_set`. The optional `name` attribute can be used to give the boundary condition a name. 

This boundary condition has three parameters, one for each degree of freedom. Set the value of each parameter to 1 to constrain the corresponding dof. 

```
<bc type="zero displacement" node_set="nodeset1">
  <x_dof>1</x_dof>
  <y_dof>1</y_dof>
  <z_dof>1</z_dof>
</bc>
```