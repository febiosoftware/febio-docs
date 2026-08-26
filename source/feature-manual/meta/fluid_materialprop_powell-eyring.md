The material type for a Powell-Eyring model [^1] is `Powell-Eyring`.

The viscous shear stress for this material model is

\[
\boldsymbol{\tau}=2\mu\mathbf{D}
\]

where

\[
\mu=\mu_{\infty}+\left(\mu_{0}-\mu_{\infty}\right)\frac{\sinh^{-1}\lambda\dot{\gamma}}{\lambda\dot{\gamma}}
\]

Here, $\dot{\gamma}=\sqrt{2\mathbf{D}:\mathbf{D}}$ is the engineering shear rate.

_Example:_

```xml
<viscous type="Powell-Eyring">
	<mu0>0.056</mu0>
	<mui>0.0035</mui>
	<lambda>5.4</lambda>
</viscous>
```

[^1]: Cho, Y I and Kensey, K R, "Effects of the non-Newtonian viscosity of blood on flows in a diseased arterial vessel. Part 1: Steady flows", Biorheology 28, 3-4 (1991), pp. 241-62.