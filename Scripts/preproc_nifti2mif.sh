# script for batch converting nifti+bval+bvec files to mif

# inputs: 
# directory containing subdirectories named by subject (subdirectories should contain the .nii, .bvec, and .bval files)
echo "Enter directory containing nifti data:"
read $input_dir

# directory to place the output file
echo "Enter directory to store output .mif files:"
read $output_dir

echo "RESULT: $input_dir $output_dir"

