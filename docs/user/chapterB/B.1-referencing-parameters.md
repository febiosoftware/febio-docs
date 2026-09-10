# B.1 Referencing Parameters

This appendix details how that model parameters can be referenced in the FEBio input files. This is used to

- write model parameters to the output file.

- reference model parameters in the parameter optimization input file.

The general format follows the following rule:

```
fem.property.property...property.parameter.component
```

Properties and parameters are referenced by tags separated by a periods. The first tag must be the _fem_ tag, which serves as the name of the model. (In future version this name can be user defined, but for now is fixed). Next, the name of a model property must follow. The following properties are currently defined:

- **material**: references a material, defined in the _Material_ section.

- **bc_fixed**: references a fixed bc, defined in the _Boundary_ section.

- **bc_prescribed**: references a prescribed bc, defined in the _Boundary_ section.

- **nodal_load**: references a nodal load, defined in the _Loads_ section.

- **surface_load**: references a surface load, defined in the _Loads_ section.

- **body_load**: references a body load, define in the _Loads_ section.

- **rigid_body**: references a rigid body. Rigid bodies are defined implicitly via rigid materials.

All of these properties define arrays. A specific property can be referenced via square brackets. For instance, to reference the first material in the model, do this

```
fem.material[0]
```

Alternatively, a property can also be reference by name or by ID. In either case, use round brackets. For instance, to reference by ID, do

```
fem.material(1)
```

The ID refers to the “id” attribute that can be specified for most model components. To reference by name,

```
fem.material('MyMaterial')
```

Note the single quotes around the material name. The name is defined via the “name” attribute.

Note that rigid bodies can only be referenced via their material name.

```
fem.rigidbody('MyRigidMaterial')
```

Each property can have a list of parameters and sub-properties. To reference a parameter, just end the reference string with the name of the parameter. For example,

```
fem.material[0].E
```

Sub-properties are referenced similarly. For example, assume that the first material is a biphasic material that defines the solid property.

```
fem.material[0].solid.E
```

If the parameter itself is an array, a specific item in the array is referenced using square brackets. For example, for an EFD-neo Hookean material,

```
fem.material[0].ksi[0]
```

In cases where the model parameter does not define a scalar it is possible to reference the components of the parameter. For instance, a vec3 parameter defines an x, y, and z component.

```
fem.body_load[0].force.x
```

Nodal positions can also be referenced using the _mesh_ property.

```
fem.mesh.node[0].position.x
```

In certain applications (e.g. optimization), it is also possible to reference output data, i.e. data that is normally used in the logfile section of the input file. This data is considered read-only. For example, the following references the 'sx' (xx-stress) of element with id 1.

```
fem.element_data('sx', 1)
```

Another example evaluates the enclosed volume of a surface (assuming the surface is closed).

```
fem.surface_data('volume', 'SomeSurface1')
```
