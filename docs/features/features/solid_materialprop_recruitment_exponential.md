# recruitment exponential

**Module:** solid

**Category:** materialprop

**Type string:** `"recruitment exponential"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `alpha` | alpha | 1 | $\ge 0$ |  |
| `mu0` | mu0 | 1 | $\ge 0$ |  |
| `mu1` | mu1 | 0 | $\in \mathbb{R}$ |  |
| `scale` | scale | 1 | $\gt 0$ |  |


## Description

The material type for an exponential weak bond recruitment function is `recruitment exponential`.

For this material the recruitment function is given by,

\[
F\left(\Xi\right)=\mu_{0}\exp\left(\mu_{1}\left(\frac{\Xi}{s}\right)^{\alpha}\right)
\]

where $\Xi$ is the measure of strain that triggers a new reactive weak bond generation. This function is unbounded with increasing $\Xi$. Users should typically employ $\mu_{0}=1$.


