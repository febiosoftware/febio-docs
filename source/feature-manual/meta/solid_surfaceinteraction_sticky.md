A sticky interface is similar to a tied interface except that it allows for initial separation of the tied surfaces and breaking of the tie after a user-defined normal traction is exceeded. The tie is only applied when the surfaces contact and sustained as long as the normal traction is less than the threshold.

The `max_traction` parameter can be used to break the tied interface after the normal traction exceeds the specified value. Initially, this value is set to zero, in which case FEBio will ignore this value and the tie cannot be broken. 

The `snap_tol` parameter is used in determining the minimum distance that a primary surface node must have approached the secondary surface facet in order to snap onto the secondary surface. The initial value is zero, meaning a node must have penetrated the secondary surface before it will be tied to it. 

