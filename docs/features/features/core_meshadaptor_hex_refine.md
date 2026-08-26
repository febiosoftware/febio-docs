# hex_refine

**Module:** core

**Category:** meshadaptor

**Type string:** `"hex_refine"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `max_iters` | max_iters | -1 | $\in \mathbb{Z}$ |  |
| `max_elements` | max_elements | -1 | $\in \mathbb{Z}$ |  |
| `map_data` | map_data | false | $\{0, 1\}$ |  |
| `nnc` | nnc | 8 | $\in \mathbb{Z}$ |  |
| `nsdim` | nsdim | 3 | $\in \mathbb{Z}$ |  |
| `transfer_method` | transfer_method | 0 | $\in \mathbb{Z}$ |  |
| `max_elem_refine` | max_elem_refine | 0 | $\in \mathbb{Z}$ |  |
| `max_value` | max_value | 0 | $\in \mathbb{R}$ |  |
| `criterion` | criterion |  | N/A |  |


## Description

The `hex_refine` adaptor refines elements by splitting each edge into 2. This may result in a non-conforming mesh, where an element node in the refined mesh lies on an edge in the parent mesh. Such hanging nodes are constrained using linear constraints and are forced to remain in the same relative position as the parent edge. This ensures that the refined mesh remains watertight. 
