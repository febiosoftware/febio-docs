The material type for the Michaelis-Menten reaction is `Michaelis-Menten`.

The Michaelis-Menten reaction may be used to model enzyme kinetics where the enzyme $\mathcal{E}^{e} $triggers the conversion of the substrate $\mathcal{E}^{s}$ into the product $\mathcal{E}^{p}$. The product molar supply is given by

\[
\hat{c}^{p}=\begin{cases}
\frac{V_{\max}c^{s}}{K_{m}+c^{s}} & c^{s}\geqslant c_{0}\\
0 & c^{s}<c_{0}
\end{cases}\,,
\]

where $c^{s}$ is the substrate concentration. The default value of $c_{0}$ is $0$. This relation may be derived, with some simplifying assumptions, by applying the law of mass action to the combination of two reactions,

\[
\mathcal{E}^{e}+\mathcal{E}^{s}\rightleftharpoons\mathcal{E}^{es}\to\mathcal{E}^{e}+\mathcal{E}^{p}
\]

Since the enzyme is not modeled explicitly in the Michaelis-Menten approximation to these two reactions, this reaction model is effectively equivalent to

\[
\mathcal{E}^{s}\to\mathcal{E}^{p}.
\]

Therefore, this reaction accepts only one reactant parameter `vR` and one product parameter `vP`. For consistency with the formulation of this reaction, the stoichiometric coefficients should be set to $\nu_{R}^{s}=\nu_{P}^{p}=1$, so that $\hat{c}^{p}=\hat{\zeta}$.

_Example:_
```xml
<reaction name="enzyme kinetics" type="Michaelis-Menten">
  <Vbar>0</Vbar>
  <vR sol="1">1</vR>
  <vP sol="2">1</vP>
  <forward_rate type="constant">
    <k>1.0</k>
  </forward_rate>
  <Km>5.0</Km>
</reaction>
```
