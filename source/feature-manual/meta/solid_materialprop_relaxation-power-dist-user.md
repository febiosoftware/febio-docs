The material type for this relaxation function is `relaxation-power-dist-user`.

The reduced relaxation function for this material type is given by

\[
g\left(\mathbf{F}\left(v\right);t-v\right)=\frac{1}{\left(1+\frac{t-v}{\tau}\right)^{\beta}}
\]

where $\tau\left(K_{2}\left(v\right)\right)$ and $\beta\left(K_{2}\left(v\right)\right)$ are user-specified functions, given either as mathematical expressions or loadcurves. The definition of $K_{2}\left(v\right)$ is given in [relaxation-exp-dist-user](solid_materialprop_relaxation-exp-dist-user.md) and some examples of how to specify these functions can be found there as well.