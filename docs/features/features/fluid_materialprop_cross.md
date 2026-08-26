# Cross

**Module:** fluid

**Category:** materialprop

**Type string:** `"Cross"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `mu0` | zero shear rate viscosity | 0 | $\ge 0$ | P.t |
| `mui` | infinite shear rate viscosity | 0 | $\ge 0$ | P.t |
| `lambda` | relaxation time | 0 | $\ge 0$ | t |
| `m` | power | 2 | $\ge 2$ |  |


## Description

The material type for a Cross model [^1] is `Cross`.

The viscous shear stress for this material model is

\[
\boldsymbol{\tau}=2\mu\mathbf{D}
\]

where

\[
\mu=\mu_{\infty}+\left(\mu_{0}-\mu_{\infty}\right)\frac{1}{1+\left(\lambda\dot{\gamma}\right)^{m}}
\]

Here, $\dot{\gamma}=\sqrt{2\mathbf{D}:\mathbf{D}}$ is the engineering shear rate.

_Example:_
```xml
<viscous type="Cross">
	<mu0>0.056</mu0>
	<mui>0.0035</mui>
	<lambda>1.0</lambda>
	<m>1.0</m>
</viscous>
```

[^1]: Cho, Y I and Kensey, K R, "Effects of the non-Newtonian viscosity of blood on flows in a diseased arterial vessel. Part 1: Steady flows", Biorheology 28, 3-4 (1991), pp. 241-62.

