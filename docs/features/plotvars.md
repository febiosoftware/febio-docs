# Plot Variables

The following plot variables are available in FEBio:

|variable | description|module|
|-------- | -----------|------|
|`acceleration` | Average element accelerations|solid|
|`Almansi strain` | Almansi strain tensor|solid|
|`beam curvature` | the curvature vector of a beam element|solid|
|`beam reference stress` | the stress vector in the reference frame of a beam element|solid|
|`beam reference stress couple` | the stress couple vector of a beam element in the reference frame|solid|
|`beam strain` | the strain vector of a beam element|solid|
|`beam stress` | the stress vector of a beam element|solid|
|`beam stress couple` | the stress couple vector of a beam element|solid|
|`body force` | the total body force vector applied to a solid element|solid|
|`concentration gap` | The concentration gap across a biphasic contact interface.|solute|
|`contact area` | Net contact area across contact interface. Evaluated by integrating the surface area at integration points where the contact pressure is not zero.|solid|
|`contact force` | Net contact force across contact interface. Evaluated by integrating the contact traction over the contact surface.|solid|
|`contact gap` | Contact gap distance, evaluated at contact surface faces|biphasic|
|`contact penalty` | Contact penalty value|solid|
|`contact pressure` | Contact pressure, evaluated at contact surface faces|solid|
|`contact status` | The nr. of integration points of the surface element that are considered in contact.|solid|
|`contact stick` | Stick status in stick-slip frictional contact (1=stick, 0=slip). Values between 0 and 1 imply that a fraction of that face is in stick mode. Currently works only with sliding-tension-compression.|solid|
|`contact traction` | Contact traction vectors, evaluated at contact surface faces|solid|
|`continuous damage` | the accumulated damage variable in a continuous-discontinuous damage model|solid|
|`continuous damage beta` | the $\beta$ parameter in a continuous-discontinuous damage model|solid|
|`continuous damage D1` | the D1 parameter in a continuous-discontinuous damage model|solid|
|`continuous damage D2` | the D2 parameter in a continuous-discontinuous damage model|solid|
|`continuous damage D2beta` | the D2beta parameter in a continuous-discontinuous damage model|solid|
|`continuous damage D3` | the D3 parameter in a continuous-discontinuous damage model|solid|
|`continuous damage Ds` | the Ds parameter in a continuous-discontinuous damage model|solid|
|`continuous damage gamma` | the $\gamma$ parameter in a continuous-discontinuous damage model|solid|
|`continuous damage P` | the P parameter in a continuous-discontinuous damage model|solid|
|`continuous damage Psi0` | the $\Psi_0$ parameter in a continuous-discontinuous damage model|solid|
|`current density` | Electric current density|solute|
|`current element angular momentum` | The element's total angular momentum at the current configuration.|solid|
|`current element center of mass` | The element's center of mass at the current configuration.|solid|
|`current element kinetic energy` | The element's total kinetic energy at the current configuration.|solid|
|`current element linear momentum` | The element's total linear momentum at the current configuration|solid|
|`current element strain energy` | The element's total strain energy at the current configuration.|solid|
|`damage` | Damage variable D|solid|
|`deformation gradient` | The deformation gradient $\mathbf{F}$|solid|
|`density` | The current density|solid|
|`Deshpande-Fleck stress` | Element yield stress based on Deshpande-Fleck criterion|solid|
|`deviatoric elasticity` | The deviatoric elasticity tensor of an uncoupled material|solid|
|`deviatoric fiber stretch` | Deviatoric fiber stretch $\tilde{\lambda }$ in a fiber material|solid|
|`deviatoric strain energy density` | Deviatoric strain energy density $\tilde{\Psi}\left(\mathbf{\tilde{C}}\right)$|solid|
|`deviatoric strong bond SED` | Strain energy density of strong bonds in reactive viscoelastic material|solid|
|`deviatoric weak bond SED` | Strain energy density of weak bonds in reactive viscoelastic material|solid|
|`dilatation gradient` | gradient of J in biphasic-FSI|fluid|
|`discrete element direction` | Unit vector along direction of discrete element|solid|
|`discrete element elongation` | Change in length of the discrete element (i.e. $\Delta L = L_t - L_0$)|solid|
|`discrete element force` | the vector force in the discrete element|solid|
|`discrete element length` | Current length of the discrete element|solid|
|`discrete element percent elongation` | ratio of change in length over original length|solid|
|`discrete element signed force` | The dot product of the force and the element's direction vector.|solid|
|`discrete element strain energy` | strain energy of the discrete element's material|solid|
|`discrete element stretch` | Current stretch of the discrete element (i.e. $\lambda = L_t / L_0$)|solid|
|`displacement` | Nodal displacements|fluid|
|`Drucker shear stress` | Element yield stress based on Drucker shear stress criterion|solid|
|`Drucker-Prager stress` | Element yield stress based on Drucker-Prager criterion|solid|
|`edge contact gap` | the contact gap of an edge-to-surface contact interface.|solid|
|`effective elasticity` | The elasticity of the elastic material in a biphasic/triphasic/multiphasic material.|biphasic|
|`effective fluid pressure` | Fluid pressure p for biphasic materials, or $\tilde{p}$ for biphasic-solute|fluid|
|`effective friction coefficient` | Effective friction coefficient at a biphasic contact interface|biphasic|
|`effective shell fluid pressure` | fluid pressure for biphasic, biphasic-solute, triphasic, and multiphasic materials of shell domains.|biphasic|
|`effective shell solute concentration` | Effective solute concentration for biphasic-solute, triphasic, and multiphasic materials of shell domains.|solute|
|`effective solute concentration` | Effective solute concentration $\tilde{c}$ for biphasic-solute materials|solute|
|`elastic fluid pressure` | Element elastic fluid pressure|fluid|
|`elasticity` | Spatial elasticity tensor components|solid|
|`electric potential` | Electric potential $\psi$ in triphasic/multiphasic materials|solute|
|`element angular momentum` | Element total angular momentum|solid|
|`element center of mass` | Element center of mass|solid|
|`element kinetic energy` | Element total kinetic energy|solid|
|`element linear momentum` | Element total linear momentum|solid|
|`element strain energy` | Element total strain energy|solid|
|`element stress power` | Element total stress power|solid|
|`enclosed volume` | Volume enclosed by named surface|solid|
|`enclosed volume change` | Change in volume enclosed by named surface|solid|
|`Euler angle` | Rigid body Euler angles|solid|
|`facet area` | The area of the surface element in the deformed configuration.|solid|
|`fatigue bond fraction` | fatigue bond fraction in a reactive-viscoelastic material|solid|
|`fiber stretch` | Element's average fiber stretch|solid|
|`fiber vector` | Material fiber vector|solid|
|`field` | Output the nodal values of a field variable.|core|
|`fixed charge density` | Fixed charge density $c^{F}$ in current configuration|solute|
|`fluid acceleration` | Fluid acceleration (material time derivative of fluid velocity $\mathbf{v}^{f}$|fluid|
|`fluid body force` | The element's average body force applied to the element.|fluid|
|`fluid bulk modulus` | The element's average bulk modulus, calculate from the pressure.|fluid|
|`fluid density` | Fluid density $\rho^{f}$ in fluid and fluid-FSI materials|fluid|
|`fluid density rate` | The element's average fluid density rate.|fluid|
|`fluid dilatation` | Fluid dilatation $e$|fluid|
|`fluid element angular momentum` | Total angular momentum of fluid element|fluid|
|`fluid element center of mass` | Center of mass of fluid element|fluid|
|`fluid element kinetic energy` | Total kinetic energy of fluid element|fluid|
|`fluid element linear momentum` | Total linear momentum of fluid element|fluid|
|`fluid element strain energy` | Total strain energy of fluid element|fluid|
|`fluid energy density` | Average energy density of fluid element|fluid|
|`fluid flow rate` | Volumetric fluid flow rate $Q=\int_{A}\mathbf{w}\cdot\mathbf{n}\,dA$ across a named surface (biphasic and multiphasic analyses)|fluid|
|`fluid flux` | Fluid flux $\mathbf{w}$ in biphasic, biphasic-solute, triphasic/multiphasic, fluid-FSI and biphasic-FSI materials.|fluid|
|`fluid force` | Net fluid force across biphasic (sliding-biphasic), biphasic-solute (sliding-biphasic-solute) and multiphasic (sliding-multiphasic) contact interface. Evaluated by integrating the fluid pressure p over the contact surface.|biphasic|
|`fluid force2` | Alternative calculation of the net fluid force|biphasic|
|`fluid heat supply density` | Average heat supply density of a fluid element|fluid|
|`fluid kinetic energy density` | Average kinetic energy densify of a fluid element|fluid|
|`fluid load support` | The total fluid load support across a named surface|biphasic|
|`fluid mass flow rate` | Mass flow rate across a named surface, $\dot{m}=\int_{A}\rho\mathbf{v}\cdot\mathbf{n}\,dA$|fluid|
|`fluid pressure` | Fluid pressure $p$ in biphasic, biphasic-solute, triphasic/multiphasic materials, and fluid materials|fluid|
|`fluid pressure tangent strain` | |fluid|
|`fluid rate of deformation` | Fluid rate of deformation tensor $\mathbf{D}$|fluid|
|`fluid relative Reynolds number` | |fluid|
|`fluid shear stress error` | |fluid|
|`fluid shear viscosity` | Average shear viscosity of a fluid element|fluid|
|`fluid specific entropy` | |fluid|
|`fluid specific free energy` | |fluid|
|`fluid specific free enthalpy` | |fluid|
|`fluid specific gauge enthalpy` | |fluid|
|`fluid specific internal energy` | |fluid|
|`fluid specific strain energy` | |fluid|
|`fluid strain energy density` | Average shear energy density of fluid element|fluid|
|`fluid stress` | Fluid stress $\boldsymbol{\sigma}$|fluid|
|`fluid stress power density` | Fluid stress power $\boldsymbol{\sigma}:\mathbf{D}$|fluid|
|`fluid surface energy flux` | The total energy flux across a named surface for a fluid analysis|fluid|
|`fluid surface force` | Net force exerted by a fluid on a named surface, $\mathbf{f}=-\int_{A}\mathbf{t}\,dA$|fluid|
|`fluid surface pressure` | Average fluid pressure on each face of a surface, evaluated from the nodal values of the fluid dilatation on that face|fluid|
|`fluid surface traction power` | Net traction power across a named surface of a fluid analysis|fluid|
|`fluid velocity` | Element fluid velocity $\mathbf{v}^{f}$ in fluid and fluid-FSI materials|fluid|
|`fluid volume ratio` | Fluid volume ratio $J$|fluid|
|`fluid volume ratio gradient` | Gradient of porosity in a biphasic-FSI material.|fluid|
|`fluid vorticity` | Fluid vorticity|fluid|
|`G norm` | |solid|
|`growth infinitesimal strain` | growth infinitesimal strain|solid|
|`growth Lagrange strain` | growth Lagrange strain|solid|
|`growth left Hencky` | growth left Hencky|solid|
|`growth left stretch` | growth left stretch|solid|
|`growth relative volume` | growth relative volume|solid|
|`growth right Hencky` | growth right Hencky|solid|
|`growth right stretch` | growth right stretch|solid|
|`ideal gas pressure` | current pressure value of the `ideal gas pressure` load|solid|
|`incremental displacement` | The displacement increment from the previously written plot state.|solid|
|`infinitesimal strain` | The average infinitesimal strain tensor in an element|solid|
|`in-situ target stretch` | the fiber stretch induced by the initial prestrain gradient|solid|
|`intact bond fraction` | fraction of intact bonds in a reactive-viscoelastic material|solid|
|`kinetic energy density` | The average kinetic energy density in an element|solid|
|`Lagrange strain` | The average Lagrange strain in an element|solid|
|`left Cauchy-Green` | The left Cauchy-Green deformation tensor $\mathbf{b}=\mathbf{F} \mathbf{F}^T$|solid|
|`left Hencky` | Left Hencky strain $\mathbf{h}=\frac{1}{2}\ln\mathbf{b}$, where $\mathbf{b}=\mathbf{F}\cdot\mathbf{F}^{T}$|solid|
|`left stretch` | Left stretch tensor $\mathbf{V}=\mathbf{b}^{1/2}$|solid|
|`local fluid load support` | Local fluid load support on biphasic contact surfaces|biphasic|
|`material axes` | "The material axes of an element stored as a $3 \times 3$ tensor. The columns of the tensor represent the local x-|solid|
|`mean-ratio` | |core|
|`mesh_data` | Stores the value of a mesh_data field to the plotfile. The output class depends on the mesh_data field.|core|
|`micro energy` | the integrated strain energy of a micro material|solid|
|`mixture deviatoric strain energy density` | Deviatoric strain energy density in mixture components|solid|
|`mixture specific strain energy` | Specific strain energy in mixture components|solid|
|`mixture strain energy density` | Strain energy density in mixture components|solid|
|`mixture stress` | the cauchy stress in a component of a solid mixture.|solid|
|`mortar-gap` | |solid|
|`nodal acceleration` | The acceleration at the nodes|solid|
|`nodal contact gap` | Contact gap distance, evaluated at contact surface nodes|solid|
|`nodal contact pressure` | Contact pressure, evaluated at contact surface nodes|solid|
|`nodal contact traction` | Contact traction vectors, evaluated at contact surface nodes|solid|
|`nodal fluid flux` | Fluid flux in biphasic, biphasic-solute, triphasic, multiphasic, fluid-FSI and biphasic-FSI materials|fluid|
|`nodal fluid velocity` | Fluid velocity $\mathbf{v}^{f}$ in fluid and fluid-FSI materials|fluid|
|`nodal shell director` | The director of a shell node.|solid|
|`nodal strain` | the Green-Lagrange strain tensor projected to the nodes.|solid|
|`nodal stress` | The Cauchy stress, projected to the nodes.|solid|
|`nodal surface traction` | Contact nodal tractions|solid|
|`nodal vector gap` | Contact gap vector at surface nodes|solid|
|`nodal velocity` | The nodal velocities|solid|
|`octahedral plastic strain` | octahedral plastic strain|solid|
|`osmolarity` | Element's average osmolarity in biphasic/triphasic/multiphasic analysis|solute|
|`osmotic coefficient` | the element-averaged osmotic coefficient in a multiphasic material|multiphasic|
|`parameter` | Stores heterogeneous material parameter data|core|
|`partition coefficient` | the element-averaged solute partition coefficient in a multiphasic material|solute|
|`permeability` | the element-averaged permeability in a biphasic-FSI material|fluid|
|`pid controller` | the output value of a PID controller|core|
|`PK1 norm` | The norm of the PK1 stress of a micro material|solid|
|`PK1 stress` | The PK1 stress of the element.|solid|
|`PK2 stress` | The PK2 stress of the element.|solid|
|`plastic yield stress` | The current yield stress in a plastic material|solid|
|`plasticity heat supply density` | Reactive plasticity heat supply|solid|
|`porosity` | the element-averaged porosity in a biphasic or multiphasic material|fluid|
|`pressure gap` | Pressure gap between opposing surfaces in a biphasic contact analysis|biphasic|
|`prestrain compatibility` | the prestrain compatibility tensor of an elastic-prestrain material|solid|
|`prestrain correction` | the 3x3 prestrain correction tensor|solid|
|`prestrain stretch` | the stretch induced by the effective prestrain gradient|solid|
|`prestrain stretch error` | the error in the prestrain stretch of an elastic-prestrain material|solid|
|`QK1 norm` | |solid|
|`rate of deformation` | The average rate of deformation tensor (i.e. symmetric part of velocity gradient) in an element|solid|
|`reaction forces` | The nodal reaction forces.|solid|
|`receptor-ligand concentration` | Receptor-ligand concentration in a biphasic-solute analysis.|multiphasic|
|`referential fixed charge density` | Referential fixed charge density $c_{r}^{F}$, which may evolve with chemical reactions|solute|
|`referential solid volume fraction` | the referential solid volume fraction in a multiphasic material|biphasic|
|`relative fluid velocity` | Average element fluid velocity relative to mesh $\mathbf{w}$ in fluid and fluid-FSI materials|fluid|
|`relative volume` | Relative volume $J=\det\mathbf{F}$|solid|
|`right Cauchy-Green` | The right Cauchy-Green deformation tensor $\mathbf{C}=\mathbf{F}^T \mathbf{F}$|solid|
|`right Hencky` | Right Hencky strain $\mathbf{H}=\frac{1}{2}\ln\mathbf{C}$|solid|
|`right stretch` | Right stretch tensor $\mathbf{U}=\mathbf{C}^{1/2}$|solid|
|`rigid acceleration` | Rigid body center of mass acceleration|solid|
|`rigid angular acceleration` | Rigid body angular acceleration|solid|
|`rigid angular momentum` | Rigid body angular momentum|solid|
|`rigid angular position` | Rigid body rotation pseudo-vector|solid|
|`rigid angular velocity` | Rigid body angular velocity|solid|
|`rigid force` | Total force applied to the rigid body|solid|
|`rigid kinetic energy` | Rigid body kinetic energy|solid|
|`rigid linear momentum` | Rigid body linear momentum|solid|
|`rigid position` | Rigid body center of mass position|solid|
|`rigid rotation vector` | Rigid body rotation pseudo-vector|solid|
|`rigid torque` | Rigid body moment|solid|
|`rigid velocity` | Rigid body center of mass velocity|solid|
|`rotation` | the values of the nodal rotation degrees of freedom stored as a vector|solid|
|`RVE generations` | Number of generations in reactive viscoelastic material|solid|
|`RVE recruitment` | weak bond recruitment ratio in reactive viscoelastic material point|solid|
|`RVE reforming bonds` | Fraction of weak bonds available to break and reform in reactive viscoelastic material|solid|
|`RVE strain` | Strain measure used in strain-dependent reactive viscoelastic relaxation and weak bond recruitment|solid|
|`s norm` | The norm of the Cauchy stress|solid|
|`sbm areal concentration` | SBM areal concentration (mole per shell area) of a shell element|multiphasic|
|`sbm concentration` | concentration of a solid-bound molecule in an element|multiphasic|
|`sbm referential apparent density` | Average element solid-bound molecule referential apparent density|multiphasic|
|`scalar surface load` | surface element averaged load. (assumes the surface has a load applied)|solid|
|`scaled-Jacobian` | |core|
|`shell bottom nodal strain` | Shell Lagrange strain extrapolated to bottom nodes|solid|
|`shell bottom nodal stress` | Shell Cauchy stress extrapolated to bottom nodes|solid|
|`shell bottom strain` | Average of shell Lagrange strain extrapolated to bottom surface|solid|
|`shell bottom stress` | Average of shell Cauchy stress extrapolated to bottom surface|solid|
|`shell director` | The shell director|solid|
|`shell displacement` | Nodal displacements of the back-nodes of shell elements|solid|
|`shell relative volume` | Relative volume of shell element|solid|
|`shell strain` | Average strain in shell element|solid|
|`shell thickness` | Shell thickness|solid|
|`shell top nodal strain` | Shell Lagrange strain extrapolated to top nodes|solid|
|`shell top nodal stress` | Shell Cauchy stress extrapolated to top nodes|solid|
|`shell top strain` | Average of shell Lagrange strain extrapolated to top surface|solid|
|`shell top stress` | Average of shell Cauchy stress extrapolated to top surface|solid|
|`solid stress` | Cauchy stress in the solid phase of an FSI material|fluid|
|`solid volume fraction` | the element-averaged solid volume fraction in a biphasic-FSI material|fluid|
|`solute concentration` | Solute concentration $c$ in biphasic-solute materials, or $c^{\alpha}$ in triphasic/multiphasic materials|solute|
|`solute flux` | Solute flux $\mathbf{j}$ in biphasic-solute materials or $\mathbf{j}^{\alpha}$ in triphasic/multiphasic materials.|solute|
|`solute relative Peclet number` | Element relative Peclet number|fluid-solutes|
|`solute volumetric flux` | Volumetric flux of solute in triphasic/multiphasic materials|solute|
|`specific strain energy` | Average element specific strain energy|biphasic|
|`SPR infinitesimal strain` | The infinitesimal strain tensor recovered using SPR|solid|
|`SPR Lagrange strain` | The Lagrange strain recovered using SPR|solid|
|`SPR prestrain correction` | The 3x3 prestrain correction tensor (recovered with SPR)|solid|
|`SPR principal stress` | Principal stress values obtained via SPR projection|solid|
|`SPR relative volume` | The relative volume (i.e. det F) recovered using the SPR method|solid|
|`SPR stress` | Cauchy stress obtained via SPR projection|solid|
|`SPR-P1 stress` | Cauchy stress obtained via SPR projection (first-order projection)|solid|
|`strain energy density` | Strain energy density $\Psi\left(\mathbf{C}\right)$|solid|
|`stress` | Cauchy stress|solid|
|`stress error` | the effective stress|solid|
|`strong bond SED` | Strain energy density of strong bonds in reactive viscoelastic material|solid|
|`surface area` | The area of a surface in the current configuration.|solid|
|`surface reaction force` | Total reaction force on a surface|solid|
|`surface reaction moment` | Total reaction moment on a surface|solid|
|`surface traction` | Nodal surface tractions of nodes on a contact surface|solid|
|`tet-quality` | |core|
|`total angular momentum` | Total angular momentum of a rigid body domain|solid|
|`total energy` | total energy (= strain energy + kinetic energy) of a solid domain.|solid|
|`total linear momentum` | Total linear momentum of a rigid body domain|solid|
|`truss stretch` | Current stretch of the truss element (i.e. $\lambda = L_t / L_0$)|solid|
|`uncoupled pressure` | The pressure of an uncoupled material|solid|
|`ut4 nodal stress` | Stresses at the nodes of the UT4 element|solid|
|`vector gap` | The vector gap at nodes of a contact surface|solid|
|`velocity` | Nodal velocities (fluid nodal velocities in fluid analyses)|solid|
|`volume fraction` | Average element volume fraction of a solid mixture|solid|
|`weak bond SED` | Strain energy density of weak bonds in reactive viscoelastic material|solid|
|`yielded bond fraction` | The fraction of bonds that have yielded in a reactive viscoelastic material|solid|
