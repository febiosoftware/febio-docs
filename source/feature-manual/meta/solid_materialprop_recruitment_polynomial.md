The material type for a polynomial weak bond recruitment function is `recruitment polynomial`.

For this material the recruitment function is given by

\[
F\left(\Xi\right)=\mu_{0}+\mu_{1}\Xi+\mu_{2}\Xi^{2}
\]

where $\Xi$ is the measure of strain that triggers a new reactive weak bond generation. This function is unbounded with increasing $\Xi$. Users should typically employ $\mu_{0}=1$.

_Example:_
```xml
<recruitment type="recruitment poly">
  <mu0>1</mu0>
  <mu1>0</mu1>
  <mu3>50</mu3>
</recruitment>
```

