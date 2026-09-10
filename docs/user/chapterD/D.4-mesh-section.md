# D.4 Mesh Section

The Mesh section defines the mesh of the model and its decomposition into separate regions. A region can be a node set, a surface (i.e. facet set), or a domain (element set). The mesh section is defined by the following sub-sections.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| NODE_SECTION | 0x01041000 | beginning of node section |
| DOMAIN_SECTION | 0x01042000 | beginning of domain section |
| SURFACE_SECTION | 0x01043000 | beginning of surface section |
| NODESET_SECTION | 0x01044000 | beginning of node set section |
| PARTS_SECTION | 0x01045000 | beginning of parts section |

</div>

/// table-caption

The child sections of the _Mesh_ section.

///

## Node Section

The NODE section defines a set of nodes of the mesh. Each node section starts with a NODE_HEADER followed by a NODE_COORDS section.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| NODE_HEADER | 0x01041100 | node header |
| NODE_COORDS | 0x01041200 | node data list |

</div>

/// table-caption

The Node section consists of a header and a list of coordinates.

///

The header contains the following information.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| NODES | 0x01041101 | number of nodes (N) in this NODE section |
| DIM | 0x01041102 | dimension of node set (i.e. nr. of coords) |
| NAME | 0x01041103 | name of node set. |

</div>

/// table-caption

The header of the Node section.

///

The NODES parameter defines the number of nodes defined in this section. The DIM parameter sets the number of coordinates that will be defined for each node (e.g. 3 for 3D problems). Each NODE section also implicitly defines a node set. The NAME attribute defines the name of this node set.

Then the NODE_COORDS section follows, which defines the nodal data for each node. This data field stores the nodal IDs and coordinates for all the nodes in the mesh. The size of the field is defined by N*DWORD + DIM*N*FLOAT where N is the number of nodes in the mesh (as defined in the header section), DIM is the dimension, and FLOAT is the size of a single precision floating point number (4 bytes). The order of the data is (e.g. if DIM equals 3),

<div markdown="1" style="display: flex; justify-content: center;">

| ID1 | x1 | y1 | z1 |... | IDn | xn | yn | zn |
|---|---|---|---|---|---|---|---|---|

</div>

Here, x[i] is the x-coordinate of node i and similarly for y and z.

## Domain Section

The Domain section lists all domains (i.e. element sets) in the mesh. Each domain is identified by a DOMAIN section.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| DOMAIN | 0x01042100 | beginning of a domain section |

</div>

/// table-caption

The Domain section consists of a list of domains.

///

Each domain is defined by two sub-sections, a _domain header_ and an _element list_.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| DOMAIN_HEADER | 0x01042101 | beginning of domain header |
| ELEMENT_LIST | 0x01042200 | list of element connectivity |

</div>

/// table-caption

Each domain section consists of a header section and an element list.

///

The _domain header_ contains the following data fields.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** | **size** |
|---|---|---|---|
| ELEM_TYPE | 0x01042102 | element type | DWORD |
| PART_ID | 0x01042103 | part ID | DWORD |
| ELEMENTS | 0x01032104 | number of elements | DWORD |
| NAME | 0x01032105 | an optional name for this domain | CHAR64 |

</div>

/// table-caption

The domain header section.

///

The ELEM_TYPE defines the type of elements stored in the domain. It can have one of the following values.

<div markdown="1" style="display: flex; justify-content: center;">

| **ELEM_TYPE** | **VALUE** | **description** |
|---|---|---|
| HEX8 | 0 | 8-node hexahedron solid element |
| PENTA6 | 1 | 6-node pentahedron solid element |
| TET4 | 2 | 4-node tetrahedron solid element |
| QUAD4 | 3 | 4-node quadrilateral shell element |
| TRI3 | 4 | 3-node triangular shell element |
| TRUSS2 | 5 | 2-node linear truss element |
| HEX20 | 6 | 20-node quadratic hexahedral element |
| TET10 | 7 | 10-node quadratic tetrahedral element |
| TET15 | 8 | 15-node quadratic tetrahedral element |
| HEX27 | 9 | 27-node quadratic hexahedral element |

