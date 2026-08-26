This nodal load defines a force that is applied to each node in the node set. The force will ramp up from the value at the end of the last time step, to the desired value defined in the force variable. 

```
<nodal_load type="nodal_target_force" node_set="set1">
  <force>1,0,0</force>
  <scale lc="1">1</scale>
</nodal_load>
```
Note that, in order to reach the target load, the loadcurve assigned to scale must start at 0 and end at 1. 