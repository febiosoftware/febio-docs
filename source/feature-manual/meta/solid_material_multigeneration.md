The material type for a multigeneration solid is `multigeneration`. This material describes a mixture of elastic solids, each created in a specific generation. It is a container for any combination of the elastic materials described.

Repeat the `generation` property as many times as needed (see [generation](solid_materialprop_generation.md)).

_Example:_
```xml
<material id="1" name="Growing Solid" type="multigeneration">
  <generation id="1">
    <start_time>0.0</start_time>
    <solid type="Holmes-Mow">
      <density>1</density>
      <E>1</E>
      <v>0</v>
      <beta>0.1</beta>
    </solid>
  </generation>
  <generation id="2">
    <start_time>1.0</start_time>
    <solid type="Holmes-Mow">
      <density>1</density>
      <E>1</E>
      <v>0</v>
      <beta>0.1</beta>
    </solid>
  </generation>
</material>
```
The corresponding value of $t^{\gamma}$ for each of the generations is provided in the `Globals` section.

_Example:_
```xml
<Globals>
  <Generations>
    <gen id="1">0.0</gen>
    <gen id="2">1.0</gen>
  </Generations>
</Globals>
```
