The `tension-only linear spring` is a linear spring that only produces a force in tension. 

\[
    f\left(d\right) = \left\{ \begin{matrix}
        {E\,d,\quad d \ge 0} \\
        {0,\quad d < 0}
    \end{matrix} \right.
\]

_Example:_
```xml
<discrete_material id="1" type="tension-only linear spring">
    <E>3.0</E>
</discrete_material>
```