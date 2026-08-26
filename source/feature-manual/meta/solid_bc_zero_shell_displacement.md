To fix the nodal back-displacement degrees of freedom (dof) of a shell use the `zero shell displacement` boundary condition. This element has two required attributes: the type is set to `zero shell displacement` and the node set to which this boundary condition applies is defined via `node_set`. The optional `name` attribute can be used to give the boundary condition a name. 

This boundary condition has three parameters, one for each degree of freedom. Set the value of each parameter to 1 to constrain the corresponding dof. 

```
<bc type="zero shell displacement" node_set="nodeset1">
  <sx_dof>1</sx_dof>
  <sy_dof>1</sy_dof>
  <sz_dof>1</sz_dof>
</bc>
```

This boundary condition can only be applied to nodes that belong to shells. 