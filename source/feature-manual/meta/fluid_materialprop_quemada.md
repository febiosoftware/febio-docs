The material type for a Quemada model [^1] is `Quemada`.

The viscous shear stress for this material model is

\[
\boldsymbol{\tau}=2\mu\mathbf{D}
\]

where

\[
\mu=\frac{\mu_{0}}{\left(1-k\frac{H}{2}\right)^{2}}
\]

and

\[
k=\frac{k_{0}+k_{\infty}\sqrt{\dot{\gamma}_{r}}}{1+\sqrt{\dot{\gamma}_{r}}}\,,\quad\dot{\gamma}_{r}=\frac{\dot{\gamma}}{\dot{\gamma}_{c}}
\]

Here, $\dot{\gamma}=\sqrt{2\mathbf{D}:\mathbf{D}}$ is the engineering shear rate.

_Example:_

```xml
<viscous type="Quemada">
	<mu0>0.03</mu0>
	<H>0.5</H>
	<k0>3.691</k0>
	<kinf>1.778</kinf>
    <gc>2.30</gc>
</viscous>
```

[^1]: Quemada, DJRA, "Rheology of concentrated disperse systems II. A model for non-newtonian shear viscosity in steady flows", Rheologica Acta 17, 6 (1978), pp. 632--642.