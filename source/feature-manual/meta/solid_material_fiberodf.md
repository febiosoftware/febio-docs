The Fiber ODF constitutive model is a special version of the Continuous Fiber Distribution constitutive model, with its own distribution type, and a unique integration scheme. It utilizes a set of non-parametric orientation distribution functions which are each defined by a position in space, and a series of spherical harmonic coefficients. This allows for the definition of extremely detailed ODFs of any shape.

This constitutive model is intended to be used in conjunction with the Fiber ODF Analysis tool in FEBio Studio, which directly analyzes 3D image data and generates ODFs based on fibers in the image. For more information on this tool and the algorithms involved please see the Fiber ODF Analysis section in the FEBio Studio User Manual, and the manuscripts associated with this tool [#rauff_algorithmic_2024, #rauff_nonparametric_2022]. 

When an FE simulation is run using this material, some preprocessing is done on the ODFs in order to reduce the computational load during the simulation. The following is a description of these preprocessing steps. For a more detailed description, please see the associated manuscript [#rauff_algorithmic_2024]. 

In order to prevent sharp changes in the fiber direction between elements, a unique ODF is interpolated for each element in the mesh based on the element’s physical distance from the nearby ODFs in the discrete ODF field. This interpolation is done using a weighted-mean approach utilizing the objective distance metric afforded by the Fisher-Rao inner product space [#rauff_algorithmic_2024]. This results in a unique ODF for each FE element in the domain of the constitutive model which smoothly transition between ODFs defined in each of the original image's subdivisions. If only a single ODF is defined for the domain (in other words, if the image was not subdivided before the analysis) then this step is skipped and the original ODF is used for all elements in the domain.

Constitutive models using continuous fiber distributions require an efficient integration scheme over the unit sphere to compute stress contributions from the fiber family. Because there is no analytical representation of these non-parametric ODFs, this integration is performed by sampling the values of the ODFs at its defined points. To ensure faithful representation of the ODF, all ODF calculations up to this point in the process use a high resolution, pre-defined set evenly-spaced points on the unit sphere. Integrating the stress contributions across the ODFs at their full resolution proved to be prohibitively computationally expensive, as this integration must occur at every integration point in the FE mesh for each stress calculation in the analysis.

To address this issue, we developed a mechanism to reduce the number of sampling points on the ODF using an approach based on finite element remeshing technology. The gradient of each ODF is calculated, and a triangulated mesh of the ODF probability surface and its gradient is passed to the mmg remeshing library. The mmg algorithm remeshes a surface of triangular elements, adjusting the relative nodal density of the ODF mesh based on the magnitude of the gradient, resulting in a higher sampling density in areas of high curvature while reducing the overall number of sample points, thereby preserving sharp changes in orientation (see figure below).

![fiberODFRemesh.png](figs/fiberODFRemesh.png)
/// figure-caption
Spherical representations of an ODF showing the results of the remeshing algorithm. (A) A full-resolution, spherical representation of an ODF. (B) An enlarged portion of the same ODF showing the area inside the black square in panel A. In this panel, the ODF’s mesh has been made visible to show the density of sampling points at the full-resolution of 40,962 points. (C) The remeshed surface of the same ODF showing the area inside the black square in panel A. The density of the ODF’s sampling points has been greatly reduced in the regions of the ODF where there is little variation in the ODF’s value, while maintaining high density in regions where there are sharp changes in value. This preserves the general shape of the ODF while significantly reducing the number of sampling points.
///

The number of integration points in the remeshed ODFs varies depending on the ODF topology, but the number points is generally reduced by about two orders of magnitude. Since the resampling of the ODFs only takes place once, at the beginning of the FE analysis, the time required for the remeshing step is small relative to the overall time involved in a FE analysis. The reduction in points dramatically increases the speed of stress computations without significantly altering the results. After the interpolation and remeshing steps, the material initialization is complete, and the FE analysis continues normally.

The `fibers` property defines the fiber constitutive relation and associated material properties. The Fiber ODF material takes any number of `fiber-odf` tags as parameters, each with a position in space, and a list of spherical harmonic coefficients.

_Example:_
```xml
<material id="1" name="Material" type="uncoupled solid mixture">
  <solid type="Mooney-Rivlin">
    <density>1</density>
    <c1>1</c1>
    <c2>0.3</c2>
  </solid>
  <solid type="fiberODF">
    <fibers type="fiber-exponential-power-law-uncoupled">
      <alpha>0</alpha>
      <beta>2</beta>
      <ksi>1</ksi>
    </fibers>
    <fiber-odf>
      <shp_harmonics>8.61001e-05,6.31376e-05, etc...</shp_harmonics>
      <position>340,300,224</position>
    </fiber-odf>
    <fiber-odf>
      <shp_harmonics>-3.28478e-05,3.90659e-06, etc...</shp_harmonics>
      <position>400,300,224</position>
    </fiber-odf>
  </solid>
</material>
```
