The material type for a Carreau-Yasuda model [#Cho91] is `Carreau-Yasuda`.

The viscous shear stress for this material model is

\[
\boldsymbol{\tau}=2\mu\mathbf{D}
\]

where

\[
\mu=\mu_{\infty}+\left(\mu_{0}-\mu_{\infty}\right)\left(1+\left(\lambda\dot{\gamma}\right)^{a}\right)^{\left(n-1\right)/a}
\]

Here, $\dot{\gamma}=\sqrt{2\mathbf{D}:\mathbf{D}}$ is the engineering shear rate.

_Example:_
```xml
<viscous type="Carreau-Yasuda">
	<mu0>0.056</mu0>
	<mui>0.0035</mui>
	<lambda>1.9</lambda>
	<n>0.22</n>
	<a>1.25</a>
</viscous>
```
