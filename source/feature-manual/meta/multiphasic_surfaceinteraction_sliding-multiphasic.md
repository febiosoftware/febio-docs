The `sliding-multiphasic` formulation is similar to the [sliding-biphasic-solute](solute_surfaceinteraction_sliding-biphasic-solute.md). This contact implementation supports multiphasic contact (see below) [^1]. When using multiphasic materials, the non-symmetric version must be used.

The sliding-multiphasic contact interface can deal with multiphasic contact surfaces. These contact interfaces allow for the possibility to track fluid and solute flow across the contact interface. In other words, fluid and solute can flow from one side of the contact interface to the other. To use this feature, the user must define additional contact parameters, namely:

```xml
<pressure_penalty>1.0</pressure_penalty>
<concentration_penalty>1.0</concentration_penalty>
<ambient_pressure>0</ambient_pressure>
<ambient_concentration sol="id">0</ambient_concentration>
```

In the same way that the penalty parameter controls the contact tractions, these penalty parameters control the penalty values that are used to calculate the Lagrange multipliers for the pressure and concentration constraints. If the laugon flag is set, the augmented Lagrangian method is used to enforce the pressure and concentration constraints. And if the auto_penalty flag is defined, an initial guess for the pressure and concentration penalty is calculated automatically using the following formulas: 

\[
varepsilon_{p}=\frac{k\cdot A}{V}\,,\quad\varepsilon_{c}=\frac{d\cdot A}{V}\,,
\]

where $A$ is the element's area, $V$ is the element's volume, $k$ is a measure of the fluid permeability which is defined as one third of the trace of the material's initial permeability tensor, and $d$ is a measure of the solute diffusivity which is defined as one third of the trace of the material's initial diffusivity tensor.

When either contact surface is multiphasic, the surface outside the contact area(s) is automatically set to ambient conditions (equivalent to setting the effective fluid pressure and effective solute concentration to the <ambient_pressure> and <ambient_concentration> values, respectively). Ambient conditions may also be associated with a load curve, for example:

```xml
<ambient_pressure lc="2">1.0</ambient_pressure>
<ambient_concentration lc="3">1.0</ambient_concentration>
```

When performing multiphasic-on-rigid contact, a two-pass analysis should not be used; the rigid surface should be the secondary surface.

[^1]: Ateshian, Gerard A, Maas, Steve, and Weiss, Jeffrey A, "Solute transport across a contact interface in deformable porous media", J Biomech 45, 6 (2012), pp. 1023-7.
