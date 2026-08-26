A linear constraint can be used to couple nodal degrees of freedom. The linear constraint has one dependent degree of freedom $u^{*}$, and several independent degrees of freedom $u_{i}$. The linear constraint is defined as follows:

\[
u^{*}=c_{0}+c_{1}u_{1}+\ldots+c_{n}u_{n}
\]

Here, the $c_{i}$ are user-specified scale factors and $c_{0}$ can be used to specify an offset.

The dependent degree of freedom $u^{*}$ will be removed from the linear system of equations. Consequently, this nodal degree of freedom should not be used in any other boundary condition.

To define a linear constraint, set the type attribute to linear constraint. The dependent degree of freedom, i.e. the dof that will be removed, is specified via a node number and a dof identifier. Each child dof is defined via the child_dof tag and similarly requires the corresponding node and dof identifier, as well as the value parameter.

```xml
<bc type="linear constraint">
  <node>5</node>
  <dof>x</dof>
  <child_dof>
    <node>8</node>
    <dof>x</dof>
    <value>1.0</value>
  </child_dof>
  <child_dof>
    <node>9</node>
    <dof>x</dof>
    <value>-1.0</value>
  </child_dof>
</bc>
```
