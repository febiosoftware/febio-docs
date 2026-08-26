# JFNK

**Module:** core

**Category:** newtonstrategy

**Type string:** `"JFNK"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `jfnk_eps` | jfnk_eps | 1e-06 | $\in \mathbb{R}$ |  |


## Description

This is an implementation of the Jacobian-Free-Newton-Krylov method. When using this Newton strategy, you must also use an iterative linear solver such as FGMRES. 
