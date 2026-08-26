A `tied biphasic` interface is similar to the tied interface. It may be used for tying any combination of solid, biphasic, and rigid materials. It enforces continuity of the fluid pressure across the interface when both materials are biphasic.

Please see [tied-elastic](solid_surfaceinteraction_tied-elastic.md) for a more detailed explanation of the parameters. 

In order to model fluid flow across the interface, the user must set the `pressure_penalty` parameter. This parameter is similar to the `penalty` parameter, but acts on the pressure gap, i.e. the difference in fluid pressure across the interface.
