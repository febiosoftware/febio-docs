# mmg_remesh

**Module:** core

**Category:** meshadaptor

**Type string:** `"mmg_remesh"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `max_iters` | max_iters | -1 | $\in \mathbb{Z}$ |  |
| `max_elements` | max_elements | 0 | $\in \mathbb{Z}$ |  |
| `map_data` | map_data | false | $\{0, 1\}$ |  |
| `nnc` | nnc | 8 | $\in \mathbb{Z}$ |  |
| `nsdim` | nsdim | 3 | $\in \mathbb{Z}$ |  |
| `transfer_method` | transfer_method | 1 | $\in \mathbb{Z}$ |  |
| `min_element_size` | min_element_size | 0 | $\in \mathbb{R}$ |  |
| `hausdorff` | hausdorff | 0.01 | $\in \mathbb{R}$ |  |
| `gradation` | gradation | 1.3 | $\in \mathbb{R}$ |  |
| `relative_size` | relative_size | true | $\{0, 1\}$ |  |
| `mesh_coarsen` | mesh_coarsen | false | $\{0, 1\}$ |  |
| `normalize_data` | normalize_data | false | $\{0, 1\}$ |  |
| `criterion` | criterion |  | N/A |  |
| `size_function` | size_function |  | N/A |  |


## Description

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
