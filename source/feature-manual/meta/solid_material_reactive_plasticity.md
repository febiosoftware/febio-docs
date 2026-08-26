The material type of a reactive elasto-plastic solid with kinematic hardening is `reactive plasticity`.

The `elastic` property defines the constitutive relation of the intact (unconstrained) elastic material and associated material properties for unconstrained materials. 

The `yield_criterion` property defines the yield criterion $\Phi$. The `flow_curve` property defines the relation between bond mass fractions $w_{\beta}$ and apparent yield stresses $\Upsilon_{\beta}$ for the bond family $\beta$.The default value in FEBio is `isochoric=1`.

_Example 1:_
Idealized elastic-perfectly plastic response of steel (mm-N-s units)

```xml
<material id="1" type="reactive plasticity">
  <elastic type="neo-Hookean">
    <density>8.05e-9</density>
    <E>200e3</E>
    <v>0.30</v>
  </elastic>
  <yield_criterion type="DC von Mises stress"/>
  <flow_curve type="PFC paper">
    <Y0>450</Y0>
  </flow_curve>
</material>
```

_Example 2:_
 Annealed mild steel (mm-N-s units)

```xml
<material id="1" type="reactive plasticity">
  <isochoric>1</isochoric>
  <elastic type="neo-Hookean">
    <density>7.85e-9</density>
    <E>205e3</E>
    <v>0.29</v>
  </elastic>
  <yield_criterion type="DC von Mises stress"/>
  <flow_curve type="PFC paper">
    <nf>15</nf>
    <Y0>220</Y0>
    <Ymax>490</Ymax>
    <w0>0.973</w0>
    <we>0</we>
    <r>1</r>
  </flow_curve>
</material>
```

_Example 3:_
Annealed copper (mm-N-s units)
```xml
<material id="1" type="reactive plasticity">
  <isochoric>1</isochoric>
  <elastic type="neo-Hookean">
    <density>7.764e-9</density>
    <E>120e3</E>
    <v>0.34</v>
  </elastic>
  <yield_criterion type="DC von Mises stress"/>
  <flow_curve type="PFC paper">
    <nf>15</nf>
    <Y0>60</Y0>
    <Ymax>288</Ymax>
    <w0>0.988</w0>
    <we>0</we>
    <r>1</r>
  </flow_curve>
</material>
```

_Example 4:_
Unaged maraging steel (mm-N-s units)
```
<material id="1" type="reactive plasticity">
  <isochoric>1</isochoric>
  <elastic type="neo-Hookean">
    <density>8.00e-9</density>
    <E>165e3</E>
    <v>0.33</v>
  </elastic>
  <yield_criterion type="DC von Mises stress"/>
  <flow_curve type="PFC paper">
    <nf>22</nf>
    <Y0>398</Y0>
    <Ymax>1010</Ymax>
    <w0>0</w0>
    <we>0</we>
    <r>0.9</r>
  </flow_curve>
</material>
```

_Example 5:_
Annealed aluminum 1100 (mm-N-s units)
```xml
<material id="1" type="reactive plasticity">
  <isochoric>1</isochoric>
  <elastic type="neo-Hookean">
    <density>2.71e-9</density>
    <E>68e3</E>
    <v>0.33</v>
  </elastic>
  <yield_criterion type="DC von Mises stress"/>
  <flow_curve type="PFC paper">
    <nf>18</nf>
    <Y0>63</Y0>
    <Ymax>112</Ymax>
    <w0>0.994</w0>
    <we>0</we>
    <r>0.6</r>
  </flow_curve>
</material>
```

_Example 6:_
Mild steel (mm-N-s units)
```
<material id="1" type="reactive plasticity">
  <isochoric>1</isochoric>
  <elastic type="natural neo-Hookean">
    <density>2.71e-9</density>
    <E>206e3</E>
    <v>0.30</v>
  </elastic>
  <yield_criterion type="DC von Mises stress"/>
  <flow_curve type="PFC math">
    <nf>15</nf>
    <emin>0.0008403</emin>
    <emax>1.3</emax>
    <plastic_response>545.46*(0.011024+eps)^0.2589</plastic_response>
  </flow_curve>
</material>
```

_Example 7:_
Steel (in-lbf-s units)
```xml
<material id="1" name="Steel" type="reactive plasticity">
  <density>1</density>
  <isochoric>1</isochoric>
  <elastic type="natural neo-Hookean">
    <E>29911000</E>
    <v>0.3</v>
  </elastic>
  <yield_criterion type="DC von Mises stress"/>
  <flow_curve type="PFC user">
  <plastic_response type="point">
    <interpolate>SMOOTH</interpolate>
    <points>
      <point> 0.002, 59822 </point>
      <point> 0.002841, 64450 </point>
      <point> 0.00469, 68500 </point>
      <point> 0.00953, 72000 </point>
      <point> 0.0193, 75000 </point>
    </points>
    </plastic_response>
  </flow_curve>
</material>
```

_Example 8:_
elastic-perfectly plastic response, using PFC math flow curve
```xml
<material id="1" name="Elastoplastic Math" type="reactive plasticity">
  <density>1</density>
  <isochoric>1</isochoric>
  <elastic type="neo-Hookean">
    <E>200000</E>
    <v>0.3</v>
  </elastic>
  <yield_criterion type="DC von Mises stress"/>
  <flow_curve type="PFC math">
    <nf>1</nf>
    <e0>0.001</e0>
    <emax>1</emax>
    <plastic_response type="math">200</plastic_response>
  </flow_curve>
</material>
```