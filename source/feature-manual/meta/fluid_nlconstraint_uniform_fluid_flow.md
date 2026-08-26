When an inlet boundary is subjected to a prescribed fluid pressure, the profile of the inlet fluid velocity remains unconstrained, and this lack of constraint often leads to poor numerical performance due to the production of velocity spikes. To avoid this problem, use this `uniform fluid velocity` constraint to help stabilize inlet conditions along the direction normal to the boundary. This constraint evaluates the average fluid velocity normal to the selected boundary, $\bar{v}_{n}$, then prescribes a linear constraint at every node such that $\mathbf{v}\cdot\mathbf{n}=\bar{v}_{n}$ is enforced. For example,

```
<constraint name="UniformFluidFlow1" surface="UniformFluidFlow1" type="uniform fluid flow">
	<laugon>0</laugon>
	<tol>0.1</tol>
	<penalty>10000</penalty>
	<minaug>0</minaug>
	<maxaug>50</maxaug>
</constraint>
```

If a very strong enforcement of this constraint is desired, increase the `penalty` and/or turn Lagrange augmentation on (`laugon`=1). This constraint is not compatible with boundary conditions that prescribe the normal component of the fluid velocity on that same boundary.