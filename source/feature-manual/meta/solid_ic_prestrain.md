The `prestrain` initial condition can be used to accomplish one of two things. It can be used to convert a forward analysis in an equivalent prestrain analysis. Or it can be used to fix the prestrain gradient. In either case the current geometry is used as the new reference geometry of the following analysis step.

The following example shows how a forward analysis can be converted to a prestrain analysis. 

```
<ic type="prestrain">
  <init>1</init>
  <reset>1</reset>
</ic> 
```

Note that this in itself may not be sufficient to define the equivalent prestrain analysis. For instance, if the forward model applied prescribed displacements, then these boundary conditions must be replaced with fixed boundary conditions.

If the `init` parameter is set to 0 (false), then the prestrain gradient will be fixated in the current geometry. This means that any remaining distortion will be applied to the prestrain correction factor before the current geometry is converted to the new reference geometry.
