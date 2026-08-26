The `local` mat3d valuator uses the local element node numbering to construct an orthonormal $3 \times 3$ matrix.

First the element in which a point $\mathbf{r}$ is located is determined. From this the nodal coordinates of the element are defined, $\mathbf{p}_n$, with $n$ ranging from 1 to the number of nodes of the element.

Let $l$ be the `local` parameter. Then, define,

\[
    \mathbf{a}=\mathbf{p}_{l_2}-\mathbf{p}_{l_1},\quad\mathbf{d}=\mathbf{p}_{l_3}-\mathbf{p}_{l_1}
\]

and the corresponding unit vectors $\hat{\mathbf{a}}=\mathbf{a}/\left||\mathbf{a} \right||$ and $\hat{\mathbf{d}}=\mathbf{d}/\left||\mathbf{d} \right||$.

Then we construct three perpendicular vectors, 

\[\begin{align}
  & {{\mathbf{e}}_{1}}=\hat{\mathbf{a}} \\ 
 & {{\mathbf{e}}_{3}}=\hat{\mathbf{a}}\times \hat{\mathbf{d}} \\ 
 & {{\mathbf{e}}_{2}}={{\mathbf{e}}_{3}}\times {{\mathbf{e}}_{1}} \\ 
\end{align}\]

From this, we define the orthonormal matrix,


\[
\mathbf{Q}=\left[ \begin{matrix} {\mathbf{e}_{1}} & {\mathbf{e}_{2}} & {\mathbf{e}_{3}} \end{matrix} \right]
\]
