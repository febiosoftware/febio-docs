A `tied-node-on-facet` interface can be used to connect two non-conforming surfaces [^1]. A tied interface requires the definition of both a primary and a secondary surface. For this particular formulation it is assumed that the nodes of the primary surface are connected to the faces of the secondary surface. The formulation is inherently symmetric.

### control parameters
Several parameters control the behavior of the algorithm.

* `symmetric_stiffness` : The formulation is inherently non-symmetric. A symmetrized version of this implementation is available by setting the `symmetric_stiffness` flag to 1, but the symmetric version does not converge as well as the non-symmetric version.

### contact enforcement
Like most contact formulations in FEBio, the contact constraint for this formulation is enforced using the augmented Lagrangian method (ALM). This particular formulation also supports a true Lagrange Multiplier method by setting the `laugon` parameter to 2. 

The following parameters affect the ALM. 

* `laugon` : this enables or disables the AML. When disabled, a standard penalty method is used. (When set to 2, a Lagrange Multiplier method is used instead.)

* `penalty`: the penalty factor used to enforce the constraint.

* `tolerance`: the tolerance on the approximate Lagrange multiplier norm and used as a termination criterion for the augmentations. 

* `minaug` : sets the minimum number of augmentations that will be done when augmentations are enabled (i.e. `laugon` is 1).

* `maxaug` : sets the maximum number of augmentations that will be done when augmentations are enabled. 

### contact projection

The formulation identifies contact pairs by using a closest point projection method. For each integration point on the primary surface, the closest point on the secondary surface is found. There are several parameters that influence how the projection works. 

* `search_tol` : this sets the tolerance on the search for finding the isoparametric coordinates of the projected point onto a secondary surface facet. 

* `offset_shells` : when enabled, takes the shell thickness into account when calculating the contact gap. 


[^1]:Laursen, T. A. and Simo, J. C., "Continuum-based finite element formulation for the implicit solution of multibody, large deformation frictional contact problems", International Journal for Numerical Methods in Engineering 36, 20 (1993), pp. 3451-3485.