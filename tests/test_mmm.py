#!/usr/bin/env python

import numpy as np
import pytest
import pandas as pd
import tidyplusPy
from tidyplusPy import mmm as mmm

# dummy data for MMM
data = pd.DataFrame(data=({'v_num': [4.1,np.nan,12.2,11,3.4,1.6,3.3,5.5], 'v_char': ['one','two',None,'two','two','one','two','two']}))

col = list(data["v_num"])
dat = [1,2,3,np.nan]

# dummy data for EM
matrix= np.random.rand(5,5)
matrix[1,0] = np.nan
matrix[2,1] = np.nan
matrix[4,2] = np.nan
matrix[3,3] = np.nan
matrix[0,0] = np.nan

d = pd.DataFrame(data=({'col1': [1], 'col2': ['a']}))
d2 = pd.DataFrame(data=({'col1': [1,None,None], 'col2': ['a',None,None]}))
d3 = pd.DataFrame(data=({'col1': [1,2,None], 'col2': ['a',None,'c']}))

d4 = pd.DataFrame(data=({'col1': [True,False,None], 'col2': ['a',None,'c']}))
e = pd.DataFrame(data=({'col2': ['a',None,'c']}))


df = pd.DataFrame(data=({'v_num': [4,np.nan,5,6,7,np.nan,9]}))
df2 = pd.DataFrame(data=({'v_char': ['one','two',None,'two','two','two']}))

mean_out = mmm.mmm(df,method="mean")
df_mean = pd.DataFrame(data=({'v_num': [4,6.2,5,6,7,6.2,9]}))


med_out = mmm.mmm(df,method="median")
df_med = pd.DataFrame(data=({'v_num': [4,6,5,6,7,6,9]}))


mod_out = mmm.mmm(df2,method="mode")
df_mod = pd.DataFrame(data=({'v_char': ['one','two','two','two','two','two']}))


# Usage

# mmm.mmm(data,method="mode")

# em.em(matrix)

def test_input():
    """
    Tests incorrect/unacceptable input data for mmm
    These should raise a type error.

    For mmm datatype should be pandas dataframe
    
    check data type
    """


        
   # Check MMM input other than pandas dataframe
        
    with pytest.raises(TypeError):
        mmm.mmm((0, np.nan, 2),method ="mean")
    with pytest.raises(TypeError):
        mmm.mmm(2,method ="mean")
        
    with pytest.raises(TypeError):
        mmm.mmm([1,2,3],method ="mean")
        
    with pytest.raises(TypeError):
        mmm.mmm(False,method ="mean")
        
    with pytest.raises(TypeError):
        mmm.mmm(['a','b'],method ="mode")
    with pytest.raises(TypeError):
        mmm.mmm(['a','b'],method ="median")
        
def test_row_input():
    
    """
    Checks row input in dataframe
    
    dataframe need more than 1 rows to estimate missing
    
    """
  
    # check if dataframe has more than 1 row
    # d = pd.DataFrame(data=({'col1': [1], 'col2': ['a']}))
    with pytest.raises(TypeError):
       mmm.mmm(pd.DataFrame(data=({'col1': [1], 'col2': ['a']})),method = "mean")
    with pytest.raises(TypeError):
       mmm.mmm(pd.DataFrame(data=({'col1': [1], 'col2': ['a']})),method = "median")
    with pytest.raises(TypeError):
       mmm.mmm(pd.DataFrame(data=({'col1': [1], 'col2': ['a']})),method = "mode")  
       
def test_more_missing():
    
    """
    Checks if array or dataframe columns have atleast 2 non-missing for imputing
    
   Mean, Mode, Median all need atleast two not null values to estimate missing
    """

    # dataframe with less than 2 non-missing
    
    # d = pd.DataFrame(data=({'col1': [1,None,None], 'col2': ['a',None,None]}))
    with pytest.raises(ValueError):
       mmm.mmm(pd.DataFrame(data=({'col1': [1,None,None], 'col2': ['a',None,None]})),method = "mean")
    with pytest.raises(ValueError):
       mmm.mmm(pd.DataFrame(data=({'col1': [1,None,None], 'col2': ['a',None,None]})),method = "median")
    with pytest.raises(ValueError):
       mmm.mmm(pd.DataFrame(data=({'col1': [1,None,None], 'col2': ['a',None,None]})),method ="mode")       
        
       
def test_method_check():
    
    """
    Error check if method in mmm is not in ("mean","median","mode")
    
    """
    
   # d = pd.DataFrame(data=({'col1': [1,2,None], 'col2': ['a',None,'c']}))
    
    with pytest.raises(Exception):
       mmm.mmm(['a','b'],method ="max")
    with pytest.raises(Exception):
       mmm.mmm(['a','b'],"")

       
def test_numeric_col() :
    
    """
    
    Checks if dataframe given to mean and median imputation has numeric column
    
    Mean and Median only work with numeric columns, dataframe with non-numeric columns should be invalid
    
    """
    
    #d = pd.DataFrame(data=({'col1': [True,False,None], 'col2': ['a',None,'c']}))
    #e = pd.DataFrame(data=({'col2': ['a',None,'c']}))
    
    with pytest.raises(Exception):
       mmm.mmm(pd.DataFrame(data=({'col1': [True,False,None], 'col2': ['a',None,'c']})),method = "mean")
    with pytest.raises(Exception):
       mmm.mmm(pd.DataFrame(data=({'col1': [True,False,None], 'col2': ['a',None,'c']})),method = "median")
       
    with pytest.raises(Exception):
       mmm.mmm(pd.DataFrame(data=({'col2': ['a',None,'c']})),method = "mean")
    with pytest.raises(Exception):
       mmm.mmm(pd.DataFrame(data=({'col2': ['a',None,'c']})),method = "median")
       
def test_outputs():
    
    """
    check if mmm return expected output
    
    """

    
    # check for mmm
    
    # df = pd.DataFrame(data=({'v_num': [4,np.nan,5,6,7,np.nan,9]}))
    # df2 = pd.DataFrame(data=({'v_char': ['one','two',None,'two','two','two']}))
    
   # mean_out = mmm.mmm(df,method="mean")
   # df_mean = pd.DataFrame(data=({'v_num': [4,6.2,5,6,7,6.2,9]}))
    assert np.array_equal(mean_out,df_mean)
    
   # med_out = mmm.mmm(df,method="median")
   # df_med = pd.DataFrame(data=({'v_num': [4,6,5,6,7,6,9]}))
    assert np.array_equal(med_out,df_med)
    
    #mod_out = mmm.mmm(df2,method="mode")
   # df_mod = pd.DataFrame(data=({'v_char': ['one','two','two','two','two','two']}))
    assert np.array_equal(mod_out,df_mod)
#    
    
    
    
    
    

