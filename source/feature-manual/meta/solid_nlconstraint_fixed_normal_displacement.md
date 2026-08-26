A fixed normal displacement constraint enforces zero solid displacement normal to a user-selected surface. This constraint is prescribed on a deformable surface of the model and is enforced for every node on that surface. It uses the local surface normal in the selected surface's reference configuration. If the selected surface is planar, the functionality of this constraint is equivalent to the symmetry plane constraint described in [symmetry plane](solid_nlconstraint_symmetry_plane.md).

```
<constraint type="fixed normal displacement" surface="FixedNormalDisplacement01">
	<laugon>0</laugon>
	<penalty>1000</penalty>
	<tol>0.2</tol>
	<minaug>0</minaug>
	<maxaug>10</maxaug>
	<shell_bottom>0</shell_bottom>
</constraint>
```

The surface (FixedNormalDisplacement01 in this example), is defined in the `Mesh` section. Let $\mathbf{u}$ denote the nodal displacement vector and let $\mathbf{n}$ denote the unit normal at each node of the surface; the fixed normal displacement constraint enforces $u_{n}\equiv\mathbf{u}\cdot\mathbf{n}=0$ using a penalty method, optionally with augmented Lagrangian. The reaction force needed to enforce this constraint is evaluated as $\varepsilon u_{n}$, where $\varepsilon$ is the user-specified penalty parameter (with units of force per length). To use the augmented Lagrangian method, set `laugon` to 1, and the Lagrange multiplier $\lambda$ will be augmented as $\lambda\leftarrow\lambda+\varepsilon u_{n}$. Augmentations terminate when the relative change in \lambda  is less than the user-specified tolerance `tol`, or when the number of augmentations exceeds `maxaug`.

For example, this constraint may be used on a cylindrical shaft, over the portion of the shaft which is supported by a bearing journal.