</div>

/// table-caption

The supported element types.

///

The PART_ID corresponds to the ID of one of the parts defined in the Parts section.

The ELEMENTS field is the number of elements in the domain.

After the domain header the element list follows. For each element it defines an ELEMENT data field.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** | **size** |
|---|---|---|---|
| ELEMENT | 0x01042201 | Element ID and connectivity | DWORD*(NE+1) |

</div>

/// table-caption

Each element is defined by an ID and a list of nodes that defines the connectivity.

///

If NE is the number of nodes per element, then this data field stores NE+1 DWORDS. The first DWORD is the element ID, a unique number that identifies the element. The following NE DWORD’s define the element connectivity.

## Surface Section

The surface section defines the surfaces of the mesh for which data is stored in the plot file. Each surface begins with a SURFACE section.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| SURFACE | 0x01043100 | beginning of a surface section |

</div>

/// table-caption

The Surface section consists of a list of surface definitions.

///

The surface section follows a similar structure as the domain section, namely a _surface header_ followed by a _facet list_.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| SURFACE_HEADER | 0x01043101 | beginning of surface header |
| FACET_LIST | 0x01043200 | facet connectivity list |

</div>

/// table-caption

Each surface is defined by a header section and a facet list.

///

The surface header contains the following data fields.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** | **size** |
|---|---|---|---|
| SURFACE_ID | 0x01043102 | surface ID | DWORD |
| FACETS | 0x01043103 | Number of facets | DWORD |
| NAME | 0x01043104 | A name for this surface | CHAR64 |
| MAX_FACET_NODES | 0x01043105 | max nodes per facet | DWORD |

</div>

/// table-caption

The surface header section.

///

The SURFACE_ID is a unique identifier and FACETS is the number of facets in the surface.

The FACET_LIST follows the header and contains a FACET data field for each facet in the surface.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** | **size** |
|---|---|---|---|
| FACET | 0x01043201 | facet definition | DWORD*NF |

</div>

/// table-caption

A facet definition.

///

Here, NF = MAX_FACET_NODES + 2. The first DWORD is a unique identifier (which currently should be ignored). The second DWORD is the number of nodes for this facet. This also defines the facet type. (For instance, 3 nodes define a triangle, 4 nodes define a quadrilateral). Next, the node ID’s follow.

## Node Set Section

The Node Set section defines all the node sets where a node set is a named collection of nodes. Each nodeset begins with the NODESET section.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| NODESET | 0x01044100 | beginning of a nodeset section |

</div>

/// table-caption

The Node Set section consists of a list of NODESET sections.

///

Next, a header section and a node list section follow.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| NODESET_HEADER | 0x01044101 | beginning of nodeset header |
| NODE_LIST | 0x01044200 | node list |

</div>

/// table-caption

Each nodeset consists of a header and a list of node numbers.

///

The header is composed of the following chunks.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** | **size** |
|---|---|---|---|
| NODESET_ID | 0x01044102 | nodeset ID | DWORD |
| NODES | 0x01044104 | Number of nodes | DWORD |
| NAME | 0x01044103 | An optional name for this nodeset | CHAR64 |

</div>

/// table-caption

The node set header.

///

The node list is a list of all the nodes that belong to this node set. All node indices are zero-based.

## Parts Section

The Parts section lists the parts defined in the plot file. For each part, a PART section is written.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| PART | 0x01045100 | beginning of a part definition |

</div>

/// table-caption

The Part section consists of a list of parts.

///

Then, for each part the following fields are written.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** | **size** |
|---|---|---|---|
| PART_ID | 0x01045101 | ID of part | DWORD |
| PART_NAME | 0x01045102 | Name of part | CHAR64 |

</div>

/// table-caption

A part definition.

///

The ID is a unique number that will be used in the domain definitions to refer to this part. The NAME is a textual description that can be used by the post-processor to present the part to the user.
