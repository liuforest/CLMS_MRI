# diffusion_mri
 
Preprocessing & Analysis pipelines for CLMS MRI Data.

## 
```
Analysis ~ 
Preprocessing ~ prep
Scripts ~ 
```

## Data Directory Structure
```
data_CLMS
|
|----0_3T_raw ~ all 3T scans & data
|----|  various structure/file formats
|
|----0_7T_raw ~ all 7T scans & data
|----|  various structure/file formats
|
|----anatomical 
|
|----diffusion 
|----|  1_dcm *(subdirectories containing ordered dicom files)*
|----|      abc_123_m00
|----|      bcd_234_m00
|----|      ...
|----|      xyz_789_m24
|----|          0010001.dcm
|----|          0010002.dcm
|----|          ...
|----|          0010999.dcm
|----|      
|----|  2_nifti *(subdirectories containing converted nifti, w/associated bvec/bval & json)*
|----|      abc_123_m00
|----|      bcd_234_m00
|----|      ...
|----|      xyz_789_m24
|----|          xyz_789_m24.bval
|----|          xyz_789_m24.bvec
|----|          xyz_789_m24.nii
|----|          xyz_789_m24.json
|----|      
|----|  2.1_brain_mask
|----|      
|----|  3.1_preproc_denoise
|----|      
|----|  3.2_preproc_degibbs
|----|      
|----|  3.3_preproc_convert
|----|      
|----|  3.4_preproc_final
|----|      
|----|  4.1_CSD *Constrained Spherical Deconvolution for fiber estimation*
|----|      
|
|----functional
|
|
|
|
|
|
|----MP2RAGE_7T
|



.../OneDrive/CLMS_OTHER_DATA (for non-image data, e.g. neuropsych tests, freesurfer structural csv files, etc.)

```

## Notebooks & Scripts
