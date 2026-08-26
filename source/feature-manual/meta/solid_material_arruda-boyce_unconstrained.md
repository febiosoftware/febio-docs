The material type for an unconstrained Arruda-Boyce material is `Arruda-Boyce unconstrained`. This isotropic Arruda-Boyce [^1] 8-chain model has been used in the field of polymer modeling and in cervical biomechanics[^2]. It is based on the simple freely-jointed-chain model and can be derived using the Langevin equation of statistical mechanics. The strain energy density for this material takes the form

\[
\Psi(I_{1},J)=\xi\left(\sqrt{\frac{I_{1}}{3N}}\beta+\ln\frac{\beta}{\sinh\beta}\right)-\frac{\xi}{3}\sqrt{N}\beta_{0}\ln J+\frac{1}{2}\kappa(\ln J^{2}-1-2\ln J)
\]

where $I_{1}=tr\mathbf{C}$ is the first invariant of $\mathbf{C}$, ${\displaystyle \beta=\mathcal{L}^{-1}\left[\sqrt{\frac{I_{1}}{3N}}\right]}$ is the inverse Langevin equation, and ${\displaystyle \beta_{0}=\mathcal{L}^{-1}\left[\sqrt{\frac{1}{N}}\right]}$. Here, $\xi=nk\Theta$  is the initial fiber modulus with $n$ $k$, $\Theta$ respectively representing the number of chains per unit volume, Boltzmann's constant, and the absolute temperature. The parameter $N=\zeta^{2}$ is the number of chain segments, and $\zeta$ is the locking stretch that represents the extensibility of the material.

A Taylor series expansion is used to evaluate the inverse Langevin equation. The parameter $n_{\mathrm{term}}$ is used to control the number of terms used to evaluate the series; $n_{\mathrm{term}}$ must be an integer between 3 and 30.

Langevin mechanics describes a stochastic process with non-Gaussian distribution. It will reduce to a Gaussian distribution when the system approaches equilibrium. Thus, when the material is far from its maximum extensibility, i.e., when $\zeta=\sqrt{N}$ is much larger than the stretch, this model will reduce to a neo-Hookean material.

_Example:_
```xml
<material id="1" name="Soft Tissue" type="Arruda-Boyce unconstrained">
	<N>5</N>
	<ksi>1</ksi>
	<n_term>30</n_term>
	<kappa>1</kappa>
</material>
```

[^1]: Arruda, E.M. and Boyce, M.C., "A Three-Dimensional Constitutive Model for the Large Stretch Behavior of Rubber Elastic Materials", J. Mech. Phys. Solids 41, 2 (1993), pp. 389-412.

[^2]: Shi, Lei, Hu, Lingfeng, Lee, Nicole, Fang, Shuyang, and Myers, Kristin, "Three-dimensional anisotropic hyperelastic constitutive model describing the mechanical response of human and mouse cervix", Acta Biomaterialia 150 (2022), pp. 277--294.