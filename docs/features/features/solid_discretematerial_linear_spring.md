# linear spring

**Module:** solid

**Category:** discretematerial

**Type string:** `"linear spring"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `E` | E | 1 | $\gt 0$ |  |


## Description

The linear spring has a linear force-displacement relation. It requires the E parameter that defines the spring constant.

\[
    f\left(d \right) = E\,d
\]

For example,
```
<discrete_material id="1" type="linear spring">
    <E>3.0</E>
</discrete_material>
```

