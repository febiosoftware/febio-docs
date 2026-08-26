# EFD Mooney-Rivlin

**Module:** solid

**Category:** material

**Type string:** `"EFD Mooney-Rivlin"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `density` | density | 1 | $\ge 0$ | M/L^3 |
| `k` | bulk modulus | 0 | $\ge 0$ | P |
| `pressure_model` | pressure_model | 0 | $[0, 3]$ |  |
| `c1` | c1 | 0 | $\in \mathbb{R}$ | P |
| `c2` | c2 | 0 | $\in \mathbb{R}$ | P |
| `beta` | beta |  | $\in \mathbb{R}$ |  |
| `ksi` | ksi |  | $\in \mathbb{R}$ | P |


## Description

The material type for a Mooney-Rivlin material with an ellipsoidal continuous fiber distribution is `EFD Mooney-Rivlin`.

The stress $\tilde{\boldsymbol{\sigma}}$ for this material is given by,

\[
\tilde{\boldsymbol{\sigma}}=\tilde{\boldsymbol{\sigma}}_{MR}+\tilde{\boldsymbol{\sigma}}_{f}\,.
\]

Here, $\tilde{\boldsymbol{\sigma}}_{MR}$ is the stress from the Mooney-Rivlin basis (see [Mooney-Rivlin](solid_material_mooney-rivlin.md)), and $\tilde{\boldsymbol{\sigma}}_{f}$ is the stress contribution from the ellipsoidal fiber distribution (see [EFD-Uncoupled](solid_material_efd_uncoupled.md)).

_Example:_
```xml
<material id="1" type="EFD Mooney-Rivlin">
  <c1>1</c1>
  <c2>0</c2>
  <beta>4.5,4.5,4.5</beta>
  <ksi>1,1,1</ksi>
  <k>20000</k>
  <mat_axis type="local">0,0,0</mat_axis>
</material>
```
