Prestrain can be applied using the `prestrain elastic` material[^1]. This material acts as a wrapper to the underlying elastic constitutive model. There are two flavors of this material, one for coupled materials and one for uncoupled. In either case, the material defines two properties. 

The `elastic` property defines the elastic constitutive model. Any of the materials in FEBio could be used, however, the prestrain material has only been validated for hyperelastic materials. The second property, called prestrain, defines the prestrain generator. This property defines how the initial prestrain gradient is calculated. Currently, it can be defined as a full second order matrix or as a fiber stretch. The prestrain data can be defined at the material level or at the element level. 

The `prestrain` property defines the way that the initial prestrain gradient tensor is calculated. An algorithm that calculates the initial prestrain based on user input is here referred to as a prestrain generator. The type attribute is used to create a specific instance of a prestrain generator.



[^1]: Maas, S.A., Erdemir, A., Halloran, J.P., and Weiss, J.A., "A general framework for applications of prestrain to computational models of biological materials.", Journal of Biomechanical Behavior of Biomedical Materials 61 (2016), pp. 499-510.