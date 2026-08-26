# pressure_stabilization

**Module:** biphasic

**Category:** load

**Type string:** `"pressure_stabilization"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `stabilize` | stabilize | true | $\{0, 1\}$ |  |


## Description

The `pressure_stabilization` surface load is a pseudo-surface load that is used to calculate the pressure stabilization time constant based on the properties of biphasic elements under that surface.

Note that the `stabilize` parameter is currently ignored so adding this feature will always perform the stabilization.

