See Section [relaxation-malkin](solid_materialprop_relaxation-malkin.md) for the description of this relaxation function. When the material parameters vary with the distortional strain $K_{2}$ according to

\[
\begin{aligned}\tau_{1}\left(K_{2}\right) & =\tau_{10}+\tau_{11}\exp\left(-\frac{K_{2}}{s_{1}}\right)\\
\tau_{2}\left(K_{2}\right) & =\tau_{20}+\tau_{21}\exp\left(-\frac{K_{2}}{s_{2}}\right)
\end{aligned}
\]

 The material type is `relaxation-Malkin-distortion`.

 The definition of $K_{2}$ is given in [relaxation-exp-dist-user](solid_materialprop_relaxation-exp-dist-user.md) and examples of how to specify these functions can be found there as well.

