This is the default auto-time stepper used by FEBio and will adjust the time step size depending on the convergence stats of the previous time step.

The `dtmin` and `dtmax` values are used to constrain the range of possible time step values. The `opt_iter` defines the estimated optimal number of quasi-Newton iterations. If the actual number of iterations is less than or equal to this value the time step size is increased, otherwise it is decreased, as detailed further below.

When a time step fails (e.g. due to a negative Jacobian), FEBio will retry the time step with a smaller time step size. The `max_retries` parameter determines the maximum number of times a timestep may be retried before FEBio error terminates. The new time step size is determined by the ratio of the time step size before restarts started and `max_retries`+1. For example, if the time step size is 0.1 and `max_retries` is set to 4, then the time step size is adjusted by 0.02: The first retry will have a step size of 0.08; the next will be 0.06, and so on. Specifically, the new time step size is determined as follows. (This is only for the case when the `aggressiveness` parameter is set to zero.)

\[
\Delta t^{k+1}=\Delta t^{k}-\Delta t^{0}/\left(m_{\mathrm{max}}+1\right)
\]

Here, $\Delta t^{k}$ is the current time step size, $\Delta t^{k+1}$ is the new time step size, $\Delta t^{0}$ is the time step size before retries started, and $m_{\mathrm{max}}$ is the max number of retries (i.e. `max_retries`). 

When the time step succeeds, the time step size will be adjusted by comparing the opt_iter parameter to the actual number of iterations it took to converge. If the actual number of iterations is larger than `opt_iter`, the time step size will be decreased. 

\[
\Delta t^{k+1}=\Delta t^{k}-\left(\Delta t^{k}-\Delta t_{\mathrm{min}}\right)\left(1-r\right)
\]

Here, $\Delta t^{k}$ is the current time step size, $\Delta t^{k+1}$ is the new time step size, $\Delta t_{\mathrm{min}}$ is the minimum time step size and $r=\sqrt{n_{\mathrm{opt}}/n}$, where $n$ is the number of iterations and $n_{\mathrm{opt}}$ is the optimal number of iterations as specified by the user (i.e. `opt_iter`).

On the other hand, if the actual number of iterations is less than `opt_iter`, then the time step size will be increased. The exact equation follows. 

\[
\Delta t^{k+1}=\Delta t^{k}+\left(\Delta t_{\mathrm{max}}-\Delta t^{k}\right)\mathrm{min}\left(0.2,r-1\right)
\]

In addition, the new time step size is enforced to be less than 5 times the old time step size, to prevent the time step size from growing too fast. After calculating the new time step size, it will be ensured that the new timestep size falls within the range defined by dtmin and dtmax and that must-points are respected. 

When FEBio fails to converge a time step, the time step size is reduced and then FEBio tries to solve the time step again. The algorithm for determining the reduced time step size, depends on the aggressiveness parameter. 

(a) aggressiveness = 0 (default): $\Delta t^{k+1}=\Delta t^{k}-\Delta t^{0}/\left(m_{\mathrm{max}}+1\right)$.

(b) aggressiveness = 1: $\Delta t^{k+1}=\gamma\Delta t^{k}$, where $\gamma$ is the cutback factor (i.e. the `cutback` parameter). 

### must-points
The user can specify a load curve for the `dtmax` parameter. This load curve is referred to as the _must-point curve_ and serves two purposes. Firstly, it defines the value of the `dtmax` parameter as a function of time. This can be useful, for instance, to enforce smaller time steps during rapid loading or larger time steps when approaching steady-state in a transient analysis. Secondly, the time points of the dtmax loadcurve define so-called _must-points_. A must-point is a time point where FEBio must pass through. This is useful for synchronizing the auto-time stepper with the loading scenario. For instance, when loading starts at time 0.5, adding a must-point at this time will guarantee that the timestepper evaluates the model at that time. In conjunction with the `PLOT_MUST_POINT` value of the plot_level parameter, this option can also be used to only write results to the plotfile at the specified time points. Consider the following example.

```xml
<dtmax lc="1">0.1</dtmax>
...
<loadcontroller id="1" type="loadcurve">
  <interpolate>STEP</interpolate>
  <points>
    <point>0,0</point>
    <point>0.5, 0.1</point>
    <point>1.0, 0.2</point>
  </points>
</loadcontroller>
```

This example defines load curve 1 as the must-point curve. This curve defines three points where FEBio will pass through (namely 0, 0.5 and 1.0). The values of each time point is the value of the maximum time-step size (`dtmax`). Since the curve is defined as a step-function, each value is valid up to the corresponding time-point. Thus, between time 0 and time 0.5, the maximum time step value is 0.1. Between 0.5 and 1.0 the maximum time step value is 0.2. If the plot_level parameter is set to PLOT_MUST_POINTS, then only the three defined time points will be stored to the plotfile.

Note that when specifying a loadcurve for the dtmax parameter, the value of this parameter will be ignored. 

