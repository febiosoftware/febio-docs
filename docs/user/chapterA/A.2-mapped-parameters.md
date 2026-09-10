# A.2 Mapped parameters

For mapped parameters, use the attribute type=“map”. In this case, the value of the parameter is the name of the map that is defined in the MeshData section.

```
<material id="1" name="my_material" type="neo-Hookean">
  <E type="map">map_E</E>
  <v>0.3</v>
</material>
```

The map is defined in the MeshData section.

```
<ElementData name="map_E" elem_set="Part1">
  <elem lid="1">1.23</elem>
  <elem lid="2">4.56</elem>
</ElementData>
```

Note that it is also possible to use maps in mathematical expressions.

```
<material id="1" name="my_material" type="neo-Hookean">
  <E type="math">5.0*map_E</E>
  <v>0.3</v>
</material>
```
