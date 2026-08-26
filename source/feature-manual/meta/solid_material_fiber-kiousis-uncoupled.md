This material type is `fiber-Kiousis-uncoupled`. It is based on the material model proposed by Kiousis et al. [^1] [^2] for modeling the balloon in a balloon-stent system.

The fiber strain energy density is given by

\[
\tilde{\Psi}_{n}\left(I_{n}\right)=\begin{cases}
\frac{d_{1}}{n}\left(\tilde{I}_{n}-d_{2}\right)^{n} & \tilde{I}_{n}\ge d_{2}\\
0 & \tilde{I}_{n}<d_{2}
\end{cases}\,,
\]

where $\tilde{I}_{n}=\tilde{\lambda}_{n}^{2}=\mathbf{n}_{r}\cdot\mathbf{\tilde{C}}\cdot\mathbf{n}_{r}$ is the square of the fiber stretch and $\mathbf{n}_{r}$ is the unit vector along the fiber direction in its reference configuration.

_Example:_

(Fiber model as specified in a continuous fiber distribution)

```xml
<fibers type="fiber-Kiousis-uncoupled">
  <d1>500</d1>
  <d2>2.25</d2>
  <n>3</n>
</fibers>
```

[^1]: Kiousis, DE, Gasser, TC, and Holzapfel, GA, "Smooth contact strategies with emphasis on the modeling of balloon angioplasty with stenting", International journal for numerical methods in engineering 75, 7 (2008), pp. 826--855.

[^2]: Kiousis, Dimitrios E, Wulff, Alexander R, and Holzapfel, Gerhard A, "Experimental studies and numerical analysis of the inflation and interaction of vascular balloon catheter-stent systems", Annals of Biomedical Engineering 37, 2 (2009), pp. 315--330.