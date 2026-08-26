In a fluid or fluid-FSI analysis, this boundary condition prescribes the tangential component of the viscous traction, $\mathbf{t}_{t}^{\tau}=\left(\mathbf{I}-\mathbf{n}\otimes\mathbf{n}\right)\cdot\mathbf{t}^{\tau}$, such that it opposes the tangential fluid flow $\mathbf{v}_{t}=\left(\mathbf{I}-\mathbf{n}\otimes\mathbf{n}\right)\cdot\mathbf{v}$ on the selected boundary surface, with $\mathbf{n}$ representing the outward normal to this surface. Specifically, $\mathbf{t}_{t}^{\tau}=-\beta\rho_{r}\left|\mathbf{v}_{t}\right|\mathbf{v}_{t}$, where $\beta$ is a unitless user-defined parameter (typical values may range from 0 to 1) and $\rho_{r}$ is the referential fluid density.

```
<surface_load type="fluid tangential stabilization" surface="surface1">
	<beta lc="1">1</beta>
</surface_load>
```