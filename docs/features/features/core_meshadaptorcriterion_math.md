# math

**Module:** core

**Category:** meshadaptorcriterion

**Type string:** `"math"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `math` | math | 1 | $\in \mathbb{R}$ |  |


## Description

This criterion evaluates a math expression over each element. 

_Example:_
```xml
<mesh_adaptor type="mmg_remesh">
  <max_iters>1</max_iters>
  <criterion type="math">
    <math>1*(1 - (X^2+Y^2)) + (X^2+Y^2)*(0.5*(Z-1)^2 - Z*(Z - 2))</math>
  </criterion>
</mesh_adaptor> 
```

