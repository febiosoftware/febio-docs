The material type for a power weak bond recruitment function is `recruitment power`. 

For this material the recruitment function is given by

\[
F\left(\Xi\right)=\mu_{0}+\mu_{1}\left(\frac{\Xi}{s}\right)^{\alpha},
\]

where $\Xi$ is the measure of strain that triggers a new reactive weak bond generation. This function is unbounded with increasing $\Xi$. Users should typically employ $\mu_{0}=1$.

_Example:_
```xml
<recruitment type="recruitment power">
  <mu0>1</mu0>
  <mu1>10</mu1>
  <alpha>2</alpha>
  <scale>0.06</scale>
</recruitment>
```
