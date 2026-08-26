The material type for orthotropic elasticity is `orthotropic elastic`.

The stress-strain relation for this material is given by

\[
\left[\begin{array}{c}
E_{11}\\
E_{22}\\
E_{33}\\
2E_{23}\\
2E_{31}\\
2E_{12}
\end{array}\right]=\left[\begin{array}{cccccc}
1/E_{1} & -\nu_{21}/E_{2} & -\nu_{31}/E_{3} & 0 & 0 & 0\\
-\nu_{12}/E_{1} & 1/E_{2} & -\nu_{32}/E_{3} & 0 & 0 & 0\\
-\nu_{13}/E_{1} & -\nu_{23}/E_{2} & 1/E_{3} & 0 & 0 & 0\\
0 & 0 & 0 & 1/G_{23} & 0 & 0\\
0 & 0 & 0 & 0 & 1/G_{31} & 0\\
0 & 0 & 0 & 0 & 0 & 1/G_{12}
\end{array}\right]\left[\begin{array}{c}
T_{11}\\
T_{22}\\
T_{33}\\
T_{23}\\
T_{31}\\
T_{12}
\end{array}\right]
\]

_Example:_
```xml
<material id="3" type="orthotropic elastic">
  <mat_axis type="vector">
    <a>0.866,0.5,0</a>
    <d>-0.5,0.866,0</d>
  </mat_axis>
  <E1>1</E1>
  <E2>2</E2>
  <E3>3</E3>
  <v12>0</v12>
  <v23>0</v23>
  <v31>0</v31>
  <G12>1</G12>
  <G23>1</G23>
  <G31>1</G31>
</material>
```