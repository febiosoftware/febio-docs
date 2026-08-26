The `elastic-solid` is the standard formulation used in FEBio for most (unconstrained) elastic materials. (That is, it's the formulation selected when the `type` attribute of the `SolidDomain` element is omitted). 

The `solid-elastic` defines the parameters `secant_stress` and `secant_tangent`. When specified the formulation will use a secant approximation of the corresponding variable. When setting `secant_stress` to 1, the stress is calculated from a secant approximation that uses the material's strain-energy density. Similarly, when `secant_tangent` is specified, the material tangent is approximated using the PK2 stress. 

The optional `elem_type` parameter must be specified as an attribute of the `SolidDomain` element. If omitted an element type and integration rule will be selected automatically based on the mesh. However, it can be specified to further specialize the quadrature rule. The values of the rule depend on the specific element type of the mesh. The tables below show the available integration rules for the different element types. The values marked with an asterisk (*) are the default.

For the **hex8** element, the following values are defined.

| hex8   | Description                                                        |
|--------|--------------------------------------------------------------------|
|`HEX8G8`| Gaussian integration using 2x2x2 integration points. (*)           |
|`HEX8G6`| Alternative integration rule for bricks using 6 integration points.|

For the **hex20** element, the following values are defined.


| hex20   | Description                                             |
|---------|---------------------------------------------------------|
|`HEX20G8`| Gaussian integration using 2x2x2 integration points. (*)|

For the **tet4** element, the following values are allowed.

| tet4   | Description                                               |
|--------|-----------------------------------------------------------|
|`TET4G1`| Gaussian integration rule using one integration point. (*)|
|`TET4G4`| Gaussian integration rule using 4 integration points.     |

For the **tet10** element, the following integration rules are supported.

| tet10     | Description                                               |
|-----------|-----------------------------------------------------------|
|`TET10G4`  | Gaussian integration rule using 4 integration points      |
|`TET10G8`  | Gaussian integration rule using 8 integration points (*)  |
|`TET10GL11`| Gauss-Lobatto integration rule using 11 integration points|

The Lobatto integration rule differs from a regular Gauss integration rule in that it includes the vertices of the tetrahedral element. This integration rule uses the 10 tetrahedral nodes, plus one integration rule located at the center of the element.

For the **tet15** element, the following integration rules are defined.

| tet15    | Description                                              |
|----------|----------------------------------------------------------|
|`TET15G8` | Gaussian integration rule using 8 integration points     |
|`TET15G11`| Gaussian integration rule using 11 integration points    |
|`TET15G15`| Gaussian integration rule using 15 integration points (*)|

For the **penta15** element, the following values are defined.

| penta15    | Description                                         |
|------------|-----------------------------------------------------|
|`PENTA15G8` | Gaussian integration using 2x2x2 integration points.|

