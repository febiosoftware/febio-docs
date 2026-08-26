Pressure loads apply a force to the surface of the geometry that is oriented along the surface normal. These pressure forces are also known as follower forces; they change direction as the body is deformed. The sign convention is so that a positive pressure will act opposite to the normal, so it will compress the material. The surface that the load is applied to is specified with the surface attribute.The surface must be defined in the Mesh section.


The `pressure` parameter defines the pressure value. The optional attribute `lc` defines a load controller for the pressure evolution. If `lc` is not defined a constant pressure is applied.

The optional `symmetric_stiffness` parameter (0 or 1) determines whether to use the exact form of the stiffness matrix for this surface load (0=non-symmetric), or the symmetric form (1=default). The non-symmetric form is numerically more robust, but it may also require using a globally non-symmetric stiffness matrix.

If the optional `linear` parameter is set to 1, a constant, deformation independent pressure load is applied. This is not recommend for large deformations. 

When the `shell_bottom flag` is set to 1, the surface is assumed to be a shell surface and the pressure is applied to the bottom part of the shell surface.


_Example:_
```xml
<surface_load type="pressure" surface="surface1">
  <pressure lc="1">1.0</pressure>
  <symmetric_stiffness>0</symmetric_stiffness>
</surface_load>
```