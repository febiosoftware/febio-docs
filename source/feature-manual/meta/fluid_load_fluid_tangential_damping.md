The `fluid tangential damping` prescribes a shear traction that opposes tangential fluid velocity on a boundary surface. This can help stabilize inflow conditions.

```
<surface_load type="fluid tangential damping" surface="surface1">
	<penalty>1</penalty>
</surface_load>
```