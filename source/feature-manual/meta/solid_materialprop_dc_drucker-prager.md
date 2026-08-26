The material type for the Drucker-Prager criterion is `DC Drucker-Prager`. It is based on the yield criterion for plasticity introduced in [^1]. For this criterion,

\[
\Xi\left(\mathbf{F}\right)=\sigma_{e}-b\sigma_{m}
\]

where $\sigma_{e}$ is the von Mises stress, $\sigma_{m}=\frac{1}{3}tr\boldsymbol{\sigma}_{0}$ is the hydrostatic stress, $b$ is a parameter that depends on the yield (or failure) stress $\sigma_{t}$ in tension, and $\sigma_{c}$ in compression $(\sigma_{c}\ge0)$,

\[
b=3\frac{\sigma_{t}-\sigma_{c}}{\sigma_{c}+\sigma_{t}}
\]

This parameter $b$ is negative when $\sigma_{c}>\sigma_{t}$. In the special case when $b=0$ the Drucker-Prager criterion reduces to the von Mises criterion. When used as a plastic yield criterion (see Section [sec:Reactive-Plasticity]), the yield stress $\sigma_{y}$ for this type of material is given by

\[
\sigma_{y}=2\frac{\sigma_{c}\sigma_{t}}{\sigma_{c}+\sigma_{t}}
\]

which reduces to $\sigma_{y}=\sigma_{t}$ for uniaxial tension, $\sigma_{y}=-\sigma_{c}$ in uniaxial compression, and more generally, $\sigma_{y}=\sigma_{c}=\sigma_{t}$ when $\sigma_{t}=\sigma_{c}$. The parameter $a$ and $b$ are related to the parameters A and B appearing on Wikipedia's description of the [Drucker-Prager yield criterion](https://en.wikipedia.org/wiki/Drucker–Prager_yield_criterion) via

\[
\begin{aligned}a & =\sqrt{3}A & b & =3\sqrt{3}B\end{aligned}
\]

Given these relationships, users may consult that web page for finding the relation between these parameters and cohesion c and angle of internal friction $\phi$ (as well as the [Mohr-Coulomb yield surface](https://en.wikipedia.org/wiki/Mohr–Coulomb_theory#Typical_values_of_cohesion_and_angle_of_internal_friction)).

[^1]: Drucker, Daniel Charles and Prager, William, "Soil mechanics and plastic analysis or limit design", Quarterly of applied mathematics 10, 2 (1952), pp. 157--165.