def append_column(df, dir, column_name, search_phrase='.nii'):
    '''
    This function appends column of filepaths to a dataframe matching by subject_id. 

    Files within folders must contain the subject id string pattern. 

    INPUTS:
        1. main_df          - the dataframe to append columns to
        2. folder_name      - folder containing files/paths to append
        3. column_name      - name of the column to append
        4. search_phrase    - text pattern to look for inside specified folder (default '.nii')

    '''
    # search directory for phrase and store as a list
    filelist = !find "{dir}" ~+ -type f -name "*{search_phrase}*"

    # convert list to a dataframe and create a column matching subject_id
    tmp_df = pd.DataFrame({'subject_id':"", column_name:filelist})
    tmp_df['subject_id'] = tmp_df[column_name].str.extract(r'(\w{3}_\d{3}_m\d{2})')

    # append the new filepaths by matching subject_id 
    df = pd.merge(df, tmp_df, on='subject_id')

    return df