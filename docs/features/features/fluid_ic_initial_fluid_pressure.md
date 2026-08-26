# initial fluid pressure

**Module:** fluid

**Category:** ic

**Type string:** `"initial fluid pressure"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `value` | value | 0 | $\in \mathbb{R}$ | P |


## Description

The `initial fluid pressure` is used to initialize the nodal dilatation of the fluid domain. The specified pressure value is converted to a corresponding dilatation and that value is assigned as the initial value for the dilatation degree of freedom. 
