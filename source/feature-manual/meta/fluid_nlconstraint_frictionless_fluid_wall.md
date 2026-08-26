One of the natural boundary conditions for fluid analyses is to enforce zero fluid velocity normal to a boundary, implying that this boundary is a frictionless fluid wall. In some analyses however, this natural boundary condition may not be enforced sufficiently well. In such cases, use this frictionless fluid wall linear constraint to produce a more strict enforcement of this condition.

```
<constraint type="frictionless fluid wall" name="FrictionlessFluidWall1" surface="FrictionlessFluidWall1">
	<laugon>0</laugon>
	<tol>0.2</tol>
	<penalty>1</penalty>
	<minaug>0</minaug>
	<maxaug>10</maxaug>
</constraint>
```

In fluid-structure interaction analyses, this constraint may be used in conjunction with the symmetry plane described in [symmetry plane](solid_nlconstraint_symmetry_plane.md), using a lower value of the penalty parameter, as may be necessary in practice.