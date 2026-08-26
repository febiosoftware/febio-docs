# compressible Gent

**Module:** solid

**Category:** material

**Type string:** `"compressible Gent"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `density` | density | 1 | $\ge 0$ | M/L^3 |
| `G` | G | 0 | $\gt 0$ | P |
| `K` | K | 0 | $\gt 0$ | P |
| `Jm` | Jm | 0 | $\gt 0$ |  |


## Description

The compressible Gent material is defined using the `compressible Gent` type string.

The strain energy of this material is defined as follows, 

\[
\Psi_{r}=-\frac{\mu J_{m}}{2}\ln\left(1-\frac{I_{1}-3}{J_{m}}\right)+\frac{\kappa}{2}\left(\frac{J^{2}-1}{2}-\ln J\right)^{4}
\]

Here, $\mu$ is the shear modulus. 

_Example:_
```xml
<material id="2" type="compressible Gent">
  <G>3.14</G>
  <Jm>1.5</Jm>
  <k>1e5</k>
</material>
```

