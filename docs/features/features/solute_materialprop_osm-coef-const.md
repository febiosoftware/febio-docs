# osm-coef-const

**Module:** solute

**Category:** materialprop

**Type string:** `"osm-coef-const"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `osmcoef` | osmotic coefficient | 1 | $\ge 0$ |  |


## Description

The material type for constant osmotic coefficient materials is `osm-coef-const`.

For this material model, $\Phi$ is constant.

_Example:_
```xml
<osmotic_coefficient name="Osmotic coefficient" type="osm-coef-const">
  <osmcoef>1</osmcoef>
</osmotic_coefficient>
```

