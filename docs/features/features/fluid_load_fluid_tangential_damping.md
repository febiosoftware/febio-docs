# fluid tangential damping

**Module:** fluid

**Category:** load

**Type string:** `"fluid tangential damping"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `penalty` | penalty | 0 | $\in \mathbb{R}$ |  |


## Description

The `fluid tangential damping` prescribes a shear traction that opposes tangential fluid velocity on a boundary surface. This can help stabilize inflow conditions.

```
<surface_load type="fluid tangential damping" surface="surface1">
	<penalty>1</penalty>
</surface_load>
```
