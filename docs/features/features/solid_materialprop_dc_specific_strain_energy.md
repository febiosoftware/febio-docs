# DC specific strain energy

**Module:** solid

**Category:** materialprop

**Type string:** `"DC specific strain energy"`

## Parameters

This feature has no parameters.


## Description

The material type for specific strain energy damage criterion is `DC specific strain energy`. For this criterion, 

\[
\Xi\left(\mathbf{F}\right)=\Psi_{0}\left(\mathbf{F}\right)/\rho
\]

where $\rho$ is the elastic material's density.

_Example:_
```xml
<criterion type="DC specific strain energy"/>
```
