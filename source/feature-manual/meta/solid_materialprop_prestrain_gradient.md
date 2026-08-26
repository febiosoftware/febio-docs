The `prestrain gradient` generator defines the full prestrain gradient matrix either for the entire material or for each element separately.

This can be used to define the `prestrain` property of the [prestrain elastic](solid_material_prestrain_elastic.md) material.

The prestrain gradient that is applied is calculated by the following equation. 

\[
\mathbf{F}_{g}=\mathbf{I}\left(1-r\right)+\mathbf{F}_{0}r
\]

Here, $F_{g}$ is the applied prestrain gradient, $\mathbf{I}$ is the 3x3 identity tensor, $\mathbf{F}_{0}$ is the target prestrain gradient, defined by `F0` parameter, and $r$ is the ramp factor. 

_Example:_

In this example, the prestrain gradient is ramped up to a desired gradient value via a load controller. 

```xml
<material id="1" type="prestrain elastic">
  <elastic type="neo-Hookean">
    <E>1.0</E>
    <v>0.3</v>
  </elastic>
  <prestrain type="prestrain gradient">
    <ramp lc="1">1.0</ramp>
    <F0>2,0,0,0,2,0,0,0,2</F0>
  </prestrain>
</material>
```
