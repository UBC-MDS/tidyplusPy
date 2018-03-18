#!/usr/bin/env python

def typemix(df):
    '''
    The function helps to find the columns in a data frame that contains different types of data.
    Python has many data types. The function roughly identifies if an observation belongs to one of the 3 main data types, numbers, booleans, and strings.

    Parameters
    ----------
    df : pandas.DataFrame
        the data frame that we want to check

    Returns
    -------
    list
        A list of 3 data frames. First one is the input data frame, the second one has the same dimension as the first one,
        but has corresponding data type marked in the cells of the columns where mixture status is found.
        The third data frame is the summary of result, with ID of the columns as row names and the 3 data types as headers.
        It tells us the total number of each data type found in each column where mixture is found.

    '''
    import pandas as pd
    import numpy as np

    if not isinstance(df,pd.DataFrame):
        raise TypeError("Input must be a data frame")

    # locate the columns with type mixture
    # I find that the columns with type mixture is put under object;
    # While the columns with only characters are also put under object, so we need to exclude these cases.
    columns_typemix=[]

    # other variable declaration
    # check location and number of each data type in the columns with mixed data types
    total_number=[]
    total_logical=[]
    total_character=[]

    # a function check if a input is boolean or not
    # since if we use excel and type any format of true/false, we will get TRUE/FALSE if we set cell format to general,
    # only TRUE/FALSE are treated as boolean data in this fuction.
    def boolean_checker(df,column):
        alist=df.iloc[:,column].tolist()
        result_list=[]
        for i in range(len(alist)):
            if alist[i] in ["TRUE","FALSE"]:
                result_list.append(True)
            else:
                result_list.append(False)
        return result_list

    # define function check if an input is a number, to be used in the series.apply()
    def number_checker(df,column):
        alist=pd.to_numeric(df.iloc[:,i], errors='coerce').tolist()
        ind=~np.isnan(alist)
        return ind.tolist()

    for i in range(df.shape[1]):
        if str(df.iloc[:,i].dtypes)=='object':
            # exclude the possibility of all characters
            # check numbers
            b=number_checker(df,i)
            # check boolean
            c=boolean_checker(df,i)

            if sum(b)!=0 or sum(c)!=0:
                columns_typemix.append(i)

    # create a data frame with same dimension as the input df
    type_df = pd.DataFrame().reindex_like(df)

    for i in columns_typemix:
        # check if data is a number
        index=number_checker(df,i)
        total_number.append(sum(index))
        type_df.iloc[index,i]="number"
        # check if data is boolean
        index=boolean_checker(df,i)
        total_logical.append(sum(index))
        type_df.iloc[index,i]="logical"
        # the rest of data should be character
        count=0
        for j in range(type_df.shape[0]):
            if not pd.isnull(df.iloc[j,i]) and pd.isnull(type_df.iloc[j,i]):
                type_df.iloc[j,i]="character"
                count=count+1
        total_character.append(count)


    # create a data frame for result summary (the third df as output)
    values = np.zeros((len(columns_typemix),4))
    columns=["Column_ID","number", "character",	"logical"]
    summary_df=pd.DataFrame(values, columns=columns)
    summary_df.iloc[:,0]=columns_typemix
    summary_df.iloc[:,1]=total_number
    summary_df.iloc[:,2]=total_character
    summary_df.iloc[:,3]=total_logical

    # create return list with 3 data frames
    return_list=[df,type_df,summary_df]
    return return_list
