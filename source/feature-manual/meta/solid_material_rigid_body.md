A rigid body can be defined using the rigid material model. The material type for a rigid body is `rigid body`.

If the `center_of_mass` parameter is omitted, FEBio will calculate the center of mass automatically. In this case, a `density` must be specified. If the `center_of_mass` is defined the `density` parameter may be omitted. Omitting both will generate an error message.

The Young's modulus $E$ and Poisson ratio $v$ currently have no effect on the results. The only place where they are used is in the calculation of a material stiffness for some auto-penalty contact formulation. If you are using contact it is advised to enter sensible values. Otherwise these parameters may be omitted.

The degrees of freedom of a rigid body are initially unconstrained. This implies that a rigid body is free to move in all three directions and rotate about any of the coordinate axes. 

_Example:_
```xml
<material id="1" type="rigid body">
  <density>1.0</density>
  <center_of_mass>0,0,0</center_of_mass>
</material>
```
