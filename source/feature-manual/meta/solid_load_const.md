This constant body force per mass $\mathbf{b}$ is defined as a 3D vector. Each component can be associated with a load controller to define a time dependent body force. Only the non-zero components need to be defined. This type of body force is spatially homogeneous, though it may vary with time when associated with a load controller:

```
<body_load type="const">
  <x lc="1">1.0</x>
  <y lc="2">1.0</y>
  <z lc="3">1.0</z>
</body_load>
```

The `lc` attribute defines the load controller to use for the corresponding component. The values of the components can be used to define scale factors for the load values.
