# stress

**Module:** solid

**Category:** meshadaptorcriterion

**Type string:** `"stress"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `metric` | metric | 0 | $\in \mathbb{Z}$ |  |


## Description

This criterion selects elements that exceed a maximum stress value. 

The values for the metric defines the stress measure to use

* 0=effective stress
* 1=max principal stress.

