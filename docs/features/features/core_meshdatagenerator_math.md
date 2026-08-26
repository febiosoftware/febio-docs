# math

**Module:** core

**Category:** meshdatagenerator

**Type string:** `"math"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `math` | math |  | N/A |  |


## Description

The `math` mesh data generator calculates nodal scalar values using a mathematical expression. 

```xml
<NodeData type="math" node_set="set1">
    <math>X+Y+Z</math>
</NodeData>
```

