The `sliding-facet-on-facet` contact formulation allows users to model contact between two surfaces. The surfaces can make contact, slide frictionless across each other, and separate. This contact formulation uses Gaussian quadrature to integrate the contact equations. This formulation is inherently symmetric. 

This formulation is mostly retained for backward compatibility. In general, it is advised to use the [sliding-elastic](solid_surfaceinteraction_sliding-elastic.md) contact interface. 

### control parameters
Several parameters control the behavior of the algorithm.

* `node_reloc` : turns this option on if you want the initial projection to move the nodes on the primary surface so that they do not cross into the secondary surface. 

* `knmult` : sets the stiffness scale factor for one of the components of the stiffness matrix.

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

The formulation identifies contact pairs by using a closest point projection method. For each integration point on the primary surface, the closest point on the secondary surface is sought. There are several parameters that influence how the projection works. 

* `search_tol` : this sets the tolerance on the search for finding the isoparametric coordinates of the projected point onto a secondary surface facet. 

* `search_radius` : this parameter sets the maximum distance to find contact pairs. Contact is only established if the primary point and secondary point are within this distance. 

* `seg_up` : sets the maximum number of segment updates (i.e. projection onto the secondary surface). Once this limit is reached, the projected points are assumed to "stick" to the secondary surface. By default, this feature is disabled, but enabling it can sometimes help the models' convergence. 

* `two_pass` : when enabled, the projection (and force calculations) are done twice. After the first pass, the second pass swaps the primary and secondary surfaces, and then runs again. 
