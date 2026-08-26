The material type for this relaxation function is `relaxation-Park-dist-user`.

The reduced relaxation function for this material type is given by

\[
g\left(\mathbf{F}\left(v\right);t-v\right)=\frac{1}{1+\left(\frac{t-v}{\tau}\right)^{\beta}}
\]

where $\tau\left(K_{2}\left(v\right)\right)$ and $\beta\left(K_{2}\left(v\right)\right)$ are user-specified functions, given either as mathematical expressions or loadcurves. The definition of $K_{2}\left(v\right)$ is given in Section [relaxation-exp-dist-user](solid_materialprop_relaxation-exp-dist-user.md) and this section also provides examples of how to specify these functions.

