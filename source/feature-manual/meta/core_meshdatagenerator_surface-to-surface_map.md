The `surface-to-surface map` generator defines a data field on the domain bounded by two surfaces. The data values are interpolated using a user-defined function between the surfaces.

```xml
<MeshData>
  <ElementData name="Emap" generator="surface-to-surface map" elem_set="Part1">
    <function type="math">x*x+1</function>
    <bottom_surface surface="surface1"/>
    <top_surface surface="surface2"/>
  <ElementData>
</MeshData>
```
