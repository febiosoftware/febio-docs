# quick_restart_test

**Module:** core

**Category:** task

**Type string:** `"quick_restart_test"`

## Parameters

This feature has no parameters.


## Description

The `quick_restart_test` runs a test on the restart feature after model initialization. This task initializes the model and then writes a dump file. After that, the model is cleared and the dump file is read to re-initialize the model. Any issues that occur during re-initialization will be reported. If no problems are encountered, the task finishes. (Note that the model is not solved.) 
