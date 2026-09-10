# E.2 Logfile Variables {: #sec:Logfile-Variables }

As discussed in [Logfile](../chapter3/3.19-output-section.md#subsec:Logfile), there are different category or classes of log variables. The following sections lists the available variables.

## Node_Data Class {: #subsec:Node_Data-Class }

The _node_data _class defines a set of nodal variables. The data is stored for each node that is listed in the item list of the_ node_data_ element or for all nodes if no list is defined.

For example, to store the current nodal positions of all nodes, use the following _node_data _element:

```
<node_data data="x;y;z"></node_data>
```

You can store the total nodal displacement for nodes 1 through 100, and all even numbered nodes 200 through 400 as follows:

```
<node_data data="ux;uy;uz">1:100:1,200:400:2</node_data>
```

## Face_Data Class

The _face_data _class defines a set of surface variables. This item requires the_ surface _attribute, which defines the surface that will be used to extract the data from. The surface must be defined in the_ Mesh_ section. The data is stored for each surface facet that is listed in the item list, or for all facets of the surface if no list is defined.

_Example:_

This example stores the contact gap and contact pressure of all the facets of surface “FacetOnFacetSliding1_primary”. The surface is defined in the Mesh section.

```
<logfile>
  <face_data data="contact gap;contact pressure" surface="FacetOnFacetSliding1_primary"/>
</logfile> 
```

## Element_Data Class {: #subsec:Element_Data-Class }

The _element_data _class defines a set of element variables. The data is stored for each element that is listed in the item list of the_ element_data_ element or for all nodes if no list is defined. Note that the actual value is the average over the element's integration points values (if applicable).

For example, to store the (average) Cauchy stress for all elements, define the following data element:

```
<element_data data="sx;sy;sz;sxy;syz;sxz" name="element stresses"> </element_data>
```

## Domain Data Class

The _domain_data_class_ defines variables that are calculated on an entire domain. The variables are often quantities integrated over the entire domain.

## Surface Data Class

The _surface_data _class defines variables that are calculated over an entire surface.

## Rigid_Body_Data Class {: #subsec:Rigid_Body_Data-Class }

The _rigid_body_data_ class defines a set of variables for each rigid body. The data is stored for each rigid body that is listed in the item list of the _rigid_body_data_ element or for all rigid bodies if no list is defined. The following variables are defined. Note that the item referenced in the item list is the material number of the rigid body.

For example, to store the rigid body reaction force of rigid body 2 and 4 add the following data element. Note that the 2 and 4 refer to the rigid body material number as defined in the _Material_ section of the input file:

```
<rigid_body_data data="Fx;Fy;Fz">2,4</rigid_body_data>
```

## Rigid_Connector_Data Class {: #subsec:Rigid_Connector_Data-Class }

The _rigid_connector_data_ class defines a set of variables for each rigid joint or rigid connector. The data is stored for each rigid joint or rigid connector that is listed in the item list of the _rigid_connector_data_ element or for all rigid connectors if no list is defined. Note that the item referenced in the item list is the rigid connector number in the order in which rigid connectors appear in the input file.

For example, to store the reaction forces and moments at rigid joints 2 and 4 add the following data element:

```
<rigid_connector_data data="RCFx;RCFy;RCFz;RCMx;RCMy;RCMz">2,4</rigid_connector_data>
```

The rigid connector translation and rotation variables return relative motions of the rigid bodies connected by rigid joints and other rigid connectors (Section [Rigid Connectors](../chapter3/3.12-rigid-section.md#subsec:Rigid-Connectors)). The rotation components represent the components of a vector whose direction is along the axis of rotation, and whose magnitude is the (counter-clockwise) angle of rotation. These relative motions are calculated as the motion of _body_b _relative to_ body_a_, expressed in the local Cartesian basis of _body_a_, whose initial origin is at_ joint_origin_. This Cartesian basis (which generally moves with _body_a_) has its first axis along_ rotation_axis_ (for revolute and planar joints) or _translation_axis _(for prismatic joints) or_ joint_axis_ (for cylindrical joints); the second axis is along the _transverse_axis _(for revolute, prismatic and cylindrical joints) or_ translation_axis_1_ (for planar joints). For spherical joints, springs, dampers, angular dampers and contractile forces, the axes are always aligned with the global Cartesian basis.

For springs, dampers and contractile forces, the returned translation components represent the relative position vector between insertion points on _body_b _and_ body_a_. The magnitude of this vector represents the distance between those points.

## Model Data Class

This category encompasses variables that are not necessarily tied to specific components of a model.
