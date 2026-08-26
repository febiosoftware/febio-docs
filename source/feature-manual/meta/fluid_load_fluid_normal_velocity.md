In a fluid or fluid-FSI analysis the fluid velocity relative to the mesh, $\mathbf{w}$, on a boundary surface with outward normal $\mathbf{n}$ may be decomposed into the normal component, $w_{n}=\mathbf{w}\cdot\mathbf{n}$, and tangential component, $\mathbf{w}_{\tau}=\left(\mathbf{I}-\mathbf{n}\otimes\mathbf{n}\right)\cdot\mathbf{w}=\mathbf{w}-w_{n}\mathbf{n}$. The surface load fluid normal velocity may be used to prescribe a desired value of $w_{n}$ on a boundary surface.

```
<surface_load type="fluid normal velocity" surface="surface1">
  <value lc="1">1.0</value>
  <velocity>1</velocity>
</surface_load>
```

Optionally, FEBio can generate a parabolic velocity profile over the named surface, This option can be turned on using the `parabolic` parameter (0=default, 1=parabolic). In this case, the `velocity` parameter provides the average value of this parabolic velocity profile, while value remains a scale factor optionally tied to a load controller. The parabolic profile is calculated under the assumption of steady Poiseuille flow in an infinite tube whose cross-section has the shape of the named surface. The parabolic velocity distribution reduces to zero only on portions of the boundary curve of the named surface where the user has fixed all three components of the fluid velocity (no-slip condition). On remaining portions of this boundary curve, symmetry conditions are assumed for the three-dimensional parabolic normal velocity profile.

```
<surface_load type="fluid normal velocity" surface="surface1">
  <velocity lc="1">-1.0</velocity>
  <parabolic>1</parabolic>
</surface_load>
```

If an arbitrary distribution with different scalar value needs to be specified for each facet, use the following syntax,

```
<surface_load type="fluid normal velocity" surface="surface1">
  <value surface_data="inlet"/>
  <velocity lc="1">-1.0</value>
</surface_load>
```

and provide the facet values in a user-defined SurfaceData map with name="inlet" and data_type="scalar".

By default, this condition only prescribes the natural boundary condition $w_{n}$, leaving $\mathbf{w}_{\tau}$ free. Optionally, it is possible to also enforce $\mathbf{w}_{\tau}=\mathbf{0}$ by prescribing essential boundary conditions on the wx, wy and wz components of $\mathbf{w}=w_{n}\mathbf{n}$ at the nodes of each facet, based on the value of $\mathbf{n}$ at each node (obtained by averaging $\mathbf{n}$ from adjoining facets). This option may be turned on using the `prescribe_nodal_velocities` parameter (0=default, 1=prescribed), for example,

```
<surface_load type="fluid normal velocity" surface="surface1">
  <velocity>-1.0</velocity>
  <prescribe_nodal_velocities>1</prescribe_nodal_velocities>
</surface_load>
```

When the fluid is prescribed on a surface boundary, better numerical convergence is achieved if the fluid dilatation is also prescribed on the rim (the boundary curve) of that surface boundary. While this can be done explicitly, a better option is to set the fluid dilatation on the rim to match the average pressure on the surface boundary, calculated during the analysis. To select this option, use the `prescribe_rim_pressure` parameter (0=default, 1=prescribed), for example,

```
<surface_load type="fluid normal velocity" surface="surface1">
  <velocity>-1.0</velocity>
  <parabolic>1</parabolic>
  <prescribe_nodal_velocities>1</prescribe_nodal_velocities>
  <prescribe_rim_pressure>1</prescribe_rim_pressure>
</surface_load>
```

Note that this `prescribe_rim_pressure` option will not work if the mesh of the boundary surface has no internal nodes.
