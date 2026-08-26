The contact potential method is based on the formulation by Kamensky et.al. [^1]. In this formulation, a repulsive potential is defined between two opposing surfaces. A force is generated that aims to prevent physical contact between the two surfaces. As a result, there will always be a small gap between the contacting surfaces. Note that this is the opposite of what happens for the other sliding contact interfaces, which require physical contact (and even a little bit of penetration) before a contact force can be generated. 

The `kc` parameter defines the scale factor for the force. This has a similar purpose as the penalty factor in other sliding contact interfaces. 

The parameter `p` defines the order of the potential. The paper discusses why the value 4 is in a sense an optimal value so it is recommend to use the default value.

The potential is divided in an "inner" and "outer" region. If $r$ is the distance from a point on the primary contact surface to the opposing secondary surface, then the "inner" region is defined by the criterion $0<r<R_{in}$ and the "outer" region is defined by $R_{in}<r<R_{out}$. The contact force is stronger in the inner region.

![FigContactPotential.png](figs/FigContactPotential.png)
/// figure-caption
Illustration of force applied by the contact potential and the relevant parameters that affect the force. 
///

The `R0_min` parameter defines the minimum distance between two potential contacting points in the reference configuration. In other words, two points whose initial distance was smaller than `R0_min` will not be considered as a valid contact pair. This parameter is important in self-contact to avoid neighboring points from generating contact forces. The default value of 0 indicates that this criterion is not used. 

The `w_tol` parameter defines a local normal criterion for a potential pair: If the absolute value of the cosine of the angle between the two local normals is less than w_tol, the two points are not considered in contact. In other words, the two normals have to point in the "same direction" in order for the two contacting points to be in contact. This criterion can be useful in cases of self-contact in order to avoid invalid contact pairs. A value of 0 effectively ignores this criterion. 

By default, the contact potential will ignore immediate neighbors of faces as candidates for contact pairing. This is done to avoid creating contact pairs that likely will always lie within the `R_out` distance. However, if immediate neighbors should be considered as possible contact pairs, then this behavior can be disabled by setting the `exclude_neighbors` parameter to 0. 

_Example:_
```xml
<contact type="contact potential" name="FacetOnFacetSliding1" surface_pair="FacetOnFacetSliding1">
    <kc>1e-6</kc>
    <p>4</p>
    <R_in>0.01</R_in>
    <R_out>0.05</R_out>
</contact>
```


[^1]: Kamensky, David, Xu, Fei, Lee, Chung-Hao, Yan, Jinhui, Bazilevs, Yuri, and Hsu, Ming-Chen, "A contact formulation based on a volumetric potential: Application to isogeometric simulations of atrioventricular valves", Computer Methods in Applied Mechanics and Engineering 330 (2018), pp. 522-546.