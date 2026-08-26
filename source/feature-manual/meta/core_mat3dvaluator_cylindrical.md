The `cylindrical` mat3d valuator generates an orthonormal matrix based on cylindrical coordinates. 

First, three perpendicular unit vectors are calculated. The first vector is generated using the parameters defined above. Let $\mathbf{r}$ be the position vector at which we want to generate a mat3d. Let $\mathbf{c}$ be the `center` parameter, $\mathbf{a}$ the `axis` parameter and $\mathbf{t}$ the `vector` parameter. Then, the vector from $\mathbf{r}$ to the axis is,

\[
    \mathbf{b}= \left( \mathbf{r} - \mathbf{c} \right) - \mathbf{a} \left( \mathbf{a} \cdot \left( \mathbf{r} - \mathbf{c}\right) \right)
\]

Then, the corresponding unit vector $\hat{\mathbf{b}}$ is found from,

\[
\hat{\mathbf{b}} = \frac{\mathbf{b}}{\left||\mathbf{b}\right||}
\]

Next, we find the rotation matrix $\mathbf{R}$ that rotates $\mathbf{e}_1=\left(1,0,0 \right)$ to $\hat{\mathbf{b}}$. 

The first unit vector is then defined by

\[
    \mathbf{a}_1 = \mathbf{R}\,\hat{\mathbf{t}}
\]

To find the third vector, we first calculate $\mathbf{d}=\mathbf{R}\,\mathbf{e}_2$. (If that produces a vector that is too close to $\mathbf{a}$, we choose instead $\mathbf{d}=\mathbf{R}\,\mathbf{e}_2$.)

The third vector is then defined by,

\[
    \mathbf{a}_3 = \frac{\mathbf{a}_1\times\mathbf{d}}{\left|| \mathbf{a}_1\times\mathbf{d} \right||}
\]

Finally, the second vector is found from,

\[
    \mathbf{a}_2 = \mathbf{a}_3\times\mathbf{a}_1
\]

The orthonormal matrix is then defined as the matrix,

\[
\mathbf{Q}=\left[ \begin{matrix} {\mathbf{a}_{1}} & {\mathbf{a}_{2}} & {\mathbf{a}_{3}} \end{matrix} \right]
\]
