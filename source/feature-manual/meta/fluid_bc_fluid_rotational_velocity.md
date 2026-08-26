This boundary condition prescribes a rotational velocity on an axisymmetric surface. It is the user's responsibility to ensure that the surface is axisymmetric. The angular velocity $\boldsymbol{\omega}=\omega\mathbf{n}$ is prescribed by specifying the angular speed $\omega$  and the unit vector along the axis of rotation (axis of symmetry) $\mathbf{n}$. The user-defined vector $\mathbf{n}$ is automatically normalized. If the axis does not pass through the origin, the user may specify any point $\mathbf{p}$ on the axis. The fluid velocity relative to the mesh, $\mathbf{w}$, for nodes on the selected surface is evaluated from $\mathbf{w}=\boldsymbol{\omega}\times\mathbf{r}$, where $\mathbf{r}=\left(\mathbf{I}-\mathbf{n}\otimes\mathbf{n}\right)\cdot\left(\mathbf{x}-\mathbf{p}\right)$ is the shortest vector from the axis to the node and $\mathbf{x}$ is the nodal position.

```
<surface_load type="fluid rotational velocity" surface="FluidRotationalVelocity01">
	<angular_speed lc="1">1</angular_speed>
	<axis>0,0,1</axis>
	<origin>0,0,0</origin>
</surface_load>
```

Though this boundary condition may be used in fluid-FSI analyses, it is most relevant for standard fluid analyses where the mesh is stationary.