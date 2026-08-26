The `biphasic` solver is the default solver used by FEBio for solving quasi-static or transient biphasic problems.

The default formulation uses equal-order interpolation for both the displacement and the fluid pressure field. However, when setting the `mixed_formulation` flag to 1, a mixed formulation is used where the pressure field is constant.

### Nonlinear solver

The `biphasic` solver solves the nonlinear finite element equations using a quasi-Newton method. This is an iterative method that requires the formation of the _stiffness matrix_ and then uses this matrix to solve a linear system of equations. Several parameters control when the stiffness matrix is formed. 

* `max_refs` : the maximum number of reformations of the stiffness matrix. Once this number is reached, FEBio will stop end the current timestep and either error terminate or try again using a smaller time step size. 

* `reform_each_time_step` : When enabled, the stiffness matrix will always be reformed at the start of each time step. 

* `reform_augment` : This flag determines whether the stiffness matrix is reformed at the start of each augmentation. 

* `diverge_reform` : When enabled, the stiffness matrix will be reformed when the energy norm increases. 

* `check_zero_diagonal` : When set to 1, the diagonal is checked for diagonal values that are close to zero. An error is produced when a zero diagonal is found.

* `zero_diagonal_tol` : The tolerance for the zero-diagonal check. 

* `qn_method` : This property sets the quasi-newton strategy. For symmetric problems it is recommended to use [BFGS](core_newtonstrategy_bfgs.md). For non-symmetric problems, it is advised to used [Broyden](core_newtonstrategy_broyden.md) instead. 

* `linear_solver` : This is an optional property that allows the user to explicitly specify the linear solver to be used for this model. If not specified, the default linear solver (usually the [pardiso](core_linearsolver_pardiso.md)). 

Several criteria are used to determine convergence of the solution for each timestep. 

* `dtol` : convergence tolerance on the displacement norm. 

* `rtol` : convergence tolerance on the residual norm.

* `etol` : convergence tolerance on the energy norm.

* `ptol` : convergence tolerance on the fluid pressure norm.

* `min_residual` : the minimum value of the residual norm. If the residual norm drops below this value, the solution is considered converged, regardless of the other norms. 

* `optimize_bw` : Permutes the internal node numbering to produce a stiffness matrix with minimal bandwidth. Minimizing the bandwidth may reduces the memory requirements for and the time to  factorize the stiffness matrix. However, most modern linear solvers do this automatically and therefore by default this flag is off. (It is only recommended to use with the [skyline](core_linearsolver_skyline.md)) linear solver.

* `equation_order` : Specifies the order in which the degrees of freedom are iterated over for each node. Set the `0` for forward (default) order, and `1` for reverse order. 

* `equation_scheme` : This parameter determines how the degrees of freedom (dofs) are grouped in the stiffness matrix. When set to `0` (staggered), all the dofs for a node are grouped together. When set to `1` (block) the dofs are grouped in blocks, one block for each dof. 

For example, if each node has two dofs, $a$ and $b$, then the grouping for the different schemes looks like:

\[
\begin{align}
    \text{staggered} &: [a_0, b_0, ..., a_n, b_n ] \\
    \text{block} &: [a_0, ..., a_n, b_0, ..., b_n ] \\
\end{align}
\]

### Line search
After the linear system is solved, a line search method will try to find a better solution, i.e. a solution that minimizes the energy, in the search direction. This can often significantly improve the convergence of the solution. The line search uses an iterative method to find this improved solution. The following parameters control the line search. 

* `lstol` : sets the tolerance for the line search method. Set to zero to skip the line search. 

* `lsmin` : the minimum allowed value for the line search factor. 

* `lsiter` : the maximum number of iterations allowed. 

* `ls_check_jacobians` : During the line search, it can happen that negative jacobians (i.e. inverted elements) are encountered. The standard error behavior is to stop the time step and either error terminate or retry with a smaller timestep size. However, when this flag is enabled, the negative jacobian errors will be handled by the line search. Often a small enough line search factor can be found that allows the solution to continue. 
