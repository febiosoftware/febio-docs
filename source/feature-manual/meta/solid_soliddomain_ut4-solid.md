The `ut4-solid` is a special formulation for tetrahedral elements that uses a nodally-averaged integration rule, as proposed by Gee et al. [^1]. This formulation requires additional parameters. 

The `alpha` parameter defines the amount of "blending" between the regular tet-contribution and the nodally integrated contribution. The value must be between 0 and 1, where 0 means no contribution from the regular tet and 1 means no contribution from the nodally averaged tet. The `iso_stab` parameter is a flag that chooses between two slightly different formulations of the nodally integrated tet. When set to 0, the stabilization is applied to the entire virtual work, whereas when set to 1 the stabilization is applied only to the isochoric part. See the [FEBio Theory Manual](https://febio.org/knowledgebase) for a detailed description of this formulation.

```
<SolidDomain name="Part1" type="ut4-solid" mat="material1">
  <alpha>0.05</alpha>
  <iso_stab>0</iso_stab>
</SolidDomain>
```

[^1]: Gee, M.W., Dohrmann, C.R., Key, S.W., and Wall, W.A., "A uniform nodal strain tetrahedron with isochoric stabilization", Int. J. Numer. Meth. Engng (2009), pp. 429-443.