# sliding-multiphasic

**Module:** multiphasic

**Category:** surfaceinteraction

**Type string:** `"sliding-multiphasic"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `laugon` | Enforcement method | 0 | $[0, 1]$ |  |
| `tolerance` | tolerance | 0.1 | $\in \mathbb{R}$ |  |
| `gaptol` | gaptol | 0 | $\in \mathbb{R}$ | L |
| `ptol` | ptol | 0 | $\in \mathbb{R}$ |  |
| `ctol` | ctol | 0 | $\in \mathbb{R}$ |  |
| `penalty` | penalty | 1 | $\in \mathbb{R}$ |  |
| `auto_penalty` | auto_penalty | false | $\{0, 1\}$ |  |
| `update_penalty` | update_penalty | false | $\{0, 1\}$ |  |
| `two_pass` | two_pass | false | $\{0, 1\}$ |  |
| `knmult` | knmult | 1 | $\in \mathbb{Z}$ |  |
| `search_tol` | search_tol | 0.01 | $\in \mathbb{R}$ |  |
| `pressure_penalty` | pressure_penalty | 1 | $\in \mathbb{R}$ |  |
| `concentration_penalty` | concentration_penalty | 1 | $\in \mathbb{R}$ |  |
| `symmetric_stiffness` | symmetric_stiffness | true | $\{0, 1\}$ |  |
| `search_radius` | search_radius | 1 | $\in \mathbb{R}$ | L |
| `seg_up` | seg_up | 0 | $\in \mathbb{Z}$ |  |
| `node_reloc` | node_reloc | false | $\{0, 1\}$ |  |
| `fric_coeff` | fric_coeff | 0 | $\in \mathbb{R}$ |  |
| `contact_frac` | contact_frac | 0 | $\in \mathbb{R}$ |  |
| `smooth_aug` | smooth_aug | false | $\{0, 1\}$ |  |
| `smooth_fls` | smooth_fls | true | $\{0, 1\}$ |  |
| `minaug` | minaug | 0 | $\in \mathbb{Z}$ |  |
| `maxaug` | maxaug | 10 | $\in \mathbb{Z}$ |  |
| `ambient_pressure` | ambient_pressure | 0 | $\in \mathbb{R}$ |  |
| `ambient_concentration` | ambient_concentration |  | N/A |  |


## Description

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

