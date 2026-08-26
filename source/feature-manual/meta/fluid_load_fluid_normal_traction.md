In a fluid or fluid-FSI analysis, the normal component $t_{n}^{\tau}=\mathbf{t}^{\tau}\cdot\mathbf{n}$ of the viscous traction $\mathbf{t}^{\tau}$ may be prescribed on a boundary surface in a fluid analysis. The fluid normal traction surface load prescribes $t_{n}^{\tau}$ on a boundary surface.

```
<surface_load type="fluid normal traction" surface="surface1">
  <scale lc="1">1.0</scale>
  <traction>1</traction>
</surface_load>
```