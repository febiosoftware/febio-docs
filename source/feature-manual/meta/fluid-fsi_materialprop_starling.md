The material type for Starling's equation for fluid supply is `Starling`.

The fluid supply is given by Starling's equation,

\[
\hat{\varphi}^{w}=k_{p}\left(p_{v}-p\right)\,,
\]

where $p$ is the fluid pressure in the biphasic material.

_Example:_

This example defines a fluid supply material of the Starling type.
```xml
<solvent_supply type="Starling">
  <kp>0.001</kp>
  <pv>0.1</pv>
</solvent_supply>
```

