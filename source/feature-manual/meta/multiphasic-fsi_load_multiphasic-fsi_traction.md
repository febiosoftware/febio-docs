In a fluid-FSI analysis, the fluid traction across an interface between a multiphasic-FSI material and a solid domain must be prescribed explicitly as a traction boundary condition on the solid domain. Otherwise, the solid domain cannot sense the fluid pressure and viscous traction. Users must identify each surface on which this FSI surface load must be prescribed. There are no user-defined parameters for this surface load.

```
<surface_load type="multiphasic-FSI traction" surface="surface1">
<surface_load>
```

This surface load must also be prescribed on free fluid surfaces (such as the surface of the fluid in open channel flow) to allow those surfaces to deform in response to the fluid stresses (e.g., producing surface waves). (Do not apply this surface load on inlet or outlet boundaries through which fluid flows.)