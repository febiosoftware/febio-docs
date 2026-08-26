In a fluid or fluid-FSI analysis, this boundary condition prescribes the fluid velocity vector relative to the mesh, $\mathbf{w}$, on a named surface, simultaneously satisfying the natural boundary condition for $w_{n}=\mathbf{w}\cdot\mathbf{n}$ and prescribing essential boundary conditions on the wx, wy and wz components of $\mathbf{w}$ at the nodes of each facet, based on the value of $\mathbf{n}$ at each node (obtained by averaging $\mathbf{n}$ from adjoining facets).

```
<surface_load type="fluid velocity" surface="surface1">
  <scale lc="1">1.0</scale>
  <velocity>0,0,1</velocity>
</surface_load>
```

If a different vector value needs to be specified for each facet, use the following syntax,

```
<surface_load type="fluid velocity" surface="surface1">
  <scale lc="1">1.0</scale>
  <velocity surface_data="inlet"/>
</surface_load>
```

and provide the facet values in a user-defined SurfaceData map with name="inlet" and data_type="vec3".