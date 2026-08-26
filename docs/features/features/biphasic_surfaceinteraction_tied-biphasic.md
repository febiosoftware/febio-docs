# tied-biphasic

**Module:** biphasic

**Category:** surfaceinteraction

**Type string:** `"tied-biphasic"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `laugon` | Enforcement method | 0 | $[0, 1]$ |  |
| `tolerance` | tolerance | 0.1 | $\in \mathbb{R}$ |  |
| `gaptol` | gaptol | -1 | $\in \mathbb{R}$ |  |
| `ptol` | ptol | -1 | $\in \mathbb{R}$ |  |
| `penalty` | penalty | 1 | $\in \mathbb{R}$ |  |
| `auto_penalty` | auto_penalty | false | $\{0, 1\}$ |  |
| `update_penalty` | update_penalty | false | $\{0, 1\}$ |  |
| `two_pass` | two_pass | false | $\{0, 1\}$ |  |
| `knmult` | knmult | 1 | $\in \mathbb{Z}$ |  |
| `search_tol` | search_tol | 0.01 | $\in \mathbb{R}$ |  |
| `pressure_penalty` | pressure_penalty | 1 | $\in \mathbb{R}$ |  |
| `symmetric_stiffness` | symmetric_stiffness | true | $\{0, 1\}$ |  |
| `search_radius` | search_radius | 1 | $\in \mathbb{R}$ |  |
| `minaug` | minaug | 0 | $\in \mathbb{Z}$ |  |
| `maxaug` | maxaug | 10 | $\in \mathbb{Z}$ |  |


## Description

A `tied biphasic` interface is similar to the tied interface. It may be used for tying any combination of solid, biphasic, and rigid materials. It enforces continuity of the fluid pressure across the interface when both materials are biphasic.

Please see [tied-elastic](solid_surfaceinteraction_tied-elastic.md) for a more detailed explanation of the parameters. 

In order to model fluid flow across the interface, the user must set the `pressure_penalty` parameter. This parameter is similar to the `penalty` parameter, but acts on the pressure gap, i.e. the difference in fluid pressure across the interface.

