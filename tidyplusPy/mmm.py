""" tidyplusPy.mmm"""

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
    """
    df = dataframe
    df_num = df._get_numeric_data() ### Get only numeric columns from dataframe
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
    
    
    elif method == "mode" :
        result = df.apply(lambda x: x.fillna(x.mode()[0]),axis=0) ## this is applied to both numeric and character values
    else :
        print("missing can't be imputed")
    
    return result ## imputed dataset




"""Dummy Dataset"""

# NaN = float('nan')
# ID = [1, 2, 3, 4, 5, 6, 7]
# A = [NaN, NaN, NaN, 0.1, 0.3, 0.3, 0.4]
# B = [0.2, NaN, 0.2, 0.7, 0.9, NaN, NaN]
# C = [NaN, 'A', 'B', NaN, 'C', 'D', 'D']
# D = [NaN, 'C', 'E', NaN, 'C', 'H', 'D']
# columns = {'A':A, 'B':B, 'C':C, 'D':D}
# df = pd.DataFrame(columns, index=ID)
# df.index.name = 'ID'
# print(df)

"""Usage"""

# mmm(df,method = "mode")