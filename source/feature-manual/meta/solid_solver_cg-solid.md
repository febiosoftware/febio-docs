The nonlinear conjugate gradient solver, CG-solid, is an alternative solution algorithm for static solid mechanics problems. It does not currently support dynamic problems, fluids, etc. This solver has advantages in several situations: 

• It uses much less memory and therefore allows bigger problems to be solved on a given computer than the standard Newton-based solvers

• Its performance scales better for large problems and it may be faster for very large problems (but see the limitations below); 

• For nonlinear problems with buckling or other instabilities it can converge much more reliably than the standard solver; 

• For many problems it will converge in a single timestep. 

However, it also has some disadvantages: 

• For small models it is typically slower than the BFGS solver; 

• Although it usually converges in a single timestep, it requires a much larger number of iterations to do so. It is therefore inefficient if many timesteps are needed to produce intermediate results or follow the progression of a problem;

• The number of iterations it requires to converge is proportional to the number of elements across the longest dimension of the mesh. It therefore performs best for compact problems with similar numbers of elements in each direction. For example a cube with equal numbers of elements in each direction would solve much faster than a flat sheet or a long, thin beam with the same total number of elements; 

• It does not currently work well for shell elements or freely moving rigid bodies. The way it works is quite different from the Newton-based solver and the problem may need to be defined differently for optimum results: 

• The convergence criteria in FEBio measure the change in the solution on each iteration as a fraction of the total change for the timestep. Because the CG solver converges in a much larger number of smaller steps, the convergence criteria must be set smaller than for the BFGS solver. The default values are dtol=1e-6 and etol=0.001, but it may be necessary to reduce these further to ensure full convergence. Check the solution carefully to make sure that it is correct and reduce dtol further if necessary.

• The rate of convergence is quite slow near to the solution so if the convergence tolerance is set too small the solution may take much longer. 

• It is usually best to use a single timestep if possible, rather than many smaller steps as is normal for the Newton solver. More timesteps will greatly increase the solution time. 

• Unlike the Newton-based solvers, prescribed displacements are applied only to the nodes they affect at first and take many iterations to propagate through the adjoining mesh. This means that they can often cause excessive deformation of the adjacent elements, for example a compressive prescribed displacement can push the surface layer of nodes right through the adjoining elements causing a negative Jacobian error. Unlike the BFGS solver, where prescribed displacements often give more stable convergence, it is better to apply forces where possible and to avoid prescribed displacements. 

• If prescribed displacements are essential, it may be necessary to use smaller timesteps to avoid excessive distortion of the adjoining elements. In this case it is possible to slacken the convergence criteria for the intermediate steps and then apply a tighter tolerance for the final step to generate a correct solution. 

• The preconditioner improves convergence when the stiffness of the nodes varies, for example because of different element sizes, different materials or features such as quadratic elements with midside nodes. For problems where all the elements are the same it offers no great advantage and may even cause slower convergence in some cases. It is therefore best to use it for irregular meshes, multiple materials, quadratic elements and contact problems, but for problems with regular meshes where all the elements are a similar size it may be better to turn it off. 

• For problems with large deformation and displacements the solver may take a very large number of iterations to converge. The solver proceeds by many small, cautious steps, unlike the Newton-based solvers, which attempt to jump straight to the final answer on each iteration. It is therefore much more reliable but may need thousands or tens of thousands of iterations to reach the solution. 

The values for the `cgmethod` parameter can be:

* 0 : Hager-Zhang conjugate gradient (This is the default and should be preferred since its faster.)
* 1 : steepest descent

For the `preconditioner` parameter set,
* 0 : no preconditioner
* 1 : for diagonal stiffness preconditioner. The diagonal stiffness preconditioner greatly improves convergence when there are different size elements, mixed materials, or quadratic elements with midside nodes. 

_Example:_
```xml
<solver type="CG-solid">
  <cgmethod>0</cgmethod>
  <preconditioner>1</preconditioner>
  <lsiter>10</lsiter>
</solver>
```