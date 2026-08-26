The `math` load controller allows users to use a mathematical expression to define a function of time. Use the `t` parameter to reference time.

```
<load_controller id="1" type="math">
    <math>2.0*sin(pi*t)</math>
</load_controller>
```