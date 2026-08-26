This material implements the constitutive model by Wang et al. [^1], which proposes a mechanism for long-range force transmission in fibrous matrices enabled by tension-driven alignment of fibers. 

The strain-energy density function is given by,

\[
W=W_{\text{b}}+W_{\text{f}},
\]

where:

\[
\begin{aligned}W_{\text{b}} & =\frac{\mu}{2}\left(\overline{I}_{1}-3\right)+\frac{\kappa}{2}\left(J-1\right)^{2},\\
W_{\text{f}} & =\stackrel[a=1]{3}{\sum}f\left(\lambda_{a}\right),
\end{aligned}
\]

and $f$ is defined via its derivative, 

\[
\frac{\partial f}{\partial\lambda_{a}}\left(\lambda_{a}\right)=\begin{cases}
0, & \lambda_{a}<\lambda_{1}\\
\frac{E_{f}\left(\frac{\lambda_{a}-\lambda_{1}}{\lambda_{2}-\lambda_{1}}\right)^{n}\left(\lambda_{a}-\lambda_{1}\right)}{n+1}, & \lambda_{1}\leq\lambda_{a}<\lambda_{2}\\
E_{f}\left[\frac{\lambda_{2}-\lambda_{1}}{n+1}+\frac{\left(1+\lambda_{a}-\lambda_{2}\right)^{m+1}-1}{m+1}\right], & \lambda_{a}\geq\lambda_{2}
\end{cases}
\]

Finally, the parameters $\lambda_{1}$ and $\lambda_{2}$ are given as follows. 

\[
\lambda_{1}	=\lambda_{c}-\lambda_{t}/2
\lambda_{2}	=\lambda_{c}+\lambda_{t}/2
\]

_Example:_
```xml
<material id="1" name="Material1" type="Shenoy">
  <density>1</density>
  <mu>0.7692</mu>
  <k>1.667</k>
  <Ef>134.6</Ef>
  <lam_c>1.02</lam_c>
  <lam_t>0.255</lam_t>
  <n>5</n>
  <m>30</m>
</material>
```

[^1]: Wang et. al., Biophysical Journal, 107, 2014, pp:2592 - 2603