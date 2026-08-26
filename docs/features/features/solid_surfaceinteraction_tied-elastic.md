# tied-elastic

**Module:** solid

**Category:** surfaceinteraction

**Type string:** `"tied-elastic"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `laugon` | Enforcement method | 0 | $[0, 1]$ |  |
| `tolerance` | tolerance | 0.1 | $\in \mathbb{R}$ |  |
| `gaptol` | gaptol | -1 | $\in \mathbb{R}$ |  |
| `penalty` | penalty | 1 | $\in \mathbb{R}$ |  |
| `auto_penalty` | auto_penalty | false | $\{0, 1\}$ |  |
| `update_penalty` | update_penalty | false | $\{0, 1\}$ |  |
| `two_pass` | two_pass | false | $\{0, 1\}$ |  |
| `knmult` | knmult | 1 | $\in \mathbb{Z}$ |  |
| `search_tol` | search_tol | 0.01 | $\in \mathbb{R}$ |  |
| `symmetric_stiffness` | symmetric_stiffness | true | $\{0, 1\}$ |  |
| `search_radius` | search_radius | 1 | $\in \mathbb{R}$ |  |
| `minaug` | minaug | 0 | $\in \mathbb{Z}$ |  |
| `maxaug` | maxaug | 10 | $\in \mathbb{Z}$ |  |
| `flip_primary` | flip_primary | false | $\{0, 1\}$ |  |
| `flip_secondary` | flip_secondary | false | $\{0, 1\}$ |  |


## Description

A `tied elastic` contact interface can be used for tying surfaces of two solid parts. It enforces continuity of the displacement across the interface.

### control parameters
Several parameters control the behavior of the algorithm.

* `symmetric_stiffness` : The formulation is inherently non-symmetric. A symmetrized version of this implementation is available by setting the `symmetric_stiffness` flag to 1, but the symmetric version does not converge as well as the non-symmetric version.

### contact enforcement
Like most contact formulations in FEBio, the contact constraint for this formulation is enforced using the augmented Lagrangian method (ALM).

The following parameters affect the ALM. 

* `laugon` : this enables or disables the AML. When disabled, a standard penalty method is used. 

* `penalty`: the penalty factor used to enforce the constraint.

* `tolerance`: the tolerance on the approximate Lagrange multiplier norm and used as a termination criterion for the augmentations. 

* `gaptol` : the tolerance in the maximum allowed gap distance between the contacting surface. A value of zero disables this termination criterion. 

* `auto_penalty` : when enabled, this option will calculate an initial value for the penalty factor that depends on element size and material stiffness. When this flag is enabled, the `penalty` parameter is a scale factor that scales the auto-penalty values. 

* `update_penalty` : when enabled, the auto-penalty calculation will run at the start of each time step. This can sometimes be helpful for materials that significantly stiffen or soften during the analysis. 

* `minaug` : sets the minimum number of augmentations that will be done when augmentations are enabled (i.e. `laugon` is 1).

* `maxaug` : sets the maximum number of augmentations that will be done when augmentations are enabled. 

* `smooth_aug` : enables the smoothed Lagrangian option, which "smooths" the approximate Lagrange multipliers at each augmentation. 

### contact projection

The formulation identifies contact pairs by using a contact projection method. For each integration point on the primary surface, a ray is projected onto the secondary surface along the local normal of the primary surface. There are several parameters that influence how the projection works. 

* `search_tol` : this sets the tolerance on the search for finding the isoparametric coordinates of the projected point onto a secondary surface facet. 

* `search_radius` : this parameter sets the maximum distance to find contact pairs. Contact is only established if the primary point and secondary point are within this distance. 

* `two_pass` : when enabled, the projection (and force calculations) are done twice. After the first pass, the second pass swaps the primary and secondary surfaces, and then runs again. 

### contact with shells

When this contact interface is used with shells, it is important to pay attention to the orientation of the shell surfaces. For this contact to work, the contacting surface must be oriented so that they face each other. If this is not the case, you can use the following flags to orient the surfaces correctly.

* `flip primary` / `flip secondary` : when enabled, this will flip the orientation of the corresponding surface. 

