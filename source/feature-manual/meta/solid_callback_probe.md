The `probe` feature is used as a property of the [micro-material](solid_material_micro-material.md) and allows users to export the data of a particular RVE to a separate plot file. 

The RVE is identified by the `element_id` parameter, which identifies an element of the macro model, and the `gausspt` parameter, which identifies the particular integration point. (Each integration point has its own RVE.) 

The `file` parameter sets the output file name for the plot file. 

When the `debug` flag is enable, all the non-converged states of the RVE are also stored to the plot file. 
