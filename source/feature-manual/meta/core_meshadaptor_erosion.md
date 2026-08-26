The `erosion` adaptor can be used to deactivate elements in a mesh, based on a user-defined criterion.

The `erode_surfaces` parameter sets the policy of handling surface facets that attach to eroded elements. The value can be set to one of the following values:

* `no`: don't erode surfaces (default)
* `yes`: erode surfaces if the underlying element is eroded. 
* `grow`: add the newly exposed facets of eroded elements to the surface. 
* `reconstruct`: reconstruct surface. This only works if the surface is defined via a part. 

_Example:_
In this example, elements that have an (integration point averaged) effective stress larger than 0.3, are eroded. Only three elements are eroded per adaptation cycle.

```xml
<mesh_adaptor type="erosion"> 
  <max_iters>1</max_iters>
  <max_elems>3</max_elems>
  <sort>1</sort>
  <criterion type="min-max filter">
    <min>0.3</min>
    <clamp>0</clamp>
    <data type="stress"/>
  </criterion>
</mesh_adaptor>
```
