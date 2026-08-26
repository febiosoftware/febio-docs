The `mmg_remesh` adaptor can be used for adaptive mesh refinement of linear tetrahedral meshes.

_Example:_
```xml
<mesh_adaptor type="mmg_remesh">
  <max_iters>1</max_iters>
  <criterion type="stress"/>
  <relative_size>1</relative_size>
  <normalize_data>0</normalize_data>
  <mesh_coarsen>0</mesh_coarsen>
  <size_function type="step">
    <x0>10</x0>
    <left_val>1</left_val>
    <right_val>0.5</right_val>
  </size_function>
</mesh_adaptor>
```