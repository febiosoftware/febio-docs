The material type for a Newtonian fluid is `Newtonian fluid`.

The viscous shear stress for this material model is

\[
\boldsymbol{\tau}=\left(\kappa-\frac{2}{3}\mu\right)\left(tr\mathbf{D}\right)\mathbf{I}+2\mu\mathbf{D}
\]

Stokes' condition is a constitutive assumption that sets $tr\boldsymbol{\tau}=0$, implying that $\kappa=0$. This assumption is only valid for some fluids (e.g., monoatomic gas [^1]). Users may use or ignore this assumption by selecting an appropriate value for $\kappa$.

_Example:_
```xml
<viscous type="Newtonian fluid">
	<mu>0.001</mu>
	<kappa>0</kappa>
</viscous>
```

[^1]: Panton, Ronald L, Incompressible flow (John Wiley & Sons, 2006).