A `surface attraction` body force can be used to attract a mesh toward a boundary surface, for the purpose of creating a mesh bias. This can be useful for fluid analyses where a finer mesh is needed in the vicinity of a no-slip boundary. The benefit of this tool over other existing tools for creating a biased mesh is its ability to work with structured and unstructured meshes, as well as linear and higher-order elements.

For each element in the mesh, its shortest distance $r$ to the selected boundary surface is evaluated using a surface projection algorithm. Then, an attractive body force per mass,$\mathbf{b}=s\exp\left(-\frac{r}{\rho}\right)\mathbf{n}$ is evaluated along the unit vector $\mathbf{n}$ directed along the shortest projection distance. Here, $\rho$  is a characteristic boundary layer thickness (`blt`) and s is a scale factor for the body force (`bsf`), whose value may be adjusted relative to account for the stiffness of the elastic solid material assigned to the mesh.

```
<body_load type="surface attraction" elem_set="EB1" surface="PressureLoad1">
    <blt>0.5</blt>
    <bsf lc="1">20</bsf>
    <search_radius>0.1</search_radius>
    <search_tol>0.01</search_tol>
</body_load>
```

Note that this body force requires the specification of an attractive surface; optionally, it also accepts the specification of the element set subjected to this attractive body force. The `search_radius` and `search_tol` parameters are used for the projection algorithm.