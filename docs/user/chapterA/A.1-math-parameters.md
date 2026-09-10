# A.1 Math parameters

Many model parameters can be made dependent on the reference coordinates. This is useful, for instance, for defining inhomogeneous materials, where some material parameters depend on the spatial position.

There are two mechanisms for creating heterogeneous parameters: a mathematical expression, or a map. The type of the parameter is set via the _type_ attribute, which can take on two values.

<div markdown="1" style="display: flex; justify-content: center;">

| **type** | **description** |
|---|---|
| math | Define a math parameter via a mathematical expression |
| map | Define a mapped parameter |
| const | Define a constant parameter (default) |

</div>

The two types of parameters are described in more detail in the sections below.

The _type_ attribute can be omitted. In that case, it is assumed to be a const parameter, unless the tag's value is not a number. In that case, it is assumed to be a math parameter.

FEBio performs parameter validation at the start of an analysis where the values of parameters are checked against the valid ranges as defined in the code. However, it is important to keep in mind that this validation is only performed on constant parameters. For math and map parameters, it is up to the user to ensure that all values over the relevant mesh partition are valid.

For math parameters, add the type=”math” attribute to the parameter's definition. The value of the parameter tag can then be any mathematical expression. The upper case letters X, Y, Z, are used to denote material coordinates. The letter _t_ denotes time. The algebraic operators +, -, *, /, ^ are supported, as well as the list of functions listed in Appendix C.

```
<material id="1" name="my_material" type="neo-Hookean">
  <E type="math">X+Y+Z</E>
  <v>0.3</v>
</material>
```

You can also use the component's other parameters inside mathematical expressions.

```
<material id="1" name="my_material" type="neo-Hookean">
  <density>1.0</density>
  <E type="math">2*density+0.1</E>
  <v>0.3</v>
</material>
```

The names of maps are also allowed in mathematical expressions. For instance, assume that a map, named “E_map” is defined in the MeshData section. Then the following is a valid mathematical expression.

```
<E type="math">2*E_map+X</E>
```
