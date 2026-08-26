The nonlinear spring allows users to define a custom relation between a measure of stretch and the spring force.

The `measure` parameter can be set to one of the following values:

1. `elongation`: Use the spring elongation, the difference between current and original length, as the measure of stretch.
2. `strain`: Use the strain, i.e. the ratio of elongation over original length, as the measure of stretch
3. `stretch`: Use the ratio of current length over original length as measure of stretch. 

_Example:_
```xml
<discrete_material id="1" name="set1" type="nonlinear spring">
	<scale>1</scale>
	<measure>elongation</measure>
	<force type="math">
		<math>x</math>
	</force>
</discrete_material>
```
