The `angles` mat3d valuator uses spherical angles to set up three perpendicular vectors to produce a orthonormal matrix. 

* `theta` : the azimuth angle (angle in xy plane and $0\leqslant\theta<2\pi$)
* `phi` : declination angle (angle with respect to the z-axis and $0\leqslant\phi\leqslant\pi$)

The first vector is defined via,

\[
\mathbf{e}_{r}=\cos\theta\sin\phi\,\mathbf{e}_{1}+\sin\theta\sin\phi\,\mathbf{e}_{2}+\cos\phi\,\mathbf{e}_{3}
\]

The second and third vectors are defined as follows,

\[
\mathbf{e}_{\theta}=-\sin\theta\,\mathbf{e}_{1}+\cos\theta\,\mathbf{e}_{2}
\]

\[
\mathbf{e}_{\phi}=-\cos\theta\cos\phi\,\mathbf{e}_{1}-\sin\theta\cos\phi\,\mathbf{e}_{2}+\sin\phi\,\mathbf{e}_{\phi}
\]

The matrix is formed by using these three vectors as columns.

\[
    \mathbf{Q}=\left[ \mathbf{e}_{r} | \mathbf{e}_{\theta} |  \mathbf{e}_{\phi} \right]
\]


