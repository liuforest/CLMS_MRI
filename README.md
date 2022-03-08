# diffusion_mri
 
Analysis pipeline for 3 T Diffusion MRI data. 

## Directory Structure
```
data_CLMS
|
|----0_raw ()
|----|  abc_123_m00
|----|  bcd_234_m00
|----|  ...
|----|  xyz_789_m24
|
|----diffusion 
|----|  1_dcm (subdirectories containing ordered dicom files)
|----|      
|----|  2_nifti (subdirectories containing converted nifti, w/associated bvec/bval & json)
|----|      
|
|----etc (other projects)

```

