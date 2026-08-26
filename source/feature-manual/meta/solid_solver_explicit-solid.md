!!! warning
    Please note that the explicit-solver is still considered an experimental feature in FEBio and may not work correctly with all of the features of FEBio yet. Use at your own risk and please report any problems you may encounter to the FEBio developers. 

FEBio supports an explicit-solid solver, which solves dynamic structural mechanics problems using an explicit time-integration scheme. This means that the solution at a given timestep is calculated using only the solution from the previous timestep. The advantage of this approach is that no stiffness matrix needs to be calculated and no linear system of equations needs to be solved (at least, with mass-lumping enabled). As a result, this solver can solve dynamic problems very fast. However, the downside of this approach is that it is only conditionally stable and imposes an upper limit on the time step size. This limit is often much smaller than the time step sizes that can be taken by implicit time-integration schemes (as used by the default Newton-based solvers in FEBio) and thus often will require many more time steps to solve the model. Thus, the explicit solver is most useful in dynamic problems that already require relatively small time step sizes, such as impact-contact models, or models that use non-elastic material behavior that may undergo rapid changes in their constitutive behavior (e.g. damage). 

The explicit solver in FEBio uses the midpoint time integration rule and uses mass lumping. Mass lumping is a technique that replaces the consistent mass matrix with a diagonal approximation. In fact, it's this diagonalization of the mass matrix that really prevents the need to solve a linear system of equations. (Since solving a diagonal linear system of equations is trivial.) 

The explicit solver can be selected by setting the `type` attribute of the `solver` element to `explicit-solid`.

_Example_:
```xml
<solver type="explicit-solid">
  ...
 </solver>
```

As mentioned, mass lumping is a technique to approximate the mass matrix with a diagonal matrix. Several approaches are supported in FEBio and can be selected by setting the `mass_lumping` parameter. 

* `mass_lumping` = 0: no mass-lumping (This is currently not implemented, but the value is reserved in case support will be added in the future.) 
* `mass_lumping` = 1 : use row summation approach. Useful for linear elements, but may produce negative nodal masses for quadratic elements and thus should not be used for models containing higher-order elements.
* `mass_lumping` = 2: HRZ lumping technique. Better suited for higher-order elements, but should not be used for shells.


Dynamic damping is a technique to dampen the solution in order to obtain an equilibrium solution (e.g. for false-transient analyses). In FEBio, dynamic damping is applied to the velocity updates and the `dyn_damping` parameter specifies the damping factor. The default value is 1 so no damping is applied. Note that the lower the damping factor, the more damping, but also the longer it may take to find the equilibrium solution.
