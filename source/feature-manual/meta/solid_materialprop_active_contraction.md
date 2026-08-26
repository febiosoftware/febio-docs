The default active contraction model is `active_contraction`. It is based on the formulation of Guccione et al. [^1] and reviewed in the [FEBio Theory Manual](https://febio.org/knowledgebase/). The active stress is evaluated as $T^{a}\mathbf{a}\otimes\mathbf{a}$, where $\mathbf{a}$ is the unit vector along the fiber in the current configuration, and

\[
T^{a}=T_{\max}\frac{Ca_{0}^{2}}{Ca_{0}^{2}+ECa_{50}^{2}}C\left(t\right)
\]

where

\[
ECa_{50}=\frac{\left(\text{Ca}_{0}\right)_{\max}}{\sqrt{\exp\left[\beta\left(\lambda\left(t\right)l_{r}-l_{0}\right)\right]-1}}
\]

In this expression, $\lambda\left(t\right)$ is the fiber stretch ratio at the current time. The activation curve $C\left(t\right)$ is represented by the `ascl` property that takes an optional attribute, `lc`, which defines the load controller. 

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
  <active_contraction type="active_contraction">
    <ascl lc="1">1</ascl>
    <ca0>4.35</ca0>
    <beta>4.75</beta>
    <l0>1.58</l0>
    <refl>2.04</refl>
  </active_contraction>
</material>
```

[^1]: Guccione, J.M. and McCulloch, A.D., "Mechanics of active contraction in cardiac muscle: part I - constitutive relations for fiber stress that describe deactivation", J. Biomechanical Engineering vol. 115, no. 1 (1993), pp. 72-83.