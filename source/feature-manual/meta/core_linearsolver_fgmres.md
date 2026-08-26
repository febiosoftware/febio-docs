This iterative linear solver, from the MKL library, implements the GMRES algorithm, which is an efficient Krylov-based iterative solution strategy. It requires several configuration parameters, listed above, and only works with unsymmetric matrices. In the table below, N refers to the number of equations.

Note that when using FGMRES as a preconditioner it is recommended to set the `fail_max_iters` flag to zero. 

_Example 1._ This example shows how to set up the FGMRES solver with an ILU0 preconditioner. 

```xml
<default_linear_solver type="fgmres">  <max_iter>100</max_iter>
  <tol>1e-5</tol>
  <pc_left type="ilu0"/>
</default_linear_solver>
```

_Example 2._ This example sets up an FGMRES solver with a Schur preconditioner. For the Schur system we use pardiso for solving the A-block outside of the Schur complement and approximate the A-block inside the Schur complement with its diagonal. This solver requires a block-structured matrix. In order to generate the block structure you need to set the `equation_scheme` control parameter to 1 in the model input file. 

```xml
<default_linear_solver type="fgmres">
    <print_level>2</print_level>
    <max_iter>100</max_iter>
    <tol>1e-5</tol>
    <abs_tol>1e-9</abs_tol>
    <pc_left type="schur">
        <print_level>0</print_level>
        <do_jacobi>0</do_jacobi>
        <A_solver type="pardiso"/>
        <schur_pc>0</schur_pc>
        <schur_A_solver type="diagonal"/>
        <schur_solver type="fgmres">
            <print_level>0</print_level>
            <max_iter>100</max_iter>
            <tol>0.05</tol>
            <fail_max_iters>0</fail_max_iters>
        </schur_solver>
    </pc_left>
</default_linear_solver>
```
