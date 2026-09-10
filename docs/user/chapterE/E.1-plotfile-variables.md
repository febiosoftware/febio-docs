# E.1 Plotfile Variables {: #sec:Plotfile-Variables }

FEBio supports two main data output mechanisms: the plot file and the log file. The plot file is a binary format that stores the data in format that makes it easy to process with FEBio Studio. The log file uses a text format that is more convenient for processing data further via scripting. See [Output Section](../chapter3/3.19-output-section.md#sec:Output-Section) to learn more about these features. This appendix list the variables that are supported by these two output formats.

There are four categories of plot file variables:

- **Nodal:** These typically correspond to data that is directly available at nodes. For instance, the primary solution variables are usually stored as nodal variables. (E.g. “displacement”)

- **Element:** These quantities correspond to data that is typically stored on the elements (e.g. stress). In FEBio, element data is usually stored at the integration points during the solution phase. Since this is often not a convenient format for post-processing, element data is processed before export and will be written to the plot file as either a constant, element-averaged value, or projected to the nodes of the element.

- **Surface:** These quantities correspond to data that is only available at the surface of the mesh (e.g. contact traction). If the surface data is defined at the nodes of the surface, it will be written directly to the plot file. However, if the data is associated with the surface facets - or more accurately, with the integration points of the surface facet - then it will be processed before export, and a constant, facet-averaged value, will be written to the plot file.

- **Rigid body:** These are quantities that correspond to data stored on rigid bodies.

The following table lists the possible values for the _type_ attribute of the plot file variable tag.

An asterisk (*) in the Category column denotes that the attribute is required and must be included in the definition of the plot variable.

The data type column specifies the type of the data. The following table lists the available data types.

<div markdown="1" style="display: flex; justify-content: center;">

| **Data Type** | **Description** |
|---|---|
| SCALAR | a single scalar value |
| VEC3 | a three-component vector |
| MAT3 | a 3x3 matrix |
| MAT3D | a diagonal 3x3 matrix (only diagonal components are stored) |
| MAT3S | a symmetric 3x3 matrix (only 6 components are stored) |
| TENS4S | a 4th order tensor with both major and minor symmetries. |

</div>

FEBio calculates element variables at the integration points. However, this is not convenient for output, so by default the integration point values are averaged over the element and a single value per element is stored. In FEBio Studio, this data is further processed and in order to get a unique nodal value, the values of adjacent elements are averaged. For linear elements and a sufficiently fine mesh, this typically produces an accurate and smooth representation of the datafield. However, for higher-order elements, this often produces artifacts, such as “bubbles” that degrade the accuracy. For these types of meshes, it may be better to use one of the other available recovery methods. At this time, FEBio offers two alternative recovery methods that often produce better results with higher-order meshes:

1. SPR method: The SPR (Superconvergent Patch Recovery) method fits at each node a quadratic function to the surrounding integration point values. The value of this quadratic function at the node will be stored to the plotfile.

1. Nodal projection: The nodal projection method extrapolates the integration point values to the nearest nodes and stores those values to the plot file.
