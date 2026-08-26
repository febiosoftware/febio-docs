The `sliding-elastic` contact interface uses facet-on-facet contact. It can be used for frictionless or frictional contact. It may optionally be set to sustain tension to prevent contact surfaces from separating along the direction normal to the interface, while still allowing tangential sliding. This method sometimes performs better than the other sliding contact formulations for problems that are dominated by compression. 

### control parameters
Several parameters control the behavior of the algorithm.

* `fric_coeff` : friction is enabled by setting this parameter to a nonzero value. 

* `tension` : when enabled, the surface can no longer separate, but they are still allowed to slide across one another. 

* `node_reloc` : turns this option on if you want the initial projection to move the nodes on the primary surface so that they do not cross into the secondary surface. 

* `symmetric_stiffness` : The formulation is inherently non-symmetric. A symmetrized version of this implementation is available by setting the `symmetric_stiffness` flag to 1, but the symmetric version does not converge as well as the non-symmetric version.

### contact enforcement
Like most contact formulations in FEBio, the contact constraint for the sliding-elastic is enforced using the augmented Lagrangian method (ALM). 

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

* `seg_up` : sets the maximum number of segment updates (i.e. projection onto the secondary surface). Once this limit is reached, the projected points are assumed to "stick" to the secondary surface. By default, this feature is disabled, but enabling it can sometimes help the models' convergence. 

* `two_pass` : when enabled, the projection (and force calculations) are done twice. After the first pass, the second pass swaps the primary and secondary surfaces, and then runs again. 

### contact with shells

When this contact interface is used with shells, it is important to pay attention to the orientation of the shell surfaces. For this contact to work, the contacting surface must be oriented so that they face each other. If this is not the case, you can use the following flags to orient the surfaces correctly.

* `flip primary` / `flip secondary` : when enabled, this will flip the orientation of the corresponding surface. 

* `shell_bottom_primary` / `shell_bottom_secondary` : this flag indicates that the bottom of the shell must be used as the contacting surface. 
