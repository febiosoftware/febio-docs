The `periodic boundary` interface enforces the constraint that maintains the relative displacement between two surfaces.

The constraint is enforced using the augmented Lagrangian method, which is controlled by the following parameters. 

* `laugon` : Enables or disables augmented Lagrangian. When disabled, a penalty method is enforced. 
* `penalty` : the penalty factor
* `tolerance` : the convergence tolerance used for the augmentations.
* `minaug` : the minimum number of augmentations. 

In addition, the following parameters can be specified. 

* `offset` : adds an additional offset to the relative displacement. By attaching a loadcontroller to this parameter, the relative distance can be increased or decreased over time. 

* `two_pass` : when enabled, the constraint is enforced twice and for the second pass the primary and secondary surfaces are swapped. 
