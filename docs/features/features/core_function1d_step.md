# step

**Module:** core

**Category:** function1d

**Type string:** `"step"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `x0` | x0 | 0 | $\in \mathbb{R}$ |  |
| `left_val` | left_val | 0 | $\in \mathbb{R}$ |  |
| `right_val` | right_val | 1 | $\in \mathbb{R}$ |  |


## Description

The `step` function applies a step function to the input value. The returned value is either `left_val` ($=l_0$) or `right_val` ($=l_1$), depending on whether the input falls left or right of the transition point $x_{0}$.

\[
f\left( x \right)=\left\{ \begin{matrix}
   {{l}_{0}}\quad,x<{{x}_{0}}  \\
   {{l}_{1}}\quad,x\ge {{x}_{0}}  \\
\end{matrix} \right.
\]

