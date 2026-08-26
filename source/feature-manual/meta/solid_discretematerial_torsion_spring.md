The `torsion spring` applies a force that aims to restore a discrete element's orientation to the reference configuration.

\[
    \mathbf{f} = r\,\left({\mathbf{e}_0} \cdot{\mathbf{e}_t}\right) \mathbf{P}\, {\mathbf{e}_0}
\]

where $\mathbf{e}_0$ is a unit vector along the discrete element's axis in the reference configuration, and similar for $\mathbf{e}_t$, and

\[
    \mathbf{P} =\frac{1}{l} \left( \mathbf{I} - \mathbf{e}_t \times \mathbf{e}_t \right) 
\]

Here, $l$ is the current length of the discrete element.
