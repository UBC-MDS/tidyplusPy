#!/usr/bin/env python

def cleanmix(typemix_result,column,type,keep=True):
    '''
    The function helps to delete the observations with unwanted data types in indicated columns in a data frame.

    Parameters
    ----------
    typemix_result : list
        the returned result (a list of 3 data frames) by typemix function

    column: list
        a number or a vector of numbers indicating the ID of columns where you want to apply the function to remove the mixture of data types

    type: a string or a vector of strings
        The data types that you want to keep or delete.

    keep: boolean
        if you want to keep or delete the data type you specify. The default setting is keep=TRUE

    Returns
    -------
    pandas.DataFrame
        A data frame with observations in unwanted data types in the columns specified deleted.

    '''
    import pandas as pd
    import numpy as np
    import warnings

    if not isinstance(typemix_result,list):
        raise TypeError("The input should be a list of data frames")

    result=typemix_result[0].copy()

    # the code for main function:
    if isinstance(column,list):
        for i in range(len(column)):
            ID=column[i]
            if ID in typemix_result[2]['Column_ID']:
                # locate the type of data of interest
                index=typemix_result[1].iloc[:,ID]==type[i]

                if sum(index)==0:
                    warnings.warn("The column deos not have the data type", UserWarning)
                else:
                    # check if keep or not
                    if keep:
                        index=~ index
                        index=index.tolist()
                        result.iloc[index,ID]=float('nan')
                    else:
                        index=index.tolist()
                        result.iloc[index,ID]=float('nan')
            else:
                warnings.warn("A column deos not have type mixture", UserWarning)

    else: # if the input just one number
        if column in typemix_result[2]['Column_ID']:
            # locate the type of data of interest
                index=typemix_result[1].iloc[:,column]==type
                if sum(index)==0:
                    warnings.warn("The column deos not have the data type", UserWarning)
                else:
                    # check if keep or not
                    if keep:
                        index=~ index
                        index=index.tolist()
                        result.iloc[index,column]=float('nan')
                    else:
                        index=index.tolist()
                        result.iloc[index,column]=float('nan')  
        else:
            warnings.warn("A column deos not have type mixture", UserWarning)


    return result
