'
- Given a directory, script searches for all tar.gz files (including subdirectories) & and extracts them to a folder with the same name. 
- If a folder with the same name already exists, do not extract. 
- For targz with more targz inside, run script again
'

# prompt user for input directory path
echo "Enter path of input directory:"
read $input_dir

# display all targz files in the input dir that don't have corresponding unpacked folder
echo "List of all unpacked tar.gz files found:"
echo find . -name '*.tar.gz'

# unpack all tar.gz 


## IN PROGRESS
