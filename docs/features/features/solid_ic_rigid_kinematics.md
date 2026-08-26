# rigid kinematics

**Module:** solid

**Category:** ic

**Type string:** `"rigid kinematics"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `velocity` | velocity | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ | L/t |
| `angular_velocity` | angular_velocity | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ | r/t |
| `center_of_rotation` | center_of_rotation | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ | L |


## Description

The `rigid kinematics` initial condition sets the initial velocity of a rigid body from the following equation. 

\[
\mathbf{v}_{0}=\mathbf{V}+\mathbf{\omega}\times\left(\mathbf{r}_{0}-\mathbf{c}\right)
\]

Here, $\mathbf{V}$ is the linear velocity, $\omega$  is the angular velocity, $\boldsymbol{r}_{0}$ is the initial position of the rigid body, and $\mathbf{c}$ is a position vector indicating the center of rotation. 
