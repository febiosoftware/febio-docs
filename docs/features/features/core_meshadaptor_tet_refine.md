# tet_refine

**Module:** core

**Category:** meshadaptor

**Type string:** `"tet_refine"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `max_iters` | max_iters | -1 | $\in \mathbb{Z}$ |  |
| `max_elements` | max_elements | -1 | $\in \mathbb{Z}$ |  |
| `map_data` | map_data | false | $\{0, 1\}$ |  |
| `nnc` | nnc | 8 | $\in \mathbb{Z}$ |  |
| `nsdim` | nsdim | 3 | $\in \mathbb{Z}$ |  |
| `transfer_method` | transfer_method | 0 | $\in \mathbb{Z}$ |  |


## Description

The `tet_refine` mesh adaptor applies a uniform refinement of a tetrahedral mesh.
