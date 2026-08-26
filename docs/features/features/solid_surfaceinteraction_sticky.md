# sticky

**Module:** solid

**Category:** surfaceinteraction

**Type string:** `"sticky"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `laugon` | Enforcement method | 0 | $[0, 1]$ |  |
| `tolerance` | tolerance | 0.01 | $\in \mathbb{R}$ |  |
| `penalty` | penalty | 1 | $\in \mathbb{R}$ |  |
| `minaug` | minaug | 0 | $\in \mathbb{Z}$ |  |
| `maxaug` | maxaug | 10 | $\in \mathbb{Z}$ |  |
| `search_tolerance` | search_tolerance | 0.0001 | $\in \mathbb{R}$ |  |
| `max_traction` | max_traction | 0 | $\in \mathbb{R}$ |  |
| `snap_tol` | snap_tol | 0 | $\in \mathbb{R}$ |  |
| `flip_secondary` | flip_secondary | false | $\{0, 1\}$ |  |
| `gap_offset` | gap_offset | 0 | $\in \mathbb{R}$ |  |


## Description

A sticky interface is similar to a tied interface except that it allows for initial separation of the tied surfaces and breaking of the tie after a user-defined normal traction is exceeded. The tie is only applied when the surfaces contact and sustained as long as the normal traction is less than the threshold.

The `max_traction` parameter can be used to break the tied interface after the normal traction exceeds the specified value. Initially, this value is set to zero, in which case FEBio will ignore this value and the tie cannot be broken. 

The `snap_tol` parameter is used in determining the minimum distance that a primary surface node must have approached the secondary surface facet in order to snap onto the secondary surface. The initial value is zero, meaning a node must have penetrated the secondary surface before it will be tied to it. 


