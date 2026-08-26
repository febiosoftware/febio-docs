The material type for Starling's equation for fluid supply is `Starling`.

The fluid supply is given by Starling's equation,

\[
\hat{\varphi}^{w}=k_{p}\left(\tilde{p}_{v}-\tilde{p}\right)+\sum\limits_{\alpha}q_{c}^{\alpha}\left(\tilde{c}_{v}^{\alpha}-\tilde{c}^{\alpha}\right)\,,
\]

where $\tilde{p}$ is the effective fluid pressure in the multiphasic material.

_Example:_

This example defines a solvent supply material of the Starling type for a multiphasic mixture containing one solute.

```xml
<solvent_supply type="Starling">
  <kp>0.001</kp>
  <pv>0.1</pv>
  <qc sol="1">1e-5</qc>
  <cv sol="1">150</cv>
</solvent_supply>
```
