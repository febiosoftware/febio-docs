The material type for reactive fatigue materials is `reactive fatigue`.

The `elastic` property defines the constitutive relation of the intact (unconstrained) elastic material and associated material properties for unconstrained materials (used with `elastic damage`). The `elastic_damage` or `fatigue_damage` properties define the cumulative distribution function and associated material properties for elastic or fatigue damage, respectively. The `elastic_criterion` and `fatigue_criterion` properties define the damage criterion for intact and fatigued bonds of the elastic solid.

_Example:_

```xml
<material id="1" type="elastic damage">
  <k0>0.001</k0>
  <beta>2</beta>
  <elastic type="neo-Hookean">
    <density>1</density>
    <E>200000</E>
    <v>0.3</v>
  </elastic>
  <elastic_damage type="CDF Weibull">
    <alpha>20</alpha>
    <mu>200</mu>
    <Dmax>1</Dmax>
  </elastic_damage>
  <fatigue_damage type="CDF Weibull">
    <alpha>10</alpha>
    <mu>100</mu>
    <Dmax>1</Dmax>
  </fatigue_damage>
  <elastic_criterion type="DC von Mises stress"/>
  <fatigue_criterion type="DC von Mises stress"/>
</material>
```
