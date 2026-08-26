The material type for the Law of Mass Action for a reversible reaction is `mass-action-reversible`.

For this type of reaction the constitutive relation for the molar production rate is given by

\[
\hat{\zeta}=\hat{\zeta}_{F}-\hat{\zeta}_{R}\,,
\]

where

\[
\begin{aligned}\hat{\zeta}_{F} & =k_{F}\prod\limits_{\alpha}\left(c^{\alpha}\right)^{\nu_{R}^{\alpha}}\\
\hat{\zeta}_{R} & =k_{R}\prod\limits_{\alpha}\left(c^{\alpha}\right)^{\nu_{P}^{\alpha}}
\end{aligned}
\,.
\]

The `forward_rate` and `reverse_rate` set the specific forward and reverse reaction rates. The units of $\hat{\zeta}_{F}$ and $\hat{\zeta}_{R}$ are $[n/L^{\mathrm{3}}\cdot t]$ and those of $c^{\alpha}$ are $[n/L^{\mathrm{3}}]$.

Example:

Consider the reversible dissociation of $CaCl$ salt into $Ca^{\mathrm{2+}}$ and $Cl^{\mathrm{-}}$ in water, $\mbox{CaCl}_{2}\rightleftharpoons\mbox{Ca}^{2+}+2\mbox{Cl}^{-}$. All three species are modeled explicitly in the mixture as solutes, with id's 1 (for $CaCl_{\mathrm{2}}$), 2 (for $Ca^{\mathrm{2+}}$) and 3 (for $Cl^{\mathrm{-}}$). The chemical reaction material is given by:

```
<reaction name="CaCl2 dissociation" type="mass-action-reversible">
  <vR sol="1">1</vR>
  <vP sol="2">1</vP>
  <vP sol="3">2</vP>
  <forward_rate type="constant">
    <k>1.0</k>
  </forward_rate>
  <reverse_rate type="constant">
    <k>0.1</k>
  </reverse_rate>
</reaction>
```
