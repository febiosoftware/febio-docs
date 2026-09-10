# D.1 Introduction

This appendix describes the structure of the FEBio binary database (more commonly referred to as the FEBio plot file), which stores the results of a FEBio analysis. The FEBio binary database format is both self-describing and extendable. A user can understand the contents of the file by simply parsing the block structure of the file. The file format is made extensible by providing an abstract layer between the data and the file system. This layer defines the file structure as a hierarchy of data blocks. The result is that each file is now structured similarly as a file folder. Each block can be viewed as a file in the folder and each branch in the hierarchy as a sub-folder.

The database consists of four parts:

1. the **header** contains some general info that may be useful for parsing the rest of the file.

1. the **dictionary** presents a textual description for each data field in the file. This can be used to identify the contents of each data field.

1. the **mesh section** defines the mesh of the model.

1. the **state sections** contain the actual data or results for the field variables.

The following sections describe the details of the database format. In the next section, the block-structure of the file is explained. The sections thereafter describe the different parts of the database.

## Changes in this version

This appendix describes version 3.0 of the binary database format. This version of the FEBio Binary Database Specification differs in a few important aspects from the previous version. It addresses the following issues:

• Reduce plot file size by describing rigid bodies via rigid body mechanics.

• Reduce plot file size by identifying non-mutable data, which is data that that does not change in different states.

• Add support for more generic “objects” that may not be represented via the mesh. In FE simulations, additional structures can be present that interact with the FE parts, but are themselves not part of the FE mesh. Examples are rigid bodies and the various mechanisms to connect rigid bodies (e.g. springs, joints, etc.).

• The State section was modified so that the position of non-rigid nodes is redefined in each section.
