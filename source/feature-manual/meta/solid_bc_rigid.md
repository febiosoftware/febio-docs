A node set can be attached to a rigid body using the `rigid` boundary condition. Rigid nodes are not assigned degrees of freedom.

```
<bc type="rigid" node_set="set1">
  <rb>2</rb>
</bc>
```

The `rb` parameter defines the material (which must be a `rigid body` material) that in turn defines the rigid body. The node set must be defined in the `Mesh` section.