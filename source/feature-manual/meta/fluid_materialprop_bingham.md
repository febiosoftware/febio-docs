The material type for a Bingham fluid [^1] is `Bingham`.

The viscous shear stress for this material model is

\[
\boldsymbol{\tau}=2\mu\mathbf{D}
\]

where

\[
\mu=\mu_{\infty}+\frac{\tau_{y}}{\dot{\gamma}}\left(1-e^{-n\dot{\gamma}}\right)
\]

Here, $\dot{\gamma}=\sqrt{2\mathbf{D}:\mathbf{D}}$ is the engineering shear rate. In the limit as $\dot{\gamma}\to0$ the viscosity is given by $\mu=\mu_{\infty}+n\tau_{y}$. If we define the scalar shear stress $\tau=\sqrt{\boldsymbol{\tau}:\boldsymbol{\tau}/2}$, if follows that $\tau=\mu_{\infty}\dot{\gamma}+\tau_{y}\left(1-e^{-n\dot{\gamma}}\right)$. Effectively, this constitutive model represents a bilinear response for $\tau$ versus $\dot{\gamma}$, with a slope of $\mu_{\infty}+n\tau_{y}$ when $\tau<\tau_{y}$ and $\mu=\mu_{\infty}$ when $\tau>\tau_{y}$. The exponential function rounds the corner at the intersection of these two lines. For an ideal Bingham fluid one would need to let $n\to\infty$. In practice, values of $n$ between 5 and 50 work well, with the lower end of this range producing faster convergence of the finite element solution.

_Example:_
```xml
<viscous type="Bingham">
	<mu>1</mu>
	<tauy>40</tauy>
	<n>40</n>
</viscous>
```

[^1]: Papanastasiou, Tasos C, "Flows of materials with yield", Journal of Rheology 31, 5 (1987), pp. 385--404.
