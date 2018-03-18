#!/usr/bin/python

import random
import numpy as np
import pandas as pd
import six


def mmm(data, method= "mean/median/mode"):
    """Multivariate Imputation by Mean, median or mode
    ----------
    data: Pandas data frame
        Data to impute.
    method : could be Mean,Median,Mode
    RETURNS
    -------
        Imputed data: Pandas dataframe
        
    EXAMPLE
    -------
    #Dummy data
    
     NaN = float('nan')
     ID = [1, 2, 3, 4, 5, 6, 7]
     A = [NaN, NaN, NaN, 0.1, 0.3, 0.3, 0.4]
     B = [0.2, NaN, 0.2, 0.7, 0.9, NaN, NaN]
     C = [NaN, 'A', 'B', NaN, 'C', 'D', 'D']
     D = [NaN, 'C', 'E', NaN, 'C', 'H', 'D']
     columns = {'A':A, 'B':B, 'C':C, 'D':D}
     df = pd.DataFrame(columns, index=ID)
     df.index.name = 'ID'
     
    USAGE
    ------
    
    mmm(df,method = "mode") ## method can be replaced with mean or median
    
    """
    if method not in ("mean","median","mode"):
        raise Exception("Only mean, median and mode can be used as methods in mmm")
    
    if not isinstance(data, pd.DataFrame) :
        raise TypeError('datatype for input data can only be pandas dataframe')
    if  data.shape[0] < 2 :
        raise TypeError('dataframe should have more than one row')
    for i in range(0,len(list(data.count()))):
        if list(data.count())[i] < 2:
            raise ValueError('dataframe should have atleast one not-null value in each column')

    

    df = data
    
    df_num = df._get_numeric_data() ### Get only numeric columns from dataframe
    
    if df_num.shape[1] == 0 :
        raise Exception("No numeric columns, mean and median imputation not valid")
    if (df_num.shape[1] > 0 and method == "mode") :
        result = df.apply(lambda x: x.fillna(x.mode()[0]),axis=0) ## this is applied to both numeric and character values
    if df_num.shape[1] > 0 :
        if method == "mean" :
            out = df_num.apply(lambda x: x.fillna(x.mean()),axis=0)
            a = []
            for i in df.columns.values.tolist() :
                if i not in out.columns.values.tolist() :
                    a.append(i)     ## Step to identify non-numeric columns
    
            result = pd.concat([out, df.ix[:,a]], axis=1) # merge all columns for result
        
        
        elif method == "median" :
            out = df_num.apply(lambda x: x.fillna(x.median()),axis=0) ### Get only numeric columns from dataframe
            a = []
            for i in df.columns.values.tolist() :
                if i not in out.columns.values.tolist() :
                    a.append(i)  ## Step to identify non-numeric columns
    
            result = pd.concat([out, df.ix[:,a]], axis=1) # merge all columns for result
    
    else :
        print("missing can't be imputed")
    
    return result ## imputed dataset



