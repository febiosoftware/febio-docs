A `node distance` constraint can be used to enforce a user-defined distance between two nodes. The default configuration of this constraint is such that the initial distance between the two nodes is preserved. The target distance can be defined as a distance relative to the initial separation between the two nodes, or as an absolute distance.

_Example:_
This example illustrates how the node distance constraint can be used to reduce the distance between two nodes to zero: the target is set to zero and the relative flag is off so that the target is interpreted as an absolute distance. 

```xml
<constraint name="NodeDistance3" type="node distance">
  <laugon>0</laugon>
  <augtol>0.01</augtol>
  <penalty lc="1">1</penalty>
  <node>17,158</node>
  <minaug>0</minaug>
  <maxaug>10</maxaug>
  <target>0</target>
  <relative>0</relative>
</constraint>
```