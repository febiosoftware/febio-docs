# tied-multiphasic

**Module:** multiphasic

**Category:** surfaceinteraction

**Type string:** `"tied-multiphasic"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `laugon` | Enforcement method | 0 | $[0, 1]$ |  |
| `tolerance` | tolerance | 0.1 | $\in \mathbb{R}$ |  |
| `gaptol` | gaptol | 0 | $\in \mathbb{R}$ |  |
| `ptol` | ptol | 0 | $\in \mathbb{R}$ |  |
| `ctol` | ctol | 0 | $\in \mathbb{R}$ |  |
| `penalty` | penalty | 1 | $\in \mathbb{R}$ |  |
| `auto_penalty` | auto_penalty | false | $\{0, 1\}$ |  |
| `update_penalty` | update_penalty | false | $\{0, 1\}$ |  |
| `two_pass` | two_pass | false | $\{0, 1\}$ |  |
| `knmult` | knmult | 1 | $\in \mathbb{Z}$ |  |
| `search_tol` | search_tol | 0.01 | $\in \mathbb{R}$ |  |
| `pressure_penalty` | pressure_penalty | 1 | $\in \mathbb{R}$ |  |
| `concentration_penalty` | concentration_penalty | 1 | $\in \mathbb{R}$ |  |
| `symmetric_stiffness` | symmetric_stiffness | true | $\{0, 1\}$ |  |
| `search_radius` | search_radius | 1 | $\in \mathbb{R}$ |  |
| `minaug` | minaug | 0 | $\in \mathbb{Z}$ |  |
| `maxaug` | maxaug | 10 | $\in \mathbb{Z}$ |  |


## Description

A `tied multiphasic` interface is similar to the [tied biphasic](biphasic_surfaceinteraction_tied-biphasic.md) interface. It may be used for tying any combination of solid, biphasic, multiphasic and rigid materials. It enforces continuity of the effective fluid pressure and effective solute concentrations across the interface when both materials are biphasic or multiphasic.

