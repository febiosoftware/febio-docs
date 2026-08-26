This valuator uses a mathematical expression to evaluate the value as a function of position and time. 

The mathematical expression may use X, Y, and Z (note uppercase) as position variables and t (lowercase) as time variable.

In this example, the E parameter is set using the math valuator. 

```
<E type="math">
    <math>X^2+Y^2+Z^2</math>
</E>
```

Note that because the type (i.e. "math") and the parameter ("math") is the same string, an abbreviated syntax is allowed.


```
<E type="math">X^2+Y^2+Z^2</E>
```
