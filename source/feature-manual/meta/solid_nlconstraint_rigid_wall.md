A rigid wall interface is similar to a sliding interface, except that the secondary surface is a rigid wall.

The `plane` property defines the reference plane for the rigid wall. Its value is an array of four values:$a,b,c,d_{0}$. The actual plane is defined by specifying the offset to the reference plane. The offset parameter takes a loadcurve as an optional attribute to define the motion of the plane as a function of time. The loadcurve defines the offset h from the initial position in the direction of the plane normal: 

\[
\begin{array}{cc}
a\,x+b\,y+c\,z+d\left(t\right)=0, & d\left(t\right)=d_{0}+h\left(t\right)\end{array}
\]

So, for example, a rigid wall that initially lies in the xy-coordinate plane and moves in the z-direction would be specified as follows:

```
<plane>0,0,1,0</plane>
<offset lc="1">1.0</offset>
```
