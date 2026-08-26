The `init_dof` initial condition can be used to initialize any degree of freedom of the model. This feature is deprecated and it is better to use one of the other specialized initial conditions.

_Example:_
```xml
<ic name="ic01" type="init_dof" node_set="set1">
    <dof>vx</dof>
    <value>1</value>
</ic>
```