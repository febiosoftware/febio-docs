The `vector` mat3d valuator generates a $3 \times 3$ orthonormal matrix using the two vectors `a` and `b` defined by the user. It is assumed that `a` and `d` are not collinear. 

First, let $\hat{\mathbf{a}}=\mathbf{a}/\left||\mathbf{a} \right||$ and $\hat{\mathbf{d}}=\mathbf{d}/\left||\mathbf{d} \right||$. Then, the three vectors are determined from, 

\[\begin{align}
  & {{\mathbf{e}}_{1}}=\hat{\mathbf{a}} \\ 
 & {{\mathbf{e}}_{3}}=\hat{\mathbf{a}}\times \hat{\mathbf{d}} \\ 
 & {{\mathbf{e}}_{2}}={{\mathbf{e}}_{3}}\times {{\mathbf{e}}_{1}} \\ 
\end{align}\]

From this, the orthonormal matrix is constructed,

\[
\mathbf{Q}=\left[ \begin{matrix} {\mathbf{e}_{1}} & {\mathbf{e}_{2}} & {\mathbf{e}_{3}} \end{matrix} \right]
\]
