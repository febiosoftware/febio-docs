A traction load applies a traction to a surface. The direction of the traction remains unchanged as the mesh deforms.

```
<surface_load type="traction" surface="surface1">
  <scale lc="1">1.0</scale>
  <traction>0,0,1</traction>
</surface_load>
```

The traction vector is determined by two quantities. The direction and magnitude is defined by the traction element. In addition, the magnitude can be scaled using the scale element. An optional load curve can be defined for the scale element using the lc attribute. This allows the traction load to become time dependent. If the lc attribute is omitted a constant traction load is applied.