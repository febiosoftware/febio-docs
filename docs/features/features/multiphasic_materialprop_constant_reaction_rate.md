# constant reaction rate

**Module:** multiphasic

**Category:** materialprop

**Type string:** `"constant reaction rate"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `k` | k | 0 | $\ge 0$ |  |


## Description

The material type for a constant specific reaction rate is `constant reaction rate`.

_Example:_
```xml
<reaction name="enzyme kinetics" type="Michaelis-Menten">
  <Vbar>0</Vbar>
  <vR sol="1">1</vR>
  <vP sol="2">1</vP>
  <forward_rate type="constant reaction rate">
    <k>1.0</k>
  </forward_rate>
</reaction>
```

