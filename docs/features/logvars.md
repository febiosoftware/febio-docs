# Log Variables

The following log variables are available in FEBio:

|variable | description|module|
|-------- | -----------|------|
|`_math` | |core|
|`alx` | x-component of angular acceleration|solid|
|`aly` | y-component of angular acceleration|solid|
|`alz` | z-component of angular acceleration|solid|
|`avg` | Average of another log variable over domain|core|
|`ax` | x-component of center of mass acceleration|solid|
|`ay` | y-component of center of mass acceleration|solid|
|`az` | z-component of center of mass acceleration|solid|
|`c` | the element-averaged actual concentration of solute in a biphasic-solute material.|solute|
|`c1` | the element-averaged actual concentration of solute with index 1 in a multiphasic material.|solute|
|`c1_integral` | the integral of the actual solute 1 concentration over the domain.|multiphasic|
|`c2` | the element-averaged actual concentration of solute with index 2 in a multiphasic material.|solute|
|`c2_integral` | the integral of the actual solute 2 concentration over the domain.|multiphasic|
|`c3` | the element-averaged actual concentration of solute with index 3 in a multiphasic material.|solute|
|`c3_integral` | the integral of the actual solute 3 concentration over the domain.|multiphasic|
|`c4` | the element-averaged actual concentration of solute with index 4 in a multiphasic material.|solute|
|`c4_integral` | the integral of the actual solute 4 concentration over the domain.|multiphasic|
|`c5` | the element-averaged actual concentration of solute with index 5 in a multiphasic material.|solute|
|`c5_integral` | the integral of the actual solute 5 concentration over the domain.|multiphasic|
|`c6` | the element-averaged actual concentration of solute with index 6 in a multiphasic material.|solute|
|`c6_integral` | the integral of the actual solute 6 concentration over the domain.|multiphasic|
|`c7` | the element-averaged actual concentration of solute with index 7 in a multiphasic material.|solute|
|`c7_integral` | the integral of the actual solute 7 concentration over the domain.|multiphasic|
|`c8` | the element-averaged actual concentration of solute with index 8 in a multiphasic material.|solute|
|`c8_integral` | the integral of the actual solute 8 concentration over the domain.|multiphasic|
|`ce1` | effective concentration of solute with index 1 in current configuration|solute|
|`ce2` | effective concentration of solute with index 2 in current configuration|solute|
|`ce3` | effective concentration of solute with index 3 in current configuration|solute|
|`ce4` | effective concentration of solute with index 4 in current configuration|solute|
|`ce5` | effective concentration of solute with index 5 in current configuration|solute|
|`ce6` | effective concentration of solute with index 6 in current configuration|solute|
|`ce7` | effective concentration of solute with index 7 in current configuration|solute|
|`ce8` | effective concentration of solute with index 8 in current configuration|solute|
|`cF` | fixed charge density in current configuration|solute|
|`constrained volume` | The volume inside the constrained volume of a `volume` constraint.|solid|
|`contact area` | The total contact area of the contact interface this surface belongs to.|solid|
|`contact gap` | The gap (separation) of the contact interface this surface belongs to|solid|
|`contact pressure` | The normal contact pressure of the contact interface this surface belongs to|solid|
|`contact_traction.x` | The x-component of the contact traction on the face|solid|
|`contact_traction.y` | The y-component of the contact traction on the face|solid|
|`contact_traction.z` | The z-component of the contact traction on the face|solid|
|`crc` | referential mass-concentration of solute in a biphasic-solute material.|solute|
|`cxxxx` | xxxx component of spatial elasticity tensor (a.k.a. c11)|solid|
|`cxxxy` | xxxy component of spatial elasticity tensor (a.k.a. c14)|solid|
|`cxxxz` | xxxz component of spatial elasticity tensor (a.k.a. c16)|solid|
|`cxxyy` | xxyy component of spatial elasticity tensor (a.k.a. c12)|solid|
|`cxxyz` | xxyz component of spatial elasticity tensor (a.k.a. c15)|solid|
|`cxxzz` | xxzz component of spatial elasticity tensor (a.k.a. c13)|solid|
|`cxyxy` | xyxy component of spatial elasticity tensor (a.k.a. c44)|solid|
|`cxyxz` | xyxz component of spatial elasticity tensor (a.k.a. c46)|solid|
|`cxyyz` | xyyz component of spatial elasticity tensor (a.k.a. c45)|solid|
|`cxzxz` | xzxz component of spatial elasticity tensor (a.k.a. c66)|solid|
|`cyyxy` | yyxy component of spatial elasticity tensor (a.k.a. c24)|solid|
|`cyyxz` | yyxz component of spatial elasticity tensor (a.k.a. c26)|solid|
|`cyyyy` | yyyy component of spatial elasticity tensor (a.k.a. c22)|solid|
|`cyyyz` | yyyz component of spatial elasticity tensor (a.k.a. c25)|solid|
|`cyyzz` | yyzz component of spatial elasticity tensor (a.k.a. c23)|solid|
|`cyzxz` | yzxz component of spatial elasticity tensor (a.k.a. c56)|solid|
|`cyzyz` | yzyz component of spatial elasticity tensor (a.k.a. c55)|solid|
|`czzxy` | zzxy component of spatial elasticity tensor (a.k.a. c34)|solid|
|`czzxz` | zzxz component of spatial elasticity tensor (a.k.a. c36)|solid|
|`czzyz` | zzyz component of spatial elasticity tensor (a.k.a. c35)|solid|
|`czzzz` | zzzz component of spatial elasticity tensor (a.k.a. c33)|solid|
|`D` | damage variable (or sum of damage variables in solid mixtures)|solid|
|`damage_1` | the damage (or fraction of broken bonds) of solid component 1 in a solid mixture material.|solid|
|`damage_2` | the damage (or fraction of broken bonds) of solid component 2 in a solid mixture material.|solid|
|`damage_3` | the damage (or fraction of broken bonds) of solid component 3 in a solid mixture material.|solid|
|`damage_4` | the damage (or fraction of broken bonds) of solid component 4 in a solid mixture material.|solid|
|`damage_5` | the damage (or fraction of broken bonds) of solid component 5 in a solid mixture material.|solid|
|`damage_6` | the damage (or fraction of broken bonds) of solid component 6 in a solid mixture material.|solid|
|`damage_7` | the damage (or fraction of broken bonds) of solid component 7 in a solid mixture material.|solid|
|`damage_8` | the damage (or fraction of broken bonds) of solid component 8 in a solid mixture material.|solid|
|`devsed` | deviatoric strain energy density|solid|
|`discrete element elongation` | The discrete element's elongation (i.e. current length minus initial length)|solid|
|`discrete element force` | The scalar force along the element's axis.|solid|
|`discrete element stretch` | The discrete element's stretch (i.e. ratio of current length over initial length)|solid|
|`E1` | first eigenvalue of Green-Lagrange strain tensor|solid|
|`E2` | second eigenvalue of Green-Lagrange strain tensor|solid|
|`E3` | third eigenvalue of Green-Lagrange strain tensor|solid|
|`effective left Hencky` | The effective (or von-Mises) norm of the left Hencky tensor|solid|
|`effective left stretch` | The effective (or von-Mises) norm of the left stretch tensor|solid|
|`effective right Hencky` | The effective (or von-Mises) norm of the right Hencky tensor|solid|
|`effective right stretch` | The effective (or von-Mises) norm of the right stretch tensor|solid|
|`effective strain` | the effective (or von-Mises) norm of the Green-Lagrange strain tensor.|solid|
|`effective stress` | the effective (or von-Mises) norm of the Cauchy stress tensor|solid|
|`esxx` | The xx component of the solid stress of a biphasic material|biphasic|
|`esxy` | The xy component of the solid stress of a biphasic material|biphasic|
|`esxz` | The xz component of the solid stress of a biphasic material|biphasic|
|`esyy` | The yy component of the solid stress of a biphasic material|biphasic|
|`esyz` | The yz component of the solid stress of a biphasic material|biphasic|
|`eszz` | The zz component of the solid stress of a biphasic material|biphasic|
|`EulerX` | X-Euler angle|solid|
|`EulerY` | Y-Euler angle|solid|
|`EulerZ` | Z-Euler angle|solid|
|`ex` | xx-component of the infinitesimal strain|solid|
|`Ex` | xx-component of the Green-Lagrange strain|solid|
|`exy` | xy-component of the infinitesimal strain|solid|
|`Exy` | xy-component of the Green-Lagrange strain|solid|
|`exz` | xz-component of the infinitesimal strain|solid|
|`Exz` | xz-component of the Green-Lagrange strain|solid|
|`ey` | yy-component of the infinitesimal strain|solid|
|`Ey` | yy-component of the Green-Lagrange strain|solid|
|`eyz` | yz-component of the infinitesimal strain|solid|
|`Eyz` | yz-component of the Green-Lagrange strain|solid|
|`ez` | zz-component of the infinitesimal strain|solid|
|`Ez` | zz-component of the Green-Lagrange strain|solid|
|`facet area` | The area of the surface facet in the current configuration|core|
|`fax` | x-component of fluid acceleration|fluid|
|`fay` | y-component of fluid acceleration|fluid|
|`faz` | z-component of fluid acceleration|fluid|
|`fd` | fluid density|fluid|
|`Fde.x` | The x-component of the discrete element's force vector.|solid|
|`Fde.y` | The y-component of the discrete element's force vector.|solid|
|`Fde.z` | The z-component of the discrete element's force vector.|solid|
|`fdxx` | xx-component of fluid rate of deformation|fluid|
|`fdxy` | xy-component of fluid rate of deformation|fluid|
|`fdxz` | xz-component of fluid rate of deformation|fluid|
|`fdyy` | yy-component of fluid rate of deformation|fluid|
|`fdyz` | yz-component of fluid rate of deformation|fluid|
|`fdzz` | zz-component of fluid rate of deformation|fluid|
|`FHAsx` | x-component of the finite helical axis|solid|
|`FHAsy` | y-component of the finite helical axis|solid|
|`FHAsz` | z-component of the finite helical axis|solid|
|`FHAtd` | |solid|
|`FHAwm` | |solid|
|`FHAwx` | x-component of angular rotation vector around finite helical axis|solid|
|`FHAwy` | y-component of angular rotation vector around finite helical axis|solid|
|`FHAwz` | z-component of angular rotation vector around finite helical axis|solid|
|`fiber_stretch` | The element's fiber stretch, averaged over integration points.|solid|
|`fiber_x` | The x-component of the element's fiber vector|solid|
|`fiber_y` | The y-component of the element's fiber vector|solid|
|`fiber_z` | The z-component of the element's fiber vector|solid|
|`fJ` | fluid volume ratio|fluid|
|`fmxs` | maximum shear of fluid Cauchy stress|fluid|
|`fp` | fluid pressure|fluid|
|`fs1` | 1st principal fluid Cauchy stress|fluid|
|`fs2` | 2nd principal fluid Cauchy stress|fluid|
|`fs3` | 3rd principal fluid Cauchy stress|fluid|
|`fsp` | fluid stress power|fluid|
|`fsxx` | xx-component of fluid Cauchy stress|fluid|
|`fsxy` | xy-component of fluid Cauchy stress|fluid|
|`fsxz` | xz-component of fluid Cauchy stress|fluid|
|`fsyy` | yy-component of fluid Cauchy stress|fluid|
|`fsyz` | yz-component of fluid Cauchy stress|fluid|
|`fszz` | zz-component of fluid Cauchy stress|fluid|
|`Ft_xx` | The xx component of the total deformation gradient of a prestrain material|solid|
|`Ft_xy` | The xy component of the total deformation gradient of a prestrain material|solid|
|`Ft_xz` | The xz component of the total deformation gradient of a prestrain material|solid|
|`Ft_yx` | The yx component of the total deformation gradient of a prestrain material|solid|
|`Ft_yy` | The yy component of the total deformation gradient of a prestrain material|solid|
|`Ft_yz` | The yz component of the total deformation gradient of a prestrain material|solid|
|`Ft_zx` | The zx component of the total deformation gradient of a prestrain material|solid|
|`Ft_zy` | The zy component of the total deformation gradient of a prestrain material|solid|
|`Ft_zz` | The zz component of the total deformation gradient of a prestrain material|solid|
|`fvx` | x-component of fluid velocity|fluid|
|`fvy` | y-component of fluid velocity|fluid|
|`fvz` | z-component of fluid velocity|fluid|
|`fwx` | x-component of fluid vorticity|fluid|
|`fwy` | y-component of fluid vorticity|fluid|
|`fwz` | z-component of fluid vorticity|fluid|
|`fx` | x-coordinate of element centroid position|fluid|
|`Fx` | x-component of the rigid body reaction force|solid|
|`Fxx` | xx-component of the deformation gradient|solid|
|`Fxy` | xy-component of the deformation gradient|solid|
|`Fxz` | xz-component of the deformation gradient|solid|
|`fy` | y-coordinate of element centroid position|fluid|
|`Fy` | y-component of the rigid body reaction force|solid|
|`Fyx` | yx-component of the deformation gradient|solid|
|`Fyy` | yy-component of the deformation gradient|solid|
|`Fyz` | yz-component of the deformation gradient|solid|
|`fz` | z--coordinate of element centroid position|fluid|
|`Fz` | z-component of the rigid body reaction force|solid|
|`Fzx` | xz-component of the deformation gradient|solid|
|`Fzy` | zy-component of the deformation gradient|solid|
|`Fzz` | zz-component of the deformation gradient|solid|
|`h1` | first eigenvalue of left Hencky strain|solid|
|`H1` | first eigenvalue of right Hencky strain|solid|
|`h2` | second eigenvalue of left Hencky strain|solid|
|`H2` | second eigenvalue of right Hencky strain|solid|
|`h3` | third eigenvalue of left Hencky strain|solid|
|`H3` | third eigenvalue of right Hencky strain|solid|
|`hx` | xx-component of the left Hencky strain|solid|
|`Hx` | xx-component of the right Hencky strain|solid|
|`hxy` | xy-component of the left Hencky strain|solid|
|`Hxy` | xy-component of the right Hencky strain|solid|
|`hxz` | xz-component of the left Hencky strain|solid|
|`Hxz` | xz-component of the right Hencky strain|solid|
|`hy` | yy-component of the left Hencky strain|solid|
|`Hy` | yy-component of the right Hencky strain|solid|
|`hyz` | yz-component of the rileft Hencky strain|solid|
|`Hyz` | yz-component of the right Hencky strain|solid|
|`hz` | zz-component of the left Hencky strain|solid|
|`Hz` | zz-component of the right Hencky strain|solid|
|`Iex` | The x-component of the element current density in a multiphasic material|multiphasic|
|`Iey` | The y-component of the element current density in a multiphasic material|multiphasic|
|`Iez` | The z-component of the element current density in a multiphasic material|multiphasic|
|`IHAsx` | x-component of the instantaneous helical axis|solid|
|`IHAsy` | y-component of the instantaneous helical axis|solid|
|`IHAsz` | z-component of the instantaneous helical axis|solid|
|`IHAtd` | |solid|
|`IHAwm` | |solid|
|`IHAwx` | x-component of angular rotation vector around instantaneous helical axis|solid|
|`IHAwy` | y-component of angular rotation vector around instantaneous helical axis|solid|
|`IHAwz` | z-component of angular rotation vector around instantaneous helical axis|solid|
|`integrate` | |core|
|`J` | relative volume (determinant of deformation gradient)|solid|
|`j1x` | The x-component of the flux of solute with index 1 in a multiphasic material|solute|
|`j1y` | The y-component of the flux of solute with index 1 in a multiphasic material|solute|
|`j1z` | The z-component of the flux of solute with index 1 in a multiphasic material|solute|
|`j2x` | The x-component of the flux of solute with index 2 in a multiphasic material|solute|
|`j2y` | The y-component of the flux of solute with index 2 in a multiphasic material|solute|
|`j2z` | The z-component of the flux of solute with index 2 in a multiphasic material|solute|
|`j3x` | The x-component of the flux of solute with index 3 in a multiphasic material|solute|
|`j3y` | The y-component of the flux of solute with index 3 in a multiphasic material|solute|
|`j3z` | The z-component of the flux of solute with index 3 in a multiphasic material|solute|
|`j4x` | The x-component of the flux of solute with index 4 in a multiphasic material|solute|
|`j4y` | The y-component of the flux of solute with index 4 in a multiphasic material|solute|
|`j4z` | The z-component of the flux of solute with index 4 in a multiphasic material|solute|
|`j5x` | The x-component of the flux of solute with index 5 in a multiphasic material|solute|
|`j5y` | The y-component of the flux of solute with index 5 in a multiphasic material|solute|
|`j5z` | The z-component of the flux of solute with index 5 in a multiphasic material|solute|
|`j6x` | The x-component of the flux of solute with index 6 in a multiphasic material|solute|
|`j6y` | The y-component of the flux of solute with index 6 in a multiphasic material|solute|
|`j6z` | The z-component of the flux of solute with index 6 in a multiphasic material|solute|
|`j7x` | The x-component of the flux of solute with index 7 in a multiphasic material|solute|
|`j7y` | The y-component of the flux of solute with index 7 in a multiphasic material|solute|
|`j7z` | The z-component of the flux of solute with index 7 in a multiphasic material|solute|
|`j8x` | The x-component of the flux of solute with index 8 in a multiphasic material|solute|
|`j8y` | The y-component of the flux of solute with index 8 in a multiphasic material|solute|
|`j8z` | The z-component of the flux of solute with index 8 in a multiphasic material|solute|
|`jx` | x-component of flux of solute in biphasic-solute material|solute|
|`jy` | y-component of flux of solute in biphasic-solute material|solute|
|`jz` | z-component of flux of solute in biphasic-solute material|solute|
|`KE` | kinetic energy|solid|
|`Kpxx` | xx-component of the permeability tensor.|biphasic|
|`Kpxy` | xy-component of the permeability tensor.|biphasic|
|`Kpxz` | xz-component of the permeability tensor.|biphasic|
|`Kpyy` | yy-component of the permeability tensor.|biphasic|
|`Kpyz` | yz-component of the permeability tensor.|biphasic|
|`Kpzz` | zz-component of the permeability tensor.|biphasic|
|`max contact gap` | The maximum contact gap value evaluated over the entire surface.|solid|
|`max shear strain` | |solid|
|`mixture_stress[0].xx` | The xx component of the mixture stress tensor for solid component 0 in a solid mixture material.|solid|
|`mixture_stress[0].xy` | The xy component of the mixture stress tensor for solid component 0 in a solid mixture material.|solid|
|`mixture_stress[0].xz` | The xz component of the mixture stress tensor for solid component 0 in a solid mixture material.|solid|
|`mixture_stress[0].yy` | The yy component of the mixture stress tensor for solid component 0 in a solid mixture material.|solid|
|`mixture_stress[0].yz` | The yz component of the mixture stress tensor for solid component 0 in a solid mixture material.|solid|
|`mixture_stress[0].zz` | The zz component of the mixture stress tensor for solid component 0 in a solid mixture material.|solid|
|`mixture_stress[1].xx` | The xx component of the mixture stress tensor for solid component 1 in a solid mixture material.|solid|
|`mixture_stress[1].xy` | The xy component of the mixture stress tensor for solid component 1 in a solid mixture material.|solid|
|`mixture_stress[1].xz` | The xz component of the mixture stress tensor for solid component 1 in a solid mixture material.|solid|
|`mixture_stress[1].yy` | The yy component of the mixture stress tensor for solid component 1 in a solid mixture material.|solid|
|`mixture_stress[1].yz` | The yz component of the mixture stress tensor for solid component 1 in a solid mixture material.|solid|
|`mixture_stress[1].zz` | The zz component of the mixture stress tensor for solid component 1 in a solid mixture material.|solid|
|`mixture_stress[2].xx` | The xx component of the mixture stress tensor for solid component 2 in a solid mixture material.|solid|
|`mixture_stress[2].xy` | The xy component of the mixture stress tensor for solid component 2 in a solid mixture material.|solid|
|`mixture_stress[2].xz` | The xz component of the mixture stress tensor for solid component 2 in a solid mixture material.|solid|
|`mixture_stress[2].yy` | The yy component of the mixture stress tensor for solid component 2 in a solid mixture material.|solid|
|`mixture_stress[2].yz` | The yz component of the mixture stress tensor for solid component 2 in a solid mixture material.|solid|
|`mixture_stress[2].zz` | The zz component of the mixture stress tensor for solid component 2 in a solid mixture material.|solid|
|`Mx` | x-component of the rigid body reaction torque|solid|
|`My` | y-component of the rigid body reaction torque|solid|
|`Mz` | z-component of the rigid body reaction torque|solid|
|`nfvx` | x-component of fluid velocity|fluid|
|`nfvy` | y-component of fluid velocity|fluid|
|`nfvz` | z-component of fluid velocity|fluid|
|`normalized internal energy` | The integral over space and time of the internal energy normalized by the volume of the domain|solid|
|`omx` | x-component of angular velocity|solid|
|`omy` | y-component of angular velocity|solid|
|`omz` | z-component of angular velocity|solid|
|`ops` | the octahedral plastic strain|solid|
|`p` | actual fluid pressure|biphasic|
|`pct` | Percentile of another log variable over domain|core|
|`pe` | effective nodal fluid pressure.|solute|
|`porosity` | the porosity calculated from $1-\phi_r/J$ where $\phi_r$ is the referential solid volume fraction.|biphasic|
|`psi` | the element-averaged electric potential of an element in a multiphasic material.|multiphasic|
|`Pxx` | The xx component of the PK1 stress|solid|
|`Pxy` | The xy component of the PK1 stress|solid|
|`Pxz` | The xz component of the PK1 stress|solid|
|`Pyx` | The yx component of the PK1 stress|solid|
|`Pyy` | The yy component of the PK1 stress|solid|
|`Pyz` | The yz component of the PK1 stress|solid|
|`Pzx` | The zx component of the PK1 stress|solid|
|`Pzy` | The zy component of the PK1 stress|solid|
|`Pzz` | The zz component of the PK1 stress|solid|
|`qw` | w-component of rotation quaternion|solid|
|`qx` | x-component of rotation quaternion|solid|
|`qy` | y-component of rotation quaternion|solid|
|`qz` | z-component of rotation quaternion|solid|
|`R11` | 11-component of the rigid body's rotation matrix|solid|
|`R12` | 12-component of the rigid body's rotation matrix|solid|
|`R13` | 13-component of the rigid body's rotation matrix|solid|
|`R21` | 21-component of the rigid body's rotation matrix|solid|
|`R22` | 22-component of the rigid body's rotation matrix|solid|
|`R23` | 23-component of the rigid body's rotation matrix|solid|
|`R31` | 31-component of the rigid body's rotation matrix|solid|
|`R32` | 32-component of the rigid body's rotation matrix|solid|
|`R33` | 33-component of the rigid body's rotation matrix|solid|
|`rcFHAsx` | |solid|
|`rcFHAsy` | |solid|
|`rcFHAsz` | |solid|
|`rcFHAtd` | |solid|
|`rcFHAwm` | |solid|
|`rcFHAwx` | |solid|
|`rcFHAwy` | |solid|
|`rcFHAwz` | |solid|
|`RCFx` | x-component of rigid connector force|solid|
|`RCFy` | y-component of rigid connector force|solid|
|`RCFz` | z-component of rigid connector force|solid|
|`rcIHAsx` | |solid|
|`rcIHAsy` | |solid|
|`rcIHAsz` | |solid|
|`rcIHAtd` | |solid|
|`rcIHAwm` | |solid|
|`rcIHAwx` | |solid|
|`rcIHAwy` | |solid|
|`rcIHAwz` | |solid|
|`RCMx` | x-component of rigid connector moment|solid|
|`RCMy` | y-component of rigid connector moment|solid|
|`RCMz` | z-component of rigid connector moment|solid|
|`RCthx` | x-component of rigid connector rotation|solid|
|`RCthy` | y-component of rigid connector rotation|solid|
|`RCthz` | z-component of rigid connector rotation|solid|
|`RCx` | x-component of rigid connector translation|solid|
|`RCy` | y-component of rigid connector translation|solid|
|`RCz` | z-component of rigid connector translation|solid|
|`Rx` | x-coordinate of nodal reaction force|solid|
|`Ry` | y-coordinate of nodal reaction force|solid|
|`Rz` | z-coordinate of nodal reaction force|solid|
|`s1` | first eigenvalue of Cauchy stress tensor|solid|
|`s1x` | The x-component of the 1st Eigen vector of the Cauchy stress|solid|
|`s1y` | The y-component of the 1st Eigen vector of the Cauchy stress|solid|
|`s1z` | The z-component of the 1st Eigen vector of the Cauchy stress|solid|
|`s2` | second eigenvalue of Cauchy stress tensor|solid|
|`s2x` | The x-component of the 2nd Eigen vector of the Cauchy stress|solid|
|`s2y` | The y-component of the 2nd Eigen vector of the Cauchy stress|solid|
|`s2z` | The z-component of the 2nd Eigen vector of the Cauchy stress|solid|
|`s3` | third eigenvalue of Cauchy stress tensor|solid|
|`s3x` | The x-component of the 3rd Eigen vector of the Cauchy stress|solid|
|`s3y` | The y-component of the 3rd Eigen vector of the Cauchy stress|solid|
|`s3z` | The z-component of the 3rd Eigen vector of the Cauchy stress|solid|
|`sbm1` | the element-averaged concentration of solid-bound molecule with index 1 in a multiphasic material.|multiphasic|
|`sbm1_integral` | The integral of sbm 1 concentration over the multiphasic material domain.|multiphasic|
|`sbm1_referential_apparent_density` | The referential apparent density of solid-bound molecule with index 1 in a multiphasic material.|multiphasic|
|`sbm2` | the element-averaged concentration of solid-bound molecule with index 2 in a multiphasic material.|multiphasic|
|`sbm2_integral` | The integral of sbm 2 concentration over the multiphasic material domain.|multiphasic|
|`sbm2_referential_apparent_density` | The referential apparent density of solid-bound molecule with index 2 in a multiphasic material.|multiphasic|
|`sbm3` | the element-averaged concentration of solid-bound molecule with index 3 in a multiphasic material.|multiphasic|
|`sbm3_integral` | The integral of sbm 3 concentration over the multiphasic material domain.|multiphasic|
|`sbm3_referential_apparent_density` | The referential apparent density of solid-bound molecule with index 3 in a multiphasic material.|multiphasic|
|`sbm4` | the element-averaged concentration of solid-bound molecule with index 4 in a multiphasic material.|multiphasic|
|`sbm4_integral` | The integral of sbm 4 concentration over the multiphasic material domain.|multiphasic|
|`sbm4_referential_apparent_density` | The referential apparent density of solid-bound molecule with index 4 in a multiphasic material.|multiphasic|
|`sbm5` | the element-averaged concentration of solid-bound molecule with index 5 in a multiphasic material.|multiphasic|
|`sbm5_integral` | The integral of sbm 5 concentration over the multiphasic material domain.|multiphasic|
|`sbm5_referential_apparent_density` | The referential apparent density of solid-bound molecule with index 5 in a multiphasic material.|multiphasic|
|`sbm6` | the element-averaged concentration of solid-bound molecule with index 6 in a multiphasic material.|multiphasic|
|`sbm6_integral` | The integral of sbm 6 concentration over the multiphasic material domain.|multiphasic|
|`sbm6_referential_apparent_density` | The referential apparent density of solid-bound molecule with index 6 in a multiphasic material.|multiphasic|
|`sbm7` | the element-averaged concentration of solid-bound molecule with index 7 in a multiphasic material.|multiphasic|
|`sbm7_integral` | The integral of sbm 7 concentration over the multiphasic material domain.|multiphasic|
|`sbm7_referential_apparent_density` | The referential apparent density of solid-bound molecule with index 7 in a multiphasic material.|multiphasic|
|`sbm8` | the element-averaged concentration of solid-bound molecule with index 8 in a multiphasic material.|multiphasic|
|`sbm8_integral` | The integral of sbm 8 concentration over the multiphasic material domain.|multiphasic|
|`sbm8_referential_apparent_density` | The referential apparent density of solid-bound molecule with index 8 in a multiphasic material.|multiphasic|
|`sed` | strain energy density|solid|
|`solution_norm` | The L2 norm of the solution vector|core|
|`sx` | xx-component of the Cauchy stress|solid|
|`Sx` | The xx-component of the PK2 stress|solid|
|`sxy` | xy-component of the Cauchy stress|solid|
|`Sxy` | The xy-component of the PK2 stress|solid|
|`sxz` | xz-component of the Cauchy stress|solid|
|`Sxz` | The xz-component of the PK2 stress|solid|
|`sy` | yy-component of the Cauchy stress|solid|
|`Sy` | The yy-component of the PK2 stress|solid|
|`syz` | yz-component of the Cauchy stress|solid|
|`Syz` | The yz-component of the PK2 stress|solid|
|`sz` | zz-component of the Cauchy stress|solid|
|`Sz` | The zz-component of the PK2 stress|solid|
|`thx` | x-component of rotation pseudo-vector|solid|
|`thy` | y-component of rotation pseudo-vector|solid|
|`thz` | z-component of rotation pseudo-vector|solid|
|`total energy` | the total energy (elastic energy + kinetic) integrated over a domain.|solid|
|`U1` | first eigenvalue of right stretch tensor|solid|
|`U2` | second eigenvalue of right stretch tensor|solid|
|`U3` | third eigenvalue of right stretch tensor|solid|
|`ux` | x-coordinate of nodal displacement|solid|
|`Ux` | xx-component of the right stretch tensor|solid|
|`Uxy` | xy-component of the right stretch tensor|solid|
|`Uxz` | xz-component of the right stretch tensor|solid|
|`uy` | y-coordinate of nodal displacement|solid|
|`Uy` | yy-component of the right stretch tensor|solid|
|`Uyz` | yz-component of the right stretch tensor|solid|
|`uz` | z-coordinate of nodal displacement|solid|
|`Uz` | zz-component of the right stretch tensor|solid|
|`V` | the current volume of an element|core|
|`V1` | first eigenvalue of left stretch tensor|solid|
|`V2` | second eigenvalue of left stretch tensor|solid|
|`V3` | third eigenvalue of left stretch tensor|solid|
|`volume` | the volume inside a constraining surface.|core|
|`volume change` | the change in volume inside a constraining surface.|core|
|`volume pressure` | The pressure inside the constrained volume of a `volume` constraint.|solid|
|`vx` | x-component of center of mass velocity|solid|
|`Vx` | xx-component of the left stretch tensor|solid|
|`Vxy` | xy-component of the left stretch tensor|solid|
|`Vxz` | xz-component of the left stretch tensor|solid|
|`vy` | y-component of center of mass velocity|solid|
|`Vy` | yy-component of the left stretch tensor|solid|
|`Vyz` | yz-component of the left stretch tensor|solid|
|`vz` | z-component of center of mass velocity|solid|
|`Vz` | zz-component of the left stretch tensor|solid|
|`wf` | fraction of fatigued bonds|solid|
|`wi` | fraction of intact bonds|solid|
|`wx` | x-component of fluid flux|biphasic|
|`wy` | y-component of fluid flux|biphasic|
|`wz` | z-component of fluid flux|biphasic|
|`x` | x-coordinate of center of mass position|solid|
|`y` | y-coordinate of center of mass position|solid|
|`z` | z-coordinate of center of mass position|solid|
