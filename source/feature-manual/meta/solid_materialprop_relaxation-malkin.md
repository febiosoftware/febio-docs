This relaxation function is derived from the continuous relaxation spectrum given in [^1]. The material type for this relaxation function is `relaxation-Malkin`.

These parameters must satisfy $\tau_{2}>\tau_{1}>0$. When $\beta>1$, the reduced relaxation function for this material type is given by

\[
g\left(t\right)=\frac{\left(\beta-1\right)t^{1-\beta}}{\tau_{1}^{1-\beta}-\tau_{2}^{1-\beta}}\left[\Gamma\left(\beta-1,\frac{t}{\tau_{2}}\right)-\Gamma\left(\beta-1,\frac{t}{\tau_{1}}\right)\right]
\]

where $\Gamma\left(a,z\right)$ is the incomplete gamma function. In the limit as \beta\to1 this function reduces to the form given by [^2],

\[
g\left(t\right)=\frac{\Gamma\left(0,\frac{t}{\tau_{2}}\right)-\Gamma\left(0,\frac{t}{\tau_{1}}\right)}{\ln\frac{\tau_{2}}{\tau_{1}}}=\frac{\text{Ei}\left(-\frac{t}{\tau_{2}}\right)-\text{Ei}\left(-\frac{t}{\tau_{1}}\right)}{\ln\frac{\tau_{1}}{\tau_{2}}}
\]

where $\text{Ei}\left(z\right)$ is the exponential integral function.

[^1]: Malkin, A Ya, "Continuous relaxation spectrum-its advantages and methods of calculation", Applied Mechanics and Engineering 11, 2 (2006), pp. 235.

[^2]: Fung, Y. C, Perrone, Nicholas, and Anliker, M, Biomechanics, its foundations and objectives (Englewood Cliffs, N.J.: Prentice-Hall, 1972).