# fluid RC

**Module:** fluid

**Category:** bc

**Type string:** `"fluid RC"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `R` | R | 0 | $\in \mathbb{R}$ | F.t/L^5 |
| `initial_pressure` | initial_pressure | 0 | $\in \mathbb{R}$ | P |
| `capacitance` | capacitance | 0 | $\in \mathbb{R}$ | L^5/F |
| `Bernoulli` | Bernoulli | false | $\{0, 1\}$ |  |


## Description

This boundary condition models a fluid surface that has an RC-equivalent circuit for outflow conditions.
