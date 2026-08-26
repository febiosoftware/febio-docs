The material type for this relaxation function is `relaxation-exp-distortion`.

The reduced relaxation function for this material type is given by

\[
g\left(\mathbf{F}\left(v\right);t-v\right)=e^{-\left(t-v\right)/\tau\left[K_{2}\left(v\right)\right]}
\]

where

\[
\tau\left(K_{2}\left(v\right)\right)=\tau_{0}+\tau_{1}\cdot\left(K_{2}\left(v\right)\right)^{\alpha}
\]

In general, $K_{2}=\left|\dev\boldsymbol{\eta}\right|$ where $\boldsymbol{\eta}=\ln\mathbf{V}$ is the spatial natural (left Hencky) strain tensor and $\mathbf{V}$ is the left stretch tensor. $K_{2}$ is evaluated at the time $v$ when weak bonds from the $u$-generation start breaking.

