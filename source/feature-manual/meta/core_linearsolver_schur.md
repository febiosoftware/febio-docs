The Schur solver is a linear solver that takes a 2x2 block structured matrix and solves the linear system by decomposing it in its Schur-complement form. Thus, instead of solving the following system directly,

\[
\left[\begin{array}{cc}
A & B\\
C & D
\end{array}\right]\left[\begin{array}{c}
u\\
v
\end{array}\right]=\left[\begin{array}{c}
a\\
b
\end{array}\right]
\]


it first solves for v,

\[
Sv=b-CA^{-1}a
\]

where $S=D-CA^{-1}B$ is the Schur complement of $A$. Then the Schur solver solves for $u$,

\[
u=A^{-1}\left(a-Bv\right)
\]

In order to use this solver, users need to select how they wish to solve the A-block, and how to solve the Schur complement. For the A-block users can choose any of the linear solvers listed above, either direct or iterative. For the Schur complement users can only choose a Krylov-based iterative solver (FGMRES or CG) because FEBio does not form the Schur complement explicitly. 

This solver is often more effective as a preconditioner for FGMRES. In this case, the A-block and Schur complement only need to be solved approximately. See the examples below for some example configurations. This solver requires a block-structured matrix. In order to generate the block structure you need to set the `equation_scheme` control parameter to 1 in the model input file.

