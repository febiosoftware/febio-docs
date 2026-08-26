The 'prestrain' constraint can be used as an update rule to eliminate the distortion induced by the incompatibility of the initial prestrain gradient with the reference geometry. Thus, we retain the original reference geometry at the cost of an altered effective prestrain field. The update rule is given by the following equation.

\[
\mathbf{G^{\mathit{k+1}}}=\mathbf{G^{\mathit{k}}}\cdot\mathbf{F_{\mathit{c}}}
\]

By specifying a loadcurve for the `update` flag, the update can be delayed. This can be useful if, for instance, the prestrain is applied incrementally and the update rule should not be applied until the full prestrain field is applied. In that case, specifying a loadcurve for the `update` flag that is zero while the prestrain is applied, will delay the update process.

_Example:_
```xml
<constraint type="prestrain">
  <tolerance>0.01</tolerance>
</constraint> 
```