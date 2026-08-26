# pardiso_64

**Module:** core

**Category:** linearsolver

**Type string:** `"pardiso_64"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `precondition` | precondition | false | $\{0, 1\}$ |  |
| `msglvl` | msglvl | 0 | $\in \mathbb{Z}$ |  |


## Description

The **pardiso_64** solver is variant of the pardiso solver that can be used for very large problems since it uses 64 bit integers. Other than that, it is identical to the standard pardiso solver. 

_Example:_
```xml
<default_linear_solver type="pardiso_64"/>
```
