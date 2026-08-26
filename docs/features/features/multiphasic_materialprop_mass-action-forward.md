# mass-action-forward

**Module:** multiphasic

**Category:** materialprop

**Type string:** `"mass-action-forward"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `override_vbar` | override_vbar | false | $\{0, 1\}$ |  |
| `Vbar` | Vbar | 0 | $\in \mathbb{R}$ |  |
| `forward_rate` | forward_rate |  | N/A |  |
| `vR` | Reactants |  | N/A |  |
| `vP` | Products |  | N/A |  |


## Description

The material type for the Law of Mass Action for a forward reaction is `mass-action-forward`.

For this type of reaction the constitutive relation for the molar production rate is given by

\[
\hat{\zeta}=k\prod\limits_{\alpha}\left(c^{\alpha}\right)^{\nu_{R}^{\alpha}}\,.
\]

The `forward_rate` property defines the constitutive form of the specific forward reaction rate. The units of $\hat{\zeta}$ are $[n/L^{\mathrm{3}}\cdot t]$ and those of $c^{\alpha}$ are $[n/L^{\mathrm{3}}]$.


