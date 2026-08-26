The `spherical` mat3d valuator produces an orthonormal $3 \times 3$ matrix. 

The parameter `center` defines the center of a sphere $\mathbf{o}$.
The parameter `vector` defines a vector $\mathbf{v}$. 

Assume $\mathbf{p}$ the position of a point at which we want to calculate a $3 \times 3$ matrix. 

Let $\mathbf{r}=\mathbf{p} - \mathbf{o}$, and define $\mathbf{R}$ the rotation matrix that rotates $\mathbf{e}_x=(1,0,0)$ to $\mathbf{r}$. Then define,

\[
    \mathbf{a} = \mathbf{R}\,\mathbf{v}
\]

Now define $\mathbf{d}=(0,1,0)$ or $\mathbf{d}=(0,0,1)$ so that $\mathbf{a} \cdot \mathbf{d}$ is smallest. 

Then construct three orthogonal vectors. 

\[
\begin{align}
   &{\mathbf{c} = \mathbf{a} \times \mathbf{d}} \\
   &{\mathbf{b} = \mathbf{c} \times \mathbf{a}} \\
\end{align}
\]

Finally, construct the orthonormal matrix.

\[
\mathbf{Q}=\left[ \begin{matrix} {\mathbf{a}} & {\mathbf{b}} & {\mathbf{c}} \end{matrix} \right]
\]
