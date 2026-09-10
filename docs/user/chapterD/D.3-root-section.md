# D.3 Root Section

The ROOT section is the first block in the file. This block contains the _header_ and _dictionary_ sections as child blocks.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| HEADER | 0x01010000 | contains the header section |
| DICTIONARY | 0x01020000 | contains the dictionary section |

</div>

/// table-caption

The Root section has two child sections, the _header_ and the _dictionary_ sections.

///

These sections will be detailed below.

## Header Section

The first section of the root block is the header section. It stores the following data:

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** | **size** |
|---|---|---|---|
| VERSION | 0x01010001 | version of the file format | DWORD |
| COMPRESSION | 0x01010004 | Compression flag | DWORD |
| AUTHOR | 0x01010005 | Author name | CHAR64 |
| SOFTWARE | 0x01010006 | Software that generated this file | CHAR64 |

</div>

/// table-caption

The Header Section

///

Currently, the VERSION will always be 0x0008. The COMPRESSION flag indicates whether the mesh and state sections are compressed or not. Data compression is an optional feature for plot files, and will not be discussed in this document. The AUTHOR contains the name of the person who created the file. The SOFTWARE tag contains the name of the software that generated the file. (Note that not all header data might be present in a plot file. For instance, as of FEBio3, the AUTHOR tag is not written to the plot file.)

## Dictionary Section

When running a FEBio analysis, FEBio will store the values of certain user-selected variables (e.g. stress, temperature, fluid pressure, etc.) to the plot file. In order for a parser to know which variables were written, it needs to read the dictionary section. This section stores a list of variables, including their names, which are stored in the plot file. Specifically, three attributes are stored for each data variable: a name that provides a description of the data, the data type (scalar, vector, tensor) and the storage format. In addition, the variables are grouped by category. Data variables can be defined for node sets, domains (element sets) and surfaces. In addition, global variables (which are not associated with any part of the model) can also be defined. Each of these categories has their own sub-section in the dictionary.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| GLOBAL_DATA | 0x01021000 | lists global data in model |
| NODESET_DATA | 0x01023000 | lists data associated with the node sets |
| DOMAIN_DATA | 0x01024000 | lists data associated with domains |
| SURFACE_DATA | 0x01025000 | lists data associated with surfaces |

</div>

/// table-caption

The Dictionary Section

///

Note that all of these sections are optional. For example, if a model does not define global data, that section will not be part of the plot file.

Each of these sub-sections defines a list of dictionary items defined by the following tag.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** |
|---|---|---|
| DICTIONARY_ITEM | 0x01020001 | beginning of dictionary item |

</div>

/// table-caption

The dictionary consists of _dictionary items_.

///

Each dictionary item contains three fields.

<div markdown="1" style="display: flex; justify-content: center;">

| **Tag** | **ID** | **description** | **size** |
|---|---|---|---|
| ITEM_TYPE | 0x01020002 | type of data | DWORD |
| ITEM_FORMAT | 0x01020003 | storage format of data | DWORD |
| ITEM_NAME | 0x01020004 | textual description of data | CHAR64 |
| ITEM_ARRAY_SIZE | 0x01020005 | Size of array variables | DWORD |
| ITEM_ARRAY_NAME | 0x01020006 | Name of array variable | CHAR64 |

</div>

/// table-caption

Structure of dictionary item.

///

The ITEM_ARRAY_SIZE and ITEM_ARRAY_NAME are only used for array variables. The ITEM_ARRAY_SIZE defines the number of data items in the array. For each data item, the ITEM_ARRAY_NAME defines an optional name for that item.

The type of the data can be any of the following values.

<div markdown="1" style="display: flex; justify-content: center;">

| **ITEM_TYPE** | **VALUE** | **description** |
|---|---|---|
| FLOAT | 0 | single precision (s.p.) floating point |
| VEC3F | 1 | 3D vector of s.p. floats (stored in x, y, z order) |
| MAT3FS | 2 | symmetric 2nd order tensor of s.p. floats (stored in xx, yy, zz, xy, yz, xz order) |
| MAT3FD | 3 | diagonal matrix of s.p. floats (stored in xx, yy, zz order). |
| TENS4FS | 4 | symmetric fourth-order tensor of s.p. floats. |
| MAT3F | 5 | 3x3 matrix of floats (stored in row order). |
| ARRAY_FLOAT | 6 | Array of floats. |
| ARRAY_VEC3F | 7 | Array of vec3f. |

</div>

/// table-caption

The supported data types.

///

As explained below, data will be stored for different regions of the mesh, where a region can be a node set, a surface, or a domain (element set). A region is composed of items where an item is a single shape in the region. For node sets, an item will refer to a node, for surfaces this will be a facet and for domains an item will refer to an element. The storage format defines how many values are written for each region and how the values relate to the geometry of the region or items. The following values are currently defined.

<div markdown="1" style="display: flex; justify-content: center;">

| **ITEM_FORMAT** | **VALUE** | **description** |
|---|---|---|
| NODE | 0 | one value for each node of the region |
| ITEM | 1 | one value for each item |
| MULT | 2 | one value for each node for each item |

</div>

/// table-caption

The different storage format identifiers.

///

The easiest format to understand is the ITEM format which simply stores one value for each item of the region. Thus, one value for each node or for each facet or for each element, depending on the region type. The MULT format defines a value for each node of each item. For example, for a surface of quads, the data will contain four values for each facet, one for each of the four nodes. The NODE format stores a single value for each node of the region. Each type of region (node set, surface, or domain) implicitly also defines a set of nodes, namely all the nodes that are part of that region. With the NODE format, the user defines a single value for each of the nodes in this implicit node set. This will be explained in more detail below in the state section.

Note that the storage formats are only important for surfaces and domains. For other categories (e.g. node sets), all formats are essentially equivalent, and can safely be ignored.
