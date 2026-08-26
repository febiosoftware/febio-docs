The moving frame load can be used to model the effects of being embedded in an accelerating and rotating coordinate system. Whereas the centrifugal body force only emulates the effect of a centrifugal force and assumes a static analysis, the moving frame load includes Coriolis effect and the effects of an accelerating coordinate system and can be used in a dynamic analysis. 

The motion of the moving frame is decomposed into a translation and a rotation. The position of a material point $\mathbf{r}$ in the fixed inertial frame can then be related to the position in the rotating frame $\mathbf{r\mathit{'}}$ via, 

\[
\mathbf{r}=\mathbf{Y}+\mathbf{R}\mathbf{r\mathit{'}}
\]

Here, $\mathbf{Y}$ is the position of the origin of the moving frame and $\mathbf{R}$ is the rotation matrix. 

Substituting this into the equations of motion (i.e. the balance of linear momentum), results in a modified equation of motion where the effects of the moving frame can be combined into a single body load. 

\[
\mathbf{f}=\rho\left(\mathbf{R}^{T}\mathbf{A}+\mathbf{\dot{W}}\times\mathbf{r}'+\mathbf{W}\times\left(\mathbf{W}\times\mathbf{r}'\right)+2\mathbf{W}\times\mathbf{v}'\right)
\]

Here, $A$ is the linear acceleration of the moving frame, $W$ is the angular velocity of the moving frame, measured in the moving frame (i.e. $\mathbf{W}=\mathbf{R}^{T}\mathbf{w}$, where $\mathbf{w}$ is the angular velocity in the fixed frame), and $\mathbf{v}'$ is the velocity of the material point, measured in the moving frame. 

The moving frame is defined via the two vectors, the angular velocity of the rotating frame $\mathbf{w}$, and the linear acceleration of the rotating frame's origin $\mathbf{A}$. The components of both vectors may be defined via load curves to make them time-dependent. 

Note that if you wish to include the effect of gravity, do not add a separate body force load. Instead, modify the linear acceleration to include gravity: $\boldsymbol{a=}A-\boldsymbol{g}$.

_Example:_
```xml
<Loads>
  <body_load type="moving frame">
    <wx>0</wx>
    <wy>0</wy>
    <wz lc="1">1</wz>
    <ax>0</ax>
    <ay>0</ay>
    <az>0</az>
  </body_load>
</Loads> 
```