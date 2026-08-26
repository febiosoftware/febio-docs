# math-interval

**Module:** core

**Category:** loadcontroller

**Type string:** `"math-interval"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `interval` | interval |  | $\in \mathbb{R}$ |  |
| `left_extend` | left_extend | 1 | $[0, 2]$ |  |
| `right_extend` | right_extend | 1 | $[0, 2]$ |  |
| `var` | var |  | N/A |  |
| `math` | math |  | N/A |  |


## Description

The `math-interval` controller is similar to the math controller, but the math expression is defined only over a time interval. The behavior outside the interval can be specified separately. 

The values for left_extend and right_extend can be set to one of the following values. 

|Extend         |Description|
|---------------|-----------|
|`zero`         | The value of the curve is zero outside the interval |
|`constant`     | The value is the constant value at the end point |
|`repeat`       | The curve is repeated |


_Example:_
```xml
<load_controller id="1" name="LC1" type="math-interval">
	<interval>0,1</interval>
	<left_extend>constant</left_extend>
	<right_extend>constant</right_extend>
	<math>sin(t)</math>
</load_controller>
```
