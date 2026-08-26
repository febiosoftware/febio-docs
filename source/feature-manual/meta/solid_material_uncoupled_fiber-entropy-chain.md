This material type is `uncoupled fiber-entropy-chain`. It was proposed by [^1]. This fiber model is based on statistical mechanics to reflect the entropy-driven nature of a biological fiber. The model is derived from the freely-jointed-chain mechanism. Its strain energy is directly related to the entropic change of the chains in the material, given by

\[
\Psi_{n}(\tilde{I}_{n})=\xi N\left(\sqrt{\frac{\tilde{I}_{n}}{N}}\beta+\text{ln}\frac{\beta}{\sinh\beta}\right)-\frac{\xi\sqrt{N}}{2}\beta_{0}\tilde{I}_{n}-\alpha_{00}
\]

where $\tilde{I}_{n}=\mathbf{n}_{r}\cdot\tilde{\mathbf{C}}\cdot\mathbf{n}_{r}$ is the deviatoric measure of the stretch ratio along the referential fiber direction $\mathbf{n}_{r}$. The inverse Langevin equation relates the parameter $\beta$  to $I_{n}$ and $N$ according to ${\displaystyle \beta=\mathcal{L}^{-1}\left(\sqrt{\frac{I_{n}}{N}}\right)}$. Here, $\beta_{0}$ is the value of $\beta$ when $I_{n}=1$, and $\alpha_{00}$ is needed to produce a state of zero energy at $I_{n}=1$. The parameter $\xi=nk\Theta$ is the initial fiber stiffness, with $n$, $k$, and $\Theta$ respectively representing the number of chains per unit volume, Boltzmann's constant, and the absolute temperature. The parameter $N=\zeta^{2}$ is the number of chain segments, and $\zeta$ is the locking stretch, representing the extensibility of the fiber. The Langevin function is given by $\mathcal{L}\left(x\right)=\coth x-\frac{1}{x}$.

When evaluating the inverse Langevin equation, a Taylor series expansion is applied for computational stability. The parameter $n_{\mathrm{term}}$ is used to control the number of terms used to evaluate the equation; it must be an integer between 3 and 30.

_Example:_
```xml
<material id="1" name="Soft Tissue" type="uncoupled solid mixture">
	<k>1e4</k>
	<solid type="Mooney-Rivlin">
	  <c1>10.0</c1>
	  <c2>0</c2>
	</solid>
	<solid type="uncoupled fiber-entropy-chain">
	  <N>2.3</N>
	  <ksi>1</ksi>
	  <n_term>25</n_term>
	  <fiber type="vector">0,0,1</fiber>
	</solid>
</material>
```

[^1]: Shi, Lei, Hu, Lingfeng, Lee, Nicole, Fang, Shuyang, and Myers, Kristin, "Three-dimensional anisotropic hyperelastic constitutive model describing the mechanical response of human and mouse cervix", Acta Biomaterialia 150 (2022), pp. 277--294.