The material type for this relaxation function is `relaxation-Park-distortion`.

The reduced relaxation function for this material type is given by

\[
g\left(\mathbf{F}\left(v\right);t-v\right)=\frac{1}{1+\left(\frac{t-v}{\tau}\right)^{\beta}}
\]

where

\[
\tau=\tau_{0}+\tau_{1}\cdot\left(K_{2}\left(v\right)\right)^{\alpha}
\]

and

\[
\beta=\beta_{0}+\beta_{1}\cdot\left(K_{2}\left(v\right)\right)^{\alpha}
\]

The definition of $K_{2}\left(v\right)$ is given in [relaxation-exp-dist-user](solid_materialprop_relaxation-exp-dist-user.md).