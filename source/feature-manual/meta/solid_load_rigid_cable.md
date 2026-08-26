The `rigid_cable` load emulates the effect of a force applied on one end of a cable that is connected to one or more rigid bodies.

The `relative` flag indicates whether the location of the cable's via-points are defined in global coordinates (relative=0) or in the local coordinates of the corresponding rigid body (relative=1). 

One or more rigid cable points must be defined that define the points that the cable runs through. The first point defined is the anchor, where the cable is attached to. The other points define the "via points", i.e. a point where the cable runs through. Each cable point is defined by the rigid body that it connects to and a point on the rigid body that the cable runs through. The point's coordinates are either in the global or the local coordinate system of the rigid body, as determined by the `relative` flag. 

The following example illustrates a rigid cable setup. 

```
<rigid_load type="rigid_cable">
  <force lc="1">100</force>
  <force_direction>1,0,0</force_direction>
  <relative>1</relative>
  <rigid_cable_point>
    <rigid_body_id>rigid1</rigid_body_id>
    <position>0, -1, 1</position>
  </rigid_cable_point>
  <rigid_cable_point>
    <rigid_body_id>rigid2</rigid_body_id>
    <position>0, 1, 1</position>
  </rigid_cable_point>
</rigid_load>
```