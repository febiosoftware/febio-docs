The material type for the Huiskes reaction rate is `Huiskes reaction rate`. This material model employs the bone remodeling framework proposed by Weinans et al. [^1] and extended by Mullender et al. [^2].

The Huiskes specific reaction rate has the form

\[
k=\frac{1}{\left(J-\varphi_{r}^{s}\right)M^{s}}\left(B\left(\frac{\Psi_{r}}{\rho_{r}^{s}}-\psi_{0}\right)+\sum_{i=1}^{N}e^{-d_{i}/D}B_{i}\left(\frac{\Psi_{ri}}{\rho_{ri}^{s}}-\psi_{0}\right)\right)\,,
\]

where $\Psi_{r}$ is the strain energy density of the solid (strain energy in current configuration per mixture volume in the reference configuration) and $\rho_{r}^{s}=\sum\nolimits_{\sigma}\rho_{r}^{\sigma}$ is the referential apparent solid density (mass of solid in current configuration per mixture volume in reference configuration). The ratio $\Psi_{r}/\rho_{r}^{s}$ is the specific strain energy (strain energy per mass of solid in the current configuration). The Huiskes specific reaction rate may assume positive and negative values; it reduces to zero at homeostasis, when $\Psi_{r}/\rho_{r}^{s}=\psi_{0}$.

Per Mullender et al. [^2], the remodeling rate $k$ at the current material point may depend not only on the specific strain energy at the current point, but also on its value in the neighborhood of the current point (e.g., due to the presence of neighboring sensing cells that provide some form of feedback at the current location). Here, $N$ represents the number of elements in the neighborhood of the current material point element, which fall within a characteristic sensing distance $D$, and $d_{i}$ represents the distance between these neighboring points and the current material point.

When $D=0$ it follows that $N=0$ and the model uses the original formulation of Weinans et al. [^1]. When $D>0$, as per Mullender et al. [^2], the finite element code first searches for all the neighboring elements N which fall within a distance of $d_{i}\le4\times D$ of the element at which $k$ needs to be evaluated (here, using $d_{i}\le4\times D$ implies that the exponential term becomes negligible beyond this distance, since $e^{-4}=0.0183156$). This search is conducted once, at the start of the analysis, implying that it is not updated at subsequent time points when the deformation may alter distances. With increasing values of $D$, the number $N$ of neighboring elements may increase considerably, especially in three-dimensional models, which will considerably slow down the computation of $k$, therefore users must be careful with choosing an appropriate value for $D$.

Since the referential solid volume fraction $\varphi_{r}^{s}$ of a multiphasic mixture evolves with its composition, users must be careful not to allow $J-\varphi_{r}^{s}\to0$ as Huikes remodeling takes place, or else the computation of $k$ from the above formula becomes nearly singular. Typically this can be done by specifying the true density of the solid, $\rho_{T}^{s}$, to be much greater than the maximum apparent density $\rho_{r}^{s}$ allowed in the solid remodeling reaction. Then, the contribution of the evolving $\rho_{r}^{s} to \varphi_{r}^{s}$ will remain negligible.

_Example:_

To reproduce the interstitial solid remodeling theory proposed by Weinans et al. [^1], consider the forward reaction 

\[
\mbox{cells}+\mbox{solutes}\to\mbox{cells}+\mbox{solid}\,,
\]

where cells convert solutes (e.g., nutrients) into synthesized solid when the specific strain energy exceeds the homeostatic value. If the cells and solutes are implicit in this reaction (e.g., if it is assumed that their concentrations change negligibly), the production rate of the solid may be given by $\hat{\zeta}=k$ using the law of mass action for a forward reaction, where $k$ has the form given above.

```xml
<reaction name="solid remodeling" type="mass-action-forward">
  <vP sbm="1">1</vP>
  <forward_rate type="Huiskes reaction rate">
    <B>1.0</B>
    <psi0>0.01</psi0>
    <D>0</D>
  </forward_rate>
</reaction>
```

[^1]: Weinans, H, Huiskes, R, and Grootenboer, H J, "The behavior of adaptive bone-remodeling simulation models", J Biomech 25, 12 (1992), pp. 1425-41.

[^2]: Mullender, M G, Huiskes, R, and Weinans, H, "A physiological approach to the simulation of bone remodeling as a self-organizational control process", J Biomech 27, 11 (1994), pp. 1389-94.
