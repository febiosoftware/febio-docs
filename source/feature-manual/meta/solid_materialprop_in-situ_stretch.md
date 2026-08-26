The `in-situ stretch` generator option calculates a prestrain gradient based on a fiber stretch and the fiber vector defined by the `elastic` material of the [prestrain elastic](solid_material_prestrain_elastic.md) material. This implies that this elastic material must define a `fiber` property. 

This option generates one of the following prestrain gradients, depending on the `isochoric` option. 

\[
\hat{\mathbf{F}}_{p,iso}=\mathbf{Q}\left[\begin{array}{ccc}
\lambda\\
 & \lambda^{-1/2}\\
 &  & \lambda^{-1/2}
\end{array}\right]\mathbf{Q^{\mathrm{\mathit{T}}}},\qquad\hat{\mathbf{F}}_{p,uni}=\mathbf{Q}\left[\begin{array}{ccc}
\lambda\\
 & 1\\
 &  & 1
\end{array}\right]\mathbf{Q^{\mathit{T}}}
\]

If the `isochoric` option is set to 1, then $\hat{\mathbf{F}}_{p,iso}$ is used. Otherwise, $\hat{\mathbf{F}}_{p,uni}$ is used. 

The rotation tensor is defined implicitly via the fiber vector $\boldsymbol{a}$ and the prestrain gradient tensor is effectively determined via, 

\[
\hat{\mathbf{F}}_{p,iso}=\lambda\mathbf{A}+\mu\left(\boldsymbol{1-}\mathbf{A}\right)
\]

where $\mathbf{A}=\boldsymbol{a}\otimes\boldsymbol{a}$, $\lambda$ the prescribed fiber stretch, and $\mu=\lambda^{-1/2}$ or $\mu=1$ depending on the `isochoric` option.

_Example:_

```xml
<material id="1" type="prestrain elastic">
   <elastic type="coupled trans-iso Mooney-Rivlin">
        <k>0.1</k>
        <density>1e-09</density>
        <c1>0.01</c1>
        <c2>0</c2>
        <c3>0.0139</c3>
        <c4>116.22</c4>
        <c5>535.09</c5>
        <lam_max>1.046</lam_max>
        <fiber type="vector">-0.0804,-0.508,-0.858</fiber>
  </elastic>
  <prestrain type="in-situ stretch">
    <stretch lc="1">1.05</stretch>
    <isochoric>1</isochoric>
  </prestrain>
</material> 
```

