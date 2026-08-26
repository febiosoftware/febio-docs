The material type for the Deshpande-Fleck criterion is `DC Deshpande-Fleck`. It is based on the yield criterion for plasticity introduced in [^1]. For this criterion, we let

\[
\Xi\left(\mathbf{F}\right)=\sqrt{\frac{\sigma_{e}^{2}+\left(3\beta\sigma_{m}\right)^{2}}{1+\beta^{2}}}
\]

where $\sigma_{e}$ is the von Mises stress, $\sigma_{m}=\frac{1}{3}\tr\boldsymbol{\sigma}_{0}$ is the hydrostatic stress, $\beta$ is a material parameter that controls the contribution of the hydrostatic stress to this criterion ($\beta=0$ recovers the von Mises yield criterion). This criterion was introducted to model yielding of polymer foams, for which Deshpande and Fleck recommended using $\beta=1/3$. On [Wikipedi](https://en.wikipedia.org/wiki/Drucker–Prager_yield_criterion#Deshpande–Fleck_yield_criterion_or_isotropic_foam_yield_criterion), this criterion is described as a modification of the Drucker-Prager criterion, but note that Deshpande and Fleck describe this material model as "phenomenological", i.e., intended to fit experimental data well, though they do suggest that $3\beta$ represents the ratio of hydrostatic strength to shear strength.

_Example:_
```xml
<criterion type="DC Deshpande-Fleck">
  <beta>0.3333</beta>
</criterion>
```

[^1]: Deshpande, VS and Fleck, NA, "Multi-axial yield behaviour of polymer foams", Acta materialia 49, 10 (2001), pp. 1859--1866.

