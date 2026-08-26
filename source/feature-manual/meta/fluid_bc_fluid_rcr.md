This boundary condition models a three-element Windkessel outflow condition on a surface in a fluid, fluid-FSI or fluid-solutes analysis, as described in [^1]. It prescribes an elastic pressure p on a surface, which satisfies the ordinary differential equation

\[
p+\tau\frac{dp}{dt}=\left(R_{d}+R\right)q+R\tau\frac{dq}{dt}+p_{d}+\tau\frac{dp_{d}}{dt},\quad\tau=R_{d}C
\]

where $R$ is the upstream flow resistance (series resistance), $R_{d}$ is the downstream flow resistance and $C$ is the downstream flow capacitance (parallel $R_{d}C$ element downstream of $R$), whereas $q$ is the volumetric flow rate across the surface (calculated internally); $p_{d}$ is an optional downstream offset pressure, which may be associated with a load controller to produce a function of time. The actual pressure $p$ obtained by solving this differential equation is converted to a dilatation and prescribed as an essential boundary condition at the nodes of the facets. Since the pressure is the solution of an ordinary differential equation, the user may also optionally specify the initial condition for the pressure.

```
<bc name="FluidRCR1" type="fluid RCR" surface="FluidRCR1">
  <R>1</R>
  <Rd>10</Rd>
  <capacitance>0.5</capacitance>
  <pressure_offset>0</pressure_offset>
  <initial_pressure>0</initial_pressure>
</bc>
```

By setting $C=0$ we recover the fluid resistance surface load described in Section [Fluid-Resistance](fluid_bc_fluid_resistance.md), with flow resistance equal to $R_{d}+R$. By setting $R$ to zero we can have simulate a parallel $R_{d}C$ circuit.

Internally, the ordinary differential equation presented above is solved numerically using a standard finite difference scheme,

\[
p_{n+1}=\left(\frac{R_{d}}{1+\frac{\tau}{\Delta t}}+R\right)q_{n+1}+\frac{\tau}{\Delta t+\tau}\left(p_{n}-p_{d,n}-Rq_{n}\right)+p_{d,n+1}
\]

where $f_{n+1}$ is the value of any function $f\left(t\right)$ at the current time step $t_{n+1}$, $f_{n}$ is its value at the previous time step $t_{n}$, and $\Delta t=t_{n+1}-t_{n}$ is the time increment.

[^1]: Vignon-Clementel, Irene E, Figueroa, C Alberto, Jansen, Kenneth E, and Taylor, Charles A, "Outflow boundary conditions for three-dimensional finite element modeling of blood flow and pressure in arteries", Comput. Methods Appl. Mech. Engrg. 195, 29 (2006), pp. 3776--3796.