# cylindrical

**Module:** core

**Category:** vec3dvaluator

**Type string:** `"cylindrical"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `center` | center | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ |  |
| `axis` | axis | {0.000000,0.000000,1.000000} | $\in \mathbb{R}^3$ |  |
| `vector` | vector | {1.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ |  |


## Description

This valuator generates a unique vector in a cylindrical distribution. 
The `center` parameter sets a point on the axis.
The `axis` parameter defines the orientation of the axis. 
The `vector` parameter is a vector that will be transported around the axis. 

The following example defines a fiber property using the `cylindrical` vector valuator. 

```
<fiber type="cylindrical">
  <center>0,0,0</center>
  <axis>0,0,1</axis>
  <vector>0,1,0</vector>
</fiber>
```

