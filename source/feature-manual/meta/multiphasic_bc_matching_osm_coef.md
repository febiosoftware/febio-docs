The `matching_osm_coef` boundary condition is a surface boundary condition that imposes the same osmotic coefficient in the bath as in the multiphasic material bounded by that surface. 

_Example:_
```xml
<bc type="matching_osm_coeff">
  <ambient_pressure>1</ambient_pressure>
  <ambient_osmolarity>1e-3</ambient_osmolarity>
  <shell_bottom>0</shell_bottom>
</bc>
```