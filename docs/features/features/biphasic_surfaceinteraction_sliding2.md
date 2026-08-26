# sliding2

**Module:** biphasic

**Category:** surfaceinteraction

**Type string:** `"sliding2"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `laugon` | Enforcement method | 0 | $[0, 1]$ |  |
| `tolerance` | tolerance | 0.1 | $\in \mathbb{R}$ |  |
| `gaptol` | gaptol | 0 | $\in \mathbb{R}$ | L |
| `ptol` | ptol | 0 | $\in \mathbb{R}$ |  |
| `penalty` | penalty | 1 | $\in \mathbb{R}$ |  |
| `auto_penalty` | auto_penalty | false | $\{0, 1\}$ |  |
| `update_penalty` | update_penalty | false | $\{0, 1\}$ |  |
| `two_pass` | two_pass | false | $\{0, 1\}$ |  |
| `knmult` | knmult | 1 | $\in \mathbb{Z}$ |  |
| `search_tol` | search_tol | 0.01 | $\in \mathbb{R}$ |  |
| `pressure_penalty` | pressure_penalty | 1 | $\in \mathbb{R}$ |  |
| `symmetric_stiffness` | symmetric_stiffness | true | $\{0, 1\}$ |  |
| `search_radius` | search_radius | 1 | $\in \mathbb{R}$ | L |
| `seg_up` | seg_up | 0 | $\in \mathbb{Z}$ |  |
| `minaug` | minaug | 0 | $\in \mathbb{Z}$ |  |
| `maxaug` | maxaug | 10 | $\in \mathbb{Z}$ |  |
| `node_reloc` | node_reloc | false | $\{0, 1\}$ |  |
| `smooth_aug` | smooth_aug | false | $\{0, 1\}$ |  |
| `dual_proj` | dual_proj | true | $\{0, 1\}$ |  |


## Description

This was the original implementation of a sliding-elastic interface that can work with biphasic materials. It has been replaced by the [sliding-biphasic](biphasic_surfaceinteraction_sliding-biphasic.md) interface and is mostly maintained for backward compatibility. 

