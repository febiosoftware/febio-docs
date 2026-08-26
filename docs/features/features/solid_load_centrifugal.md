# centrifugal

**Module:** solid

**Category:** load

**Type string:** `"centrifugal"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `angular_speed` | angular_speed | 0 | $\in \mathbb{R}$ | r/t |
| `rotation_axis` | rotation_axis | {0.000000,0.000000,1.000000} | $\in \mathbb{R}^3$ |  |
| `rotation_center` | rotation_center | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ | L |


## Description

A centrifugal body force per mass $\mathbf{b}=\omega^{2}r\mathbf{e}_{r}$ may be used for bodies undergoing steady-state rotation with angular speed $\omega$ about a rotation axis directed along $\mathbf{n}$ and passing through the rotation center $\mathbf{c}$. Here, $r$ represents the distance of each material point from the axis of rotation, and $\mathbf{e}_{r}$ is the radial unit vector from the axis of rotation, both of which are calculated internally from the knowledge of $\mathbf{n}$ and $\mathbf{c}$.

```
<body_load type="centrifugal">
  <angular_speed>1.0</angular_speed>
  <rotation_axis>0.707,0.707,0</rotation_axis>
  <rotation_center>0,0,0</rotation_center>
</body_load>
```
