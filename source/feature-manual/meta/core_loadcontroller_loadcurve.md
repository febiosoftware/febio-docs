A loadcurve controller is defined by the `loadcurve` type. The loadcurve is defined by repeating the point element for all data points:

```
<load_controller id="1" type="loadcurve">
  <interpolate>LINEAR</interpolate>
  <extend>CONSTANT</extend>
  <points>
    <point> 0, 0 </point>
    ...
    <point> 1, 1 </point>
  </points>
</loadcurve>
```

The `id` attribute is the load controller number and is used in other sections of the input file as a means to reference this controller.

The optional parameters `interpolate` and `extend` define how the value of the loadcurve is interpolated from the data points. The `interpolate` parameter defines the interpolation function and `extend` defines how the values of the loadcurve are determined outside of the interval defined by the first and last data point. The following tables list the possible values. The default values are marked with an asterisk (*).

|Interpolate|Description|
|-----------|-----------|
|`step`     | Use a step interpolation function |
|`linear`   | Use a linear interpolation function |
|`smooth`   | The values are interpolated using a cubic polynomial|

![Load curve types](figs/FigLoadCurveTypes.png)
///figure-caption
The different types of load curves.
///

|Extend         |Description|
|---------------|-----------|
|`constant`     | The value of the curve is the value of the closest endpoint |
|`extrapolate`  | The value is extrapolated linearly from the endpoints |
|`repeat`       | The curve is repeated |
|`repeat offset`| The curve is repeated but offset from the endpoints |

![Load curve extend](figs/FigLoadCurveExtend.png)
/// figure-caption
The different extend options
///
