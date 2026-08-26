The material type for this relaxation function is `relaxation-exp-dist-user`.

The reduced relaxation function for this material type is given by

\[
g\left(\mathbf{F}\left(v\right);t-v\right)=e^{-\left(t-v\right)/\tau\left[K_{2}\left(v\right)\right]}
\]

where $\tau\left(K_{2}\left(v\right)\right)$ is given as a mathematical expression (type="math"), or as a loadcurve (type="point").

_Example 1:_
```xml
<material id="1" name="RVE" type="reactive viscoelastic">
  <kinetics>1</kinetics>
  <trigger>1</trigger>
  <elastic type="neo-Hookean">
    <density>1</density>
    <E>0.13</E>
    <v>0.3</v>
  </elastic>
  <bond type="neo-Hookean">
    <density>1</density>
    <E>0.52</E>
    <v>0.3</v>
  </bond>
  <relaxation type="relaxation-exp-dist-user">
    <tau type="math">1.0+2.0*(K2^0.5)</tau>
  </relaxation>
</material>
```

_Example 2:_
```xml
<material id="1" name="RVE UC" type="uncoupled reactive viscoelastic">
  <kinetics>1</kinetics>
  <trigger>1</trigger>
  <k>25</k>
  <elastic type="Mooney-Rivlin">
    <density>1</density>
    <c1>0.025</c1>
    <c2>0</c2>
  </elastic>
  <bond type="Mooney-Rivlin">
    <density>1</density>
    <c1>0.025</c1>
    <c2>0</c2>
  </bond>
  <relaxation type="relaxation-exp-dist-user">
    <tau type="point">
      <interpolate>SMOOTH</interpolate>
      <points>
        <point>0.00, 1.00</point>
        <point>0.25, 2.00</point>
        <point>0.50, 2.41</point>
        <point>0.75, 2.73</point>
        <point>1.00, 3.00</point>
      </points>
    </tau>
  </relaxation>
</material>
```

