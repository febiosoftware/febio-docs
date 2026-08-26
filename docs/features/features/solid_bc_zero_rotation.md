# zero rotation

**Module:** solid

**Category:** bc

**Type string:** `"zero rotation"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `u_dof` | x-rotation | false | $\{0, 1\}$ |  |
| `v_dof` | y-rotation | false | $\{0, 1\}$ |  |
| `w_dof` | z-rotation | false | $\{0, 1\}$ |  |


## Description

The `zero rotation` boundary condition fixes the selected rotational degrees of freedom of the nodes in the specified node set.

This only applies to the nodes of an element domain that defines rotational degrees of freedom. At this point, this is only relevant for beam elements. 

