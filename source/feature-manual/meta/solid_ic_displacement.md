The `displacement` initial condition can be used to set the initial displacement for a solid-mechanics analysis.

It should be noted that the initial displacement will be reflected in the plot file at time=0, but not the stress. However, internally, the stress at time=0 will be taken into account as the calculation is performed for subsequent times.

_Example:_
```xml
<ic type="displacement" node_set="set1">
  <value>1.0,0.0,0.0</value>
</ic>
```