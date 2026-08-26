# tied-facet-on-facet

**Module:** solid

**Category:** surfaceinteraction

**Type string:** `"tied-facet-on-facet"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `laugon` | Enforcement method | 0 | $[0, 1]$ |  |
| `tolerance` | tolerance | 0.01 | $\in \mathbb{R}$ |  |
| `penalty` | penalty | 1 | $\in \mathbb{R}$ |  |
| `minaug` | minaug | 0 | $\in \mathbb{Z}$ |  |
| `maxaug` | maxaug | 10 | $\in \mathbb{Z}$ |  |
| `search_tolerance` | search_tolerance | 0.0001 | $\in \mathbb{R}$ |  |
| `gap_offset` | gap_offset | false | $\{0, 1\}$ |  |


## Description

A `tied-facet-on-facet` contact interface can be used for tying the surfaces of two solid parts. It enforces continuity of the displacement across the interface. This formulation is inherently symmetric. 


### contact enforcement
Like most contact formulations in FEBio, the contact constraint for this formulation is enforced using the augmented Lagrangian method (ALM).

The following parameters affect the ALM. 

* `laugon` : this enables or disables the AML. When disabled, a standard penalty method is used. 

* `penalty`: the penalty factor used to enforce the constraint.

* `tolerance`: the tolerance on the approximate Lagrange multiplier norm and used as a termination criterion for the augmentations. 

* `minaug` : sets the minimum number of augmentations that will be done when augmentations are enabled (i.e. `laugon` is 1).

* `maxaug` : sets the maximum number of augmentations that will be done when augmentations are enabled. 


### contact projection

The formulation identifies contact pairs by using a closest point projection method. For each integration point on the primary surface, the closest point on the secondary surface is found . There are several parameters that influence how the projection works. 

* `search_tol` : this sets the tolerance on the search for finding the isoparametric coordinates of the projected point onto a secondary surface facet. 

* `gap_offset` : specifies an additional offset that is taken into account when calculating the contact gap. 

