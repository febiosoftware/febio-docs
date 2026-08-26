The material type for a gamma recruitment function is `recruitment gamma`.

For this material the bond recruitment functions is given by

\[
F\left(\Xi\right)=1+r\frac{\gamma\left(\alpha,\Xi/\mu\right)}{\Gamma\left(\alpha,0\right)}\,,
\]

where $\gamma\left(\alpha,z\right)$ and $\Gamma\left(\alpha,z\right)$ are the lower and upper incomplete gamma functions, respectively. The normalization by $\Gamma\left(\alpha,0\right)$ ensures that this function is bounded by $1\le F\left(\Xi\right)\le1+r$.

_Example:_
```xml
<recruitment type="recruitment gamma">
  <alpha>3</alpha>
  <mu>0.4</mu>
  <max>4</max>
</recruitment>
```

