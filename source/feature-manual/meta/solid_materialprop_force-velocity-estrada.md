This material model was formulated by Estrada et al. [^1] and is called `force-velocity-Estrada`. It is a modification of the `active_contraction` material based on the formulation of Guccione et al. [^2] described in [active-contraction](solid_materialprop_active_contraction.md), based on the fading-memory formulation poroposed by Hunter et al. [^3]. The active stress is evaluated as $T^{a}\mathbf{a}\otimes\mathbf{a}, where \mathbf{a}$ is the unit vector along the fiber in the current configuration, and

\[
T^{a}=e\left(t\right)\underbrace{T_{\max}\frac{Ca_{0}^{2}}{Ca_{0}^{2}+ECa_{50}^{2}}}_{\begin{array}{c}
\text{instantaneous length}\\
\text{dependence}
\end{array}}\underbrace{\frac{1+aQ\left(t,\lambda\left(t\right)\right)}{1-Q\left(t,\lambda\left(t\right)\right)}}_{\text{force-velocity}}
\]

where

\[
ECa_{50}=\frac{\left(\text{Ca}_{0}\right)_{\max}}{\sqrt{\exp\left[\beta\left(\lambda\left(t\right)l_{r}-l_{0}\right)\right]-1}}
\]

and

\[
Q\left(t,\lambda\left(t\right)\right)=\sum_{k=1}^{3}A_{k}\int_{-\infty}^{t}e^{-\alpha_{k}\left(t-\tau\right)}\dot{\lambda}\left(\tau\right)\,d\tau
\]

In these expressions, $\lambda\left(t\right)$ is the fiber stretch ratio at the current time. Here, $T^{a}$ "is the product of three distinct components: a time-varying normalized activation, $e\left(t\right)$, that defines the time course of force generation throughout the cardiac cycle; an instantaneous length-dependent term that scales the peak possible isometric tension based on the current fiber stretch; and a force-velocity term that dampens the instantaneous force generation based on the rate of shortening of the fibers" [^1]. The activation curve $e\left(t\right)$ is represented by the `ascl` property that takes an optional attribute, `lc`, which defines the time-dependent load controller.

_Example:_

This example defines a transversely isotropic material with a Mooney-Rivlin basis. It defines a homogeneous fiber direction and uses the active fiber contraction feature.

```xml
<material id="3" type="trans iso Mooney-Rivlin">
  <c1>13.85</c1>
  <c2>0.0</c2>
  <c3>2.07</c3>
  <c4>61.44</c4>
  <c5>640.7</c5>
  <k>100.0</k>
  <lam_max>1.03</lam_max>
  <fiber type="vector">1,0,0</fiber>
  <active_contraction type="force-velocity-Estrada">
    <ascl lc="1">1</ascl>
    <ca0>4.35</ca0>
    <beta>4.75</beta>
    <l0>1.58</l0>
    <refl>1.58</refl>
	<Tmax>135.7</Tmax>
	<alpha1>30.30303</alpha1>
	<A1>50</A1>
	<a_t>0.5</a_t>
	<force_velocity>1</force_velocity>
  </active_contraction>
</material>
```

[^1]: Estrada, Ana Cristina, Yoshida, Kyoko, Clarke, Samantha A, and Holmes, Jeffrey W, "Longitudinal Reinforcement of Acute Myocardial Infarcts Improves Function by Transmurally Redistributing Stretch and Stress", J Biomech Eng 142, 2 (2020).

[^2]: Guccione, J.M. and McCulloch, A.D., "Mechanics of active contraction in cardiac muscle: part I - constitutive relations for fiber stress that describe deactivation", J. Biomechanical Engineering vol. 115, no. 1 (1993), pp. 72-83.

[^3]: Hunter, P J, McCulloch, A D, and ter Keurs, H E, "Modelling the mechanical properties of cardiac muscle", Prog Biophys Mol Biol 69, 2-3 (1998), pp. 289-331.