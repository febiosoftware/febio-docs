# fluid resistance

**Module:** fluid

**Category:** bc

**Type string:** `"fluid resistance"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `R` | R | 0 | $\in \mathbb{R}$ | F.t/L^5 |
| `pressure_offset` | pressure_offset | 0 | $\in \mathbb{R}$ | P |


## Description

In a fluid, fluid-FSI or fluid-solutes analysis, this boundary condition prescribes an elastic pressure $p=R\,q+p_{d}$ on a surface, where R is the flow resistance and q is the volumetric flow rate across the surface (calculated internally); $p_{d}$ is an optional offset pressure. The pressure p is converted to a dilatation and prescribed as an essential boundary condition at the nodes of the facets.

```
<bc type="fluid resistance" surface="surface1">
  <R lc="1">7.93e+07</R>
  <pressure_offset lc="2">10640</pressure_offset>
<bc>
```
