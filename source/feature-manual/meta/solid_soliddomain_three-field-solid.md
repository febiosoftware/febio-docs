The `three-field-solid` solid domain type implements a three-field formulation [^1] for solving the finite element equations. This formulation is recommended for modeling (nearly-) incompressible materials using linear hexahedral and pentahedral elements. These elements tend to "lock" when modeling incompressible materials and the three-field formulation overcomes this issue. This formulation requires an uncoupled-elastic material to work. 

In addition to the displacement, this formulation also solves for the pressure $p$ and volume ratio $J$. The pressure can be seen as a Lagrange multiplier and the volume constraint (i.e. $J=1$) is enforced using an augmented Lagrangian method. The bulk modulus $k$ (defined on the material) is seen as a penalty factor for the constraint enforcement. Without augmentations, this amounts to a penalty method for enforcing the constraint. To enable augmentations, set `laugon` to 1 and specify a convergence tolerance using `atol`.  The augmentation tolerance determines the convergence condition that is used for the augmented Lagrangian method: convergence is reached when the relative ratio of the Lagrange multiplier norm of the previous augmentation $\left\Vert \lambda_{k}\right\Vert$ to the current one $\left\Vert \lambda_{k+1}\right\Vert$ is less than the specified value:

\[
\left|\frac{\left\Vert \lambda_{k+1}\right\Vert -\left\Vert \lambda_{k}\right\Vert }{\left\Vert \lambda_{k+1}\right\Vert }\right|<\varepsilon 
\]

Thus, a value of 0.01 implies that the change in norm between the previous augmentation loop and the current loop is less than 1%.

In addition, you can control the minimum and maximum number of augmentations using `minaug` and `maxaug`. 

_Example:_

```xml
<SolidDomain name="Part1" mat="Material1" type="three-field-solid">
    <laugon>1</laugon>
    <atol>0.01</atol>
    <minaug>0</minaug>
    <maxaug>0</maxaug>
</SolidDomain>
```

[^1]: Simo, J.C. and Taylor, R.L., "Quasi-incompressible finite elasticity in principal stretches: Continuum basis and numerical algorithms", Computer Methods in Applied Mechanics and Engineering 85 (1991), pp. 273-310.