# solid_bound

**Module:** multiphasic

**Category:** globaldata

**Type string:** `"solid_bound"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `density` | density | 1 | $\in \mathbb{R}$ | M/L^3 |
| `molar_mass` | molar_mass | 1 | $\in \mathbb{R}$ | M/n |
| `charge_number` | charge_number | 0 | $\in \mathbb{Z}$ |  |


## Description

In multiphasic analyses with chemical reactions involving solid-bound molecules, a unique identifier must be associated with each such molecule in order to enforce consistent properties across the entire model. This unique identification is achieved by listing each solid-bound species that appears in the entire finite element model and associating it with a unique id, name, charge number, molar mass and density:

```
<Globals>
  <SolidBoundMolecules>
    <solid_bound id="1" name="CS">
      <charge_number>-2</charge_number>
      <molar_mass>463.37</molar_mass>
      <density>1.5<density>
    </solid_bound >
  </SolidBoundMolecules >
</Globals>
```

The `id` number should be referenced in the `sbm` attribute of solid-bound molecules when included in the definition of a multiphasic material. The `charge_number` parameter is used in the calculation of the fixed charge density contributed by this solid-bound molecule to the overall solid matrix fixed-charge density. The `density` parameter is used in the calculation of the contribution of this molecule to the referential solid volume fraction. The `density` and `molar_mass` parameters are used in the calculation of the molar volume of this molecule in chemical reactions.


