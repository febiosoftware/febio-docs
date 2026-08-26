# solub-const

**Module:** solute

**Category:** materialprop

**Type string:** `"solub-const"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `solub` | solubility | 1 | $\ge 0$ |  |


## Description

The material type for constant solubility materials is `solub-const`.

For this material model, $\tilde{\kappa}$ is constant.

_Example:_
```
<solubility name="Solubility" type="solub-const">
  <solub>1</solub>
</solubility>
```

