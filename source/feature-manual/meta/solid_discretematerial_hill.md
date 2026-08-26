The force in the Hill discrete element is the sum of the passive element and the active element. 

\[
F=F_{p}+F_{a}
\]

The passive force is given by,

\[
F_{p}=\begin{cases}
F_{max}\left(\exp\left(K_{sh}\left(l-1\right)/L_{max}-1\right)/\exp\left(K_{sh}-1\right)\right) & ,l>1\\
0 & ,l\leqslant1
\end{cases}
\]

where $l$ is the relative stretch defined by, $l=l_m/l_0$ and $l_m$ is the discrete element length and $l_0$ is either the `L0` parameter, which sets the reference length of the muscle, or the initial discrete element length (if `L0` is set to zero). 

The Max Force parameter (`Fmax`) is the maximum force the muscle can produce. Physiologically, this happens under 1) tetanized neural activation 2) at the optimum muscle length and 3) isometric contraction (contraction without movement). From a modelling perspective, this is the tensile force developed in the discrete element at the optimum length (Max Length) and 100% activation.

The Max Length parameter (`Lmax`) is the optimum muscle length. This corresponds to the peak of the force-length curve.

The shape parameter ($K_{sh}$ = `Ksh`) is a dimensionless parameter that controls the rate of the rise of the exponential function that defines the passive force-length relationship for the parallel elastic component of the Hill model.


The active force is given by, 

\[
F_a=ac\,F_{max}\,F_{tl}\left(l\right)\,F_{tv}\left(v\right)
\]

Here, $v$, a measure of the relative discrete element's growth speed, is defined by,

\[
v=v_m/\left(V_{max}\,S_v\left(ac\right)\right)
\]

where $v_m$ is the actual discrete element's growth speed and the Maximum Shortening Velocity parameter (`Vmax`) defines the maximum shortening velocity for the muscle.

The Activation Level parameter (`ac`) defines the normalized activation level of the muscle, which can vary between 0 (no activation, passive properties) to 1 (maximum activation). This parameter can be set as a constant or varied as a function of time via a load curve.

The shortening velocity-force curve (`Sv`) defines a scale factor that optionally scales the Maximum Shortening Velocity property (`Vmax`) as a function of the current activation level. This curve can be defined using the Curve Editor. The x-axis should be the activation level (varying between 0 and 1, no units), and the y-axis should be the scale factor (no units). If this curve is not defined, the value entered for `Vmax` is assumed constant as a function of activation level.

The normalized tension-length curve (`Ftl`) (Figure 1) defines the relationship between normalized length (x-axis) and normalized tension (y-axis).  This curve can be defined using the Curve Editor. A normalized length of 1 means that the current length is the same as the initial length (`L0`). A normalized force of 1 means that the force is equal to the Max Force property (`Fmax`).

![image.png](figs/FigHillForceLength.png)
/// figure-caption
Example data for the normalized tension-length curve (`Ftl`).
/// 

The normalized force-velocity curve (`Fvl`) (Figure 2) defines the relationship between normalized velocity (x-axis) and normalized velocity (y-axis). This curve can be defined using the Curve Editor. A normalized velocity of 0 means that the muscle is neither shortening nor lengthening, while a normalized velocity of -1 and +1 indicate maximal velocities of shortening and lengthening, respectively. A normalized force of 1 means that the force at the current velocity of shortening/lengthening is equal to the Max Force property (`Fmax`).

![image.png](figs/FigHillForceVelocity.png)
/// figure-caption
Example data for the normalized force-velocity curve (`Fvl`).
/// 

The properties `Sv`, `Ftl`, and `Ftv`, are optional and will evaluate to 1 if omitted. They can be defined as load curves. See the example below. 

_Example:_
```xml
<discrete_material id="1" name="test" type="Hill">
  <Vmax>1</Vmax>
  <ac>0.1</ac>
  <Fmax>50</Fmax>
  <Ksh>5</Ksh>
  <Lmax>1.5</Lmax>
  <L0>10</L0>
  <Ftl type="point">
    <interpolate>smooth</interpolate> 				
    <points>
      <pt>0.0, 0</pt>
      <pt>0.1, 0.000258139</pt>
      <pt>0.2, 0.00161616</pt>
      <pt>0.3, 0.00740118</pt>
      <pt>0.4, 0.0272783</pt>
      <pt>0.5, 0.0820396</pt>
      <pt>0.6, 0.201851</pt>
      <pt>0.7, 0.406524</pt>
      <pt>0.8, 0.670275</pt>
      <pt>0.9, 0.904792</pt>
      <pt>1.0, 0.999955</pt>
      <pt>1.1, 0.904792</pt>
      <pt>1.2, 0.670275</pt>
      <pt>1.3, 0.406524</pt>
      <pt>1.4, 0.201851</pt>
      <pt>1.5, 0.0820396</pt>
      <pt>1.6, 0.0272783</pt>
      <pt>1.7, 0.00740118</pt>
      <pt>1.8, 0.00161616</pt>
      <pt>1.9, 0.000258139</pt>
      <pt>2.0, 0</pt>
	</points>
  </Ftl> 
</discrete_material> 
```