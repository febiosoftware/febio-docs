The material type for a Weibull recruitment function is `recruitment Weibull`.

For this material the recruitment functions is given by

\[
F\left(\Xi\right)=1+r\left(1-\exp\left[-\left(\Xi/\mu\right)^{\alpha}\right]\right)\,.
\]

Its minimum value is $1$ and its maximum value is $1+r$ as $\Xi/\mu\to\infty$.

_Example:_
```xml
<recruitment type="recruitment Weibull">
  <mu>0.3</mu>
  <alpha>2.0</alpha>
  <max>4</max>
</recruitment>
```
