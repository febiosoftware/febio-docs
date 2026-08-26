# prescribed rotation

**Module:** solid

**Category:** bc

**Type string:** `"prescribed rotation"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `dof` | dof | -1 | $\in \mathbb{Z}$ |  |
| `value` | value | 0 | $\in \mathbb{R}$ | r |
| `relative` | relative | false | $\{0, 1\}$ |  |


## Description

The `prescribed rotation` boundary condition sets the value of the selected rotational degree of freedom of the nodes in the specified node set.

The `value` parameter is specified in radians.

This only applies to the nodes of an element domain that defines rotational degrees of freedom. At this point, this is only relevant for beam elements.

