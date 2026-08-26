The `fsi-volume-erosion` adaptor erodes elements that have a volume ratio that is less than a user-specified threshold. 

The `min_volume_ratio` parameter sets the minimum threshold value. 

The `max_elems` is the maximum number of elements that can be eroded in one pass and `mat_iters` is the maximum number of passes that will be applied. 

The `metric` allows users to choose the criterion for erosion. The value `0` (default) uses the volume ratio; The value `1` uses the second principal value of the right Cauchy-Green tensor. 
