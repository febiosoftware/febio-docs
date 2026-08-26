The material type for a log-normal recruitment function is `recruitment log-normal`.

For this material the recruitment function is given by

\[
F\left(\Xi\right)=1+\frac{r}{2}\text{erfc}\left[-\frac{\ln\left(\Xi/\mu\right)}{\sigma\sqrt{2}}\right]\,.
\]

Its minimum value is 1 and its maximum value is $1+r$ as $\Xi/\mu\to\infty$.

_Example:_
```xml
<recruitment type="recruitment log-normal">
  <mu>0.3</mu>
  <sigma>0.25</sigma>
  <max>4</max>
</recruitment>
```
