In biphasic-solute, triphasic, and multiphasic analyses, a unique identifier must be associated with each solute in order to enforce consistent nodal degrees of freedom across boundaries of different materials. This unique identification is achieved by listing each solute species that appears in the entire finite element model and associating it with a unique id, name, and providing its charge number $z^{\alpha}$, molar mass $M^{\alpha}$, and density $\rho_{T}^{\alpha}$:

```
<Globals>
  <Solutes>
    <solute id="1" name="Na">
      <charge_number>1</charge_number>
      <molar_mass>22.99</molar_mass>
      <density>0.97</density>
    </solute>
    <solute id="2" name="Cl">
      <charge_number>-1</charge_number>
      <molar_mass>35.45</molar_mass>
      <density>3.21</density>
    </solute>
    <solute id="3" name="Glc">
      <charge_number>0</charge_number>
      <molar_mass>180.16</molar_mass>
      <density>1.54</density>
    </solute>
  </Solutes>
</Globals>
```

These solute identification numbers should be referenced in the `sol` attribute of solutes when defining a biphasic-solute, triphasic or multiphasic material.

The `molar_mass` and `density` parameters of solutes are needed only when solutes are involved in chemical reactions. When not specified, default values for these properties are set to 1.
