Assume $\mathbf{p}$ the position of a point at which we want to calculate a $3 \times 3$ matrix. 

First, find the vector to the axis 

\[
    \mathbf{b} = \left( \mathbf{p} - \mathbf{c} \right) - \mathbf{a}\left( \mathbf{a} \cdot  \left( \mathbf{p} - \mathbf{c}\right) \right)
\]

 and its length

\[
    R = \left|| \mathbf{b} \right||
\]

Define the unit vector,

\[
    \hat{\mathbf{b}} = \frac{\mathbf{b}}{\left|| \mathbf{b} \right||}
\]

Calculate the relative radius $w=(R - R_0)/(R_1 - R_0)$

Define $\mathbf{R}_{01}$ as the rotation that rotates $\mathbf{v}_0$ to $\mathbf{v}_1$ and $\mathbf{R}_w$ the rotation matrix by interpolating between the identity matrix $\mathbf{I}$ and $\mathbf{R}_{01}$ at fraction $w$. Then, define,

\[
    \mathbf{v}=\mathbf{R}_w\,\mathbf{v}_0
\]

Define $\mathbf{Q}$ the rotation matrix that rotates $\mathbf{e}_x=(1,0,0)$ to $\mathbf{b}$ and define $\mathbf{d}=\mathbf{Q}\,\mathbf{e}_y$.

Next, construct three orthogonal vectors,

\[
\begin{align}
   &{\mathbf{e}_1 = \mathbf{v}} \\
   &{\mathbf{e}_3 = \mathbf{e}_1 \times \mathbf{d}} \\
   &{\mathbf{e}_2 = \mathbf{e}_3 \times \mathbf{e}_1} \\
\end{align}
\]

Finally, construct the orthonormal matrix.

\[
\mathbf{Q}=\left[ \begin{matrix} {\mathbf{e}_{1}} & {\mathbf{e}_{2}} & {\mathbf{e}_{3}} \end{matrix} \right]
\]
