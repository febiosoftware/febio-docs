The `prescribed deformation` boundary condition can be used to prescribe the displacement of a node using the following equation. 

\[
\boldsymbol{u}=s\left(\boldsymbol{F}-\boldsymbol{I}\right)\boldsymbol{X}
\]

Here, $\boldsymbol{u}$ is the displacement vector, $\boldsymbol{X}$ the reference position vector, $\boldsymbol{F}$ a "deformation gradient", $\boldsymbol{I}$ the identity tensor, and $s$ a scale factor. 

_Example:_
```xml
<bc type="prescribed deformation" node_set="set1">
  <scale lc="1">0.1</scale>
  <F>2,0,0, 0,2,0, 0,0.25,0</F>
<bc>
```