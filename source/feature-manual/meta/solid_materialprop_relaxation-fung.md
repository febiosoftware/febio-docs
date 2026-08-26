This relaxation function, which is derived from a continuous relaxation spectrum, was introduced by Fung [^1]. The material type for this relaxation function is `relaxation-Fung`.

These parameters must satisfy $\tau_{2}>\tau_{1}$. The reduced relaxation function for this material type is given by

\[
g\left(t\right)=\frac{\tau_{2}e^{-t/\tau_{2}}-\tau_{1}e^{-t/\tau_{1}}+t\left[\text{Ei}\left(-\frac{t}{\tau_{2}}\right)-\text{Ei}\left(-\frac{t}{\tau_{1}}\right)\right]}{\tau_{2}-\tau_{1}}
\]

where $\text{Ei}\left(\cdot\right)$ is the exponential integral function.

[^1]: Fung, Y. C, Biomechanics: mechanical properties of living tissues (New York: Springer-Verlag, 1981).