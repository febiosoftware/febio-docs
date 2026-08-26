# relaxation-power

**Module:** solid

**Category:** materialprop

**Type string:** `"relaxation-power"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `tau` | time constant | 0 | $\gt 0$ | t |
| `beta` | power exponent | 0 | $\gt 0$ |  |


## Description

The material type for this relaxation function is `relaxation-power`.

The reduced relaxation function for this material type is given by

\[
g\left(t\right)=\frac{1}{\left(1+\frac{t}{\tau}\right)^{\beta}}
\]




