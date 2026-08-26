# defgrad

**Module:** solid

**Category:** meshdatagenerator

**Type string:** `"defgrad"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `node_displacement_map` | node_displacement_map |  | N/A |  |


## Description

The `defgrad` meshdata generator generates a mat3d (i.e. a $3 \times 3$ matrix) field over the domain that is the gradient of a displacement vector field. 

The displacement vector field must also be specified as a nodedata map in the `MeshData` section of the input file.

