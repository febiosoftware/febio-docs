# relative error

**Module:** core

**Category:** meshadaptorcriterion

**Type string:** `"relative error"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `error` | error | 0 | $\in \mathbb{R}$ |  |
| `data` | data |  | N/A |  |


## Description

This criterion evaluates a relative error metric for each element. 

If the `error` parameter is nonzero, this criterion will evaluate a relative size metric for each element. Otherwise, the actual relative error is evaluated.

The `data` parameter specifies the metric to evaluate the element values. Any other meshadaptor criteria. 


