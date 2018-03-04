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
    
    return 



def cleanmix(typemix_result,column,type=majority,keep=TRUE):
    '''
    The function helps to delete the observations with unwanted data types in indicated columns in a data frame.
    
    Parameters
    ----------
    typemix_result : list
        the returned result (a list of 3 data frames) by typemix function
        
    column: list
        a number or a vector of numbers indicating the ID of columns where you want to apply the function to remove the mixture of data types

    type: a string
        a data type that you want to keep or delete. The default will be the majority type in the column
        
    keep: boolean
        if you want to keep or delete the data type you specify. The default setting is keep=TRUE
        
    Returns
    -------
    pandas.DataFrame
        A data frame with observations in unwanted data types in the columns specified deleted.
    
    '''
    
    
    return