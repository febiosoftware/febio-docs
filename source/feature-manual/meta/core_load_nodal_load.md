The nodal_load adds a value directly to the corresponding degrees of freedom in the global external load vector. When the loads are applied to displacement degrees of freedom, the forces always point in the same direction and do not deform with the geometry (i.e. they are non-follower forces). For other degrees of freedom they define a constant normal flux.

```
<nodal_load type="nodal_load" node_set="set1">
  <dof>x</dof>
  <scale lc="1">1.0</scale>
</nodal_load>
```

The `dof` parameter defines the degree of freedom. The following values are allowed:

* `x`: apply force in x-direction
* `y`: apply force in y-direction
* `z`: apply force in z-direction
* `p`: apply normal volumetric fluid flow rate
* `cn`: apply normal molar solute flow rate
* `t`: apply normal heat flux (heat transfer analysis)

For solutes, replace "n" with the solute id from the global solute table; for example, "c2". 

An optional load controller can be specified for the scale parameter with the `lc` attribute.