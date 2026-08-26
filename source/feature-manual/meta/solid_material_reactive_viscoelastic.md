The material type for a compressive reactive viscoelastic solid is `reactive viscoelastic`.

The `kinetics` parameter should be set to 1 for Type I bond kinetics or 2 for Type II bond kinetics. 

The `trigger` parameter should be set 0 when weak bonds break and reform in response to any form of the strain; it should be set to 1 when the trigger is distortional strain; and it should be set to 2 when the trigger is dilatational strain, 

\[\text{trigger}=\begin{cases}
0\text{ for any strain} & \left\Vert \Delta\mathbf{E}\right\Vert \\
1\text{ for distortional strain} & \left\Vert \text{dev}\Delta\boldsymbol{\eta}\right\Vert \\
2\text{ for dilatational strain} & \left|\ln\left(\det\Delta\mathbf{F}\right)\right|
\end{cases}
\]


where $\Delta\mathbf{E}=\frac{1}{2}\left(\Delta\mathbf{F}^{T}\cdot\Delta\mathbf{F}-\mathbf{I}\right)$ is the incremental Lagrange strain, $\Delta\boldsymbol{\eta}=\ln\Delta\mathbf{V}$ is the incremental natural strain, $where \Delta\mathbf{V}$ is the left stretch tensor of $\Delta\mathbf{F}$, and $\Delta\mathbf{F}=\mathbf{F}\left(t_{n+1}\right)\cdot\mathbf{F}^{-1}\left(t^{m}\right)$, where $t_{n+1}$ is the current time and $t^{m}$ is the birth time of the most recent weak bond generation.

The `elastic` and `bond` materials may be selected from the list of unconstrained elastic materials. 

The `recruitment` material can be used to model nonlinear viscoelasticity where the weak bond response becomes more significant with increasing strain. 

The parameters `wmin` and `emin` can be adjusted to improve computational efficiency by reducing the number of generations u in an analysis. In practice, the value of `emin` should be no greater than one-hundredth of the equilibrium strain in a loading configuration. The parameter `wmin` must be in the range $0\le w_{\min}\le1.$ In practice, a good balance between accuracy and efficiency is achieved by using $w_{\min}\le0.05$.

_Example:_
```
<material id="1" name="RV solid" type="reactive viscoelastic">
  <kinetics>1</kinetics>
  <trigger>0</trigger>
  <wmin>0.05</wmin>
  <emin>0.001</emin>
  <elastic type="Holmes-Mow">
    <density>1</density>
    <E>1</E>
    <v>0.3</v>
    <beta>0.5</beta>
  </elastic>
  <bond type="Holmes-Mow">
    <density>1</density>
    <E>1</E>
    <v>0.3</v>
    <beta>0.5</beta>
  </bond>
  <relaxation type="relaxation-exponential">
    <tau>4</tau>
  </relaxation>
  <recruitment type="recruitment power">
    <mu0>1</mu0>
    <mu1>30</mu1>
    <alpha>2</alpha>
    <scale>1</scale>
</material>
```
