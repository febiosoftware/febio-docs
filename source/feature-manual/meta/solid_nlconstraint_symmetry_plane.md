A symmetry plane enforces zero solid displacement normal to a user-selected plane. This constraint is prescribed on a deformable surface of the model and is enforced for every node on that surface. It is the user's responsibility to select only planar surfaces.

```
<constraint type="symmetry plane" surface="SymmetryPlane01">
	<laugon>1</laugon>
	<penalty>1e6</penalty>
	<tol>1e-6</tol>
	<minaug>0</minaug>
	<maxaug>50</maxaug>
</constraint>
```

The surface (SymmetryPlane01 in this example), is defined in the `Mesh` section. Let $\mathbf{u}$ denote the nodal displacement vector and let $\mathbf{n}$ denote the unit normal to the plane; the symmetry plane constraint enforces $u_{n}\equiv\mathbf{u}\cdot\mathbf{n}=0$ using a penalty method, optionally with augmented Lagrangian. The reaction force needed to enforce this constraint is evaluated as $\varepsilon u_{n}$, where $\varepsilon$  is the user-specified `penalty` parameter (with units of force per length). To use the augmented Lagrangian method, set `laugon` to 1, and the Lagrange multiplier `\lambda` will be augmented as $\lambda\leftarrow\lambda+\varepsilon u_{n}$. Augmentations terminate when the relative change in $\lambda$  is less than the user-specified tolerance `tol`, or when the number of augmentations exceeds `maxaug`.