The material type of a reactive elasto-plastic damage solid with kinematic hardening is `reactive plastic damage`.

The `elastic` property specifies the constitutive relation of the intact (unconstrained) elastic material and associated material properties. 

The `yield_criterion` property defines the yield criterion $\Phi$.

The `flow_curve` property specifies the relation between bond mass fractions $w_{\beta}$ and apparent yield stresses $\Upsilon_{\beta}$ for the bond family $\beta$.

If only plastic damage needs to be modeled, the tags `elastic_damage` and `elastic_damage_criterion` may be omitted. If `plastic_damage` and `plastic_damage_criterion` are also omitted the material response becomes identical to the `reactive plasticity` material described in Section [reactive plasticity](solid_material_reactive_plasticity.md).

_Example:_ A-533 Grade B class 1 nuclear pressure vessel steel (mm-N-s units)
```xml
<material id="1" type="reactive plasticity">
  <isochoric>1</isochoric>
  <elastic type="neo-Hookean">
    <density>8.00e-9</density>
    <E>206.9e3</E>
    <v>0.29</v>
  </elastic>
  <yield_criterion type="DC von Mises stress"/>
  <flow_curve type="PFC paper">
    <nf>10</nf>
    <Y0>458</Y0>
    <Ymax>730</Ymax>
    <w0>0.985</w0>
    <we>0.00072</we>
    <r>1</r>
  </flow_curve>
  <plastic_damage type="CDF Weibull">
    <mu>3.3</mu>
    <alpha>3</alpha>
    <Dmax>1</Dmax>
  </plastic_damage>
  <plastic_damage_criterion type="DC octahedral shear strain"/>
</material>
```