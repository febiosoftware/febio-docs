To fix an effective solute concentration $\tilde{c}$ degree of freedom (`c_dof`) in a multiphasic or fluid-solutes analysis, use the `zero concentration` boundary conditions.

```
<bc node_set="set01" type="zero concentration">
  <c_dof>c1</c_dof>
</bc>
```