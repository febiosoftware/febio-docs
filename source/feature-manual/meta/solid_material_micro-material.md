To model first-order homogenization use the `micro-material` material.

Homogenization refers to the process of evaluating the physical response of a macro model by explicitly solving a separate finite element model that represents the micro structure of the material. This micro-model is referred to as the Representative Volume Element (RVE). In the first-order approach it is assumed that the macro and micro scales are separated, which implies that the size of the RVE is negligible compared to the size of the macro model.

### Macro model definition

For the most part, the definition of the macro-model is a standard finite element model with properly chosen boundary conditions. The use of first-order homogenization is controlled entirely by the material definition. 

The `RVE` parameter defines the file name of the RVE model. The RVE is a standard FE model, although somewhat slimmed down. See the `rve_type` parameter definition and the section RVE model definition below.

The `rve_type` parameter determines the type of RVE (and its assumed boundary conditions) that will be used and must be one of the following values.

|rve_type| description|
|--------|------------|
|0|	Prescribed displacement RVE: The position of all RVE boundary nodes is fully prescribed|
|1|	Periodic RVE: RVE with periodic boundary constraints. Constraints are enforced with linear constraints. |

The `bc_set` parameter defines the name of the nodeset (defined in the RVE model), that defines the outside surface. In general, this parameter does not need to be defined. It is only needed for problems using rve_type = 0, and for which the RVE geometry is not a closed cube. 

By default, FEBio will only output the deformation of the macro model to the plot file. It will not output any results from the RVE models. (Given there could be thousands of RVE models, this would be too cumbersome to do.) However, users can request FEBio to output the deformation of the RVE model at specific points in the model using the probe option. The `probe` property requires the following parameter.

|probe parameter|description|
|---------------|-----------|
|element_id     | the ID of the element to probe|
|gausspt        | the index of the integration point|
|file           | output file name for RVE model|

### RVE model definition

The RVE model is a standard FE model, with a few caveats.

* The time stepping parameters will be ignored, since the macro model controls the time stepping of the RVE to make sure that both models advance in sync. 

* The boundary conditions of the RVE depend on the rve_type parameter: 

    * `rve_type` = 0: The RVE model should not have any boundary conditions applied. The RVE may define a nodeset that defines the outside surface of the RVE. This is generally not needed, but must be defined when the RVE geometry is not a closed cube. 

    * `rve_type` = 1: The RVE should have periodic constraints applied for all opposing surfaces. 

* The RVE model does not need an Output section, but may define the plotfile section. This will be used to define the contents of the probe's plotfiles. 

* The size of the RVE is assumed to be much smaller than the macro model. It is allowed to use a different length unit for the coordinates of the RVE nodes. However, the unit of stress must be the same for both the macro model and the RVE model. 

