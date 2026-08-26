# relaxation-Prony

**Module:** solid

**Category:** materialprop

**Type string:** `"relaxation-Prony"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `t1` | relaxation time t1 | 1 | $\ge 0$ | t |
| `t2` | relaxation time t2 | 1 | $\ge 0$ | t |
| `t3` | relaxation time t3 | 1 | $\ge 0$ | t |
| `t4` | relaxation time t4 | 1 | $\ge 0$ | t |
| `t5` | relaxation time t5 | 1 | $\ge 0$ | t |
| `t6` | relaxation time t6 | 1 | $\ge 0$ | t |
| `g1` | coefficient g1 | 0 | $[0, 1]$ |  |
| `g2` | coefficient g2 | 0 | $[0, 1]$ |  |
| `g3` | coefficient g3 | 0 | $[0, 1]$ |  |
| `g4` | coefficient g4 | 0 | $[0, 1]$ |  |
| `g5` | coefficient g5 | 0 | $[0, 1]$ |  |
| `g6` | coefficient g6 | 0 | $[0, 1]$ |  |


## Description

The material type for this relaxation function is `relaxation-Prony`.

The reduced relaxation function for this material type is given by

\[
g\left(t\right)=\frac{\sum_{i=1}^{6}\gamma_{i}e^{-t/\tau_{i}}}{\sum_{i=1}^{6}\gamma_{i}}
\]

The coefficients $\gamma_{i}$ are normalized by $\sum_{i}\gamma_{i}$ to enforce $g\left(0\right)=1$.
