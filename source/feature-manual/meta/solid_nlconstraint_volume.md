This feature implements a constraint that aims to maintain the volume enclosed by a user-specified surface using an constant pressure.

The constraint can be defined as,

\[
    c = V_t - V_0 = 0
\]

The pressure is the Lagrange multiplier that enforces this constraint. 

If the `laugon` parameter is 0, a penalty method is used. 

\[
    p = \varepsilon\,c=\varepsilon \left( V_t - V_0 \right)
\]

If `laugon` is set to 1, the augmented Lagrangian method is used. 

\[
    p^{k+1} = p^{k} + \Delta p
\]

where $\Delta p = \varepsilon\,c$.