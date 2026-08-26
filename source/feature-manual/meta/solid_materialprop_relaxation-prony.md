The material type for this relaxation function is `relaxation-Prony`.

The reduced relaxation function for this material type is given by

\[
g\left(t\right)=\frac{\sum_{i=1}^{6}\gamma_{i}e^{-t/\tau_{i}}}{\sum_{i=1}^{6}\gamma_{i}}
\]

The coefficients $\gamma_{i}$ are normalized by $\sum_{i}\gamma_{i}$ to enforce $g\left(0\right)=1$.