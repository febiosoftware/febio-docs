# in-situ stretch

**Module:** solid

**Category:** nlconstraint

**Type string:** `"in-situ stretch"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `update` | update | true | $\{0, 1\}$ |  |
| `tolerance` | tolerance | 0 | $\in \mathbb{R}$ |  |
| `min_iters` | min_iters | 0 | $\in \mathbb{Z}$ |  |
| `max_iters` | max_iters | -1 | $\in \mathbb{Z}$ |  |
| `max_stretch` | max_stretch | 0 | $\in \mathbb{R}$ |  |
| `isochoric` | isochoric | true | $\{0, 1\}$ |  |


## Description

The `in-situ stretch` constraint can be used as a prestrain update rule to enforce the fiber stretch induced by the initial prestrain gradient. As with the in-situ stretch generator option, this rule has an isochoric version and an uniaxial version for the update rule. 

\[
\mathbf{G}_{iso}=\mathbf{Q}\left[\begin{array}{ccc}
\lambda^{-1}\\
 & \lambda^{1/2}\\
 &  & \lambda^{1/2}
\end{array}\right]\mathbf{Q^{\mathrm{\mathit{T}}}},\qquad\mathbf{G}_{uni}=\mathbf{Q}\left[\begin{array}{ccc}
\lambda^{-1}\\
 & 1\\
 &  & 1
\end{array}\right]\mathbf{Q^{\mathit{T}}}
\]

where $\lambda^{2}=\mathbf{a}_{0}\cdot\mathbf{C}^{k}\cdot\mathbf{a}_{0}$, is the fiber stretch induced by the distortion. 

_Example:_
```xml
<constraint type="in-situ stretch">
  <tolerance>0.01</tolerance>
  <isochoric>1</isochoric>
</constraint>
```
