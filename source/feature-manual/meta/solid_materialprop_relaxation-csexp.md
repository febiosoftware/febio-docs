This relaxation function is derived from a continuous exponential relaxation spectrum, see [FEBio Theory Manual](https://febio.org/knowledgebase/). The material type for this relaxation function is `relaxation-CSexp`.

This parameter must satisfy $\tau>0$. The reduced relaxation function for this material type is given by

\[
g\left(t\right)=2\sqrt{\frac{t}{\tau}}K_{1}\left(2\sqrt{\frac{t}{\tau}}\right)
\]

where $K_{1}\left(z\right)$ is the modified Bessel function of the second kind, of order 1.

