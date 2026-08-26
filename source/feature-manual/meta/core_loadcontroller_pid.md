The PID controller allows users to create simple control systems where the value of one model parameter is used to control the output of another model parameter. The PID controller calculates the output value as a sum of three terms: a term proportional to the error (i.e. the difference between a user-defined target value and the measurement), a derivative term, and an integral term.

_Example:_
```xml
<load_controller id="1" type="PID">
    <var>fem.rigid_body[1].euler.z</var>
    <target>1.5708</target>
    <Kp>5</Kp>
    <Kd>1</Kd>
    <Ki>4</Ki>
</load_controller>
```