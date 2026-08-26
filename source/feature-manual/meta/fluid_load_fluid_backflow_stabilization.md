In a fluid or fluid-FSI analysis, this boundary condition prescribes the normal component of the viscous traction, $t_{n}^{\tau}=\mathbf{t}^{\tau}\cdot\mathbf{n}$, such that it opposes backflow, i.e., when $v_{n}=\mathbf{v}\cdot\mathbf{n}$ is negative. Specifically, $t_{n}^{\tau}=\beta\rho_{r}v_{n}^{2}$ when $v_{n}<0$ and $0$ otherwise, where $\beta$  is a unitless user-defined parameter (typical values may range from 0 to 1) and $\rho_{r}$ is the referential fluid density.

```
<surface_load type="fluid backflow stabilization" surface="surface1">
	<beta lc="1">1</beta>
</surface_load>
```