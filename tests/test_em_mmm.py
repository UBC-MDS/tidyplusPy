#!/usr/bin/python

import numpy as np
import pytest
import pandas as pd
import tidyplusPy
from tidyplusPy import EM as em
from tidyplusPy import mmm as mmm

##dummy data for MMM
data = pd.DataFrame(data=({'v_num': [4.1,np.nan,12.2,11,3.4,1.6,3.3,5.5], 'v_char': ['one','two',None,'two','two','one','two','two']}))

col = list(data["v_num"])
dat = [1,2,3,np.nan]

##dummy data for EM
matrix= np.random.rand(5,5)
matrix[1,0] = np.nan
matrix[2,1] = np.nan
matrix[4,2] = np.nan
matrix[3,3] = np.nan
matrix[0,0] = np.nan

## Usage

mmm.mmm(data,method="mode")

em.em(matrix)

def test_input():
    """
    Tests incorrect/unacceptable input data for both em and mmm
    These should raise a type error.
    
    For EM datatype should be numpy nd array
    For mmm datatype should be pandas dataframe
    
    check data type
    """

## Check EM datatypes other than numpy nd.array
    with pytest.raises(TypeError):
        em.em('some string' )

    with pytest.raises(TypeError):
        em.em( False )

    with pytest.raises(TypeError):
        em.em( 2 )

    with pytest.raises(TypeError):
        em.em( (0, np.nan, 2) )
        
## Check MMM input other than pandas dataframe
        
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
        
def row_input():
    
    """
    Checks row input in nd array and dataframe
    
    nd array and dataframe need more than 1 rows to estimate missing
    
    """
    
    empty_array = np.array([])
    
    ## Array should have more than 1 row
    a = np.random.rand(1,3)
    a[0,0] = None
    a[0,2] = np.nan
    a[0,0] = np.nan
    
    with pytest.raises(ValueError):
       em.em( empty_array )
       
    with pytest.raises(ValueError):
       em.em(a)
       
     ## check if dataframe has more than 1 row
    d = pd.DataFrame(data=({'col1': [1], 'col2': ['a']}))
    with pytest.raises(ValueError):
       mmm.mmm(d,method = "mean")
    with pytest.raises(ValueError):
       mmm.mmm(d,method = "median")
    with pytest.raises(ValueError):
       mmm.mmm(d,method = "mode")  
       
def more_missing():
    
    """
    Checks if array or dataframe columns have atleast 2 non-missing for imputing
    
    EM, Mean, Mode, Median all need atleast two not null values to estimate missing
    """
    
    ## Array with less than 2 non - missing
    a = np.random.rand(2,5)
    a[0,0] = None
    a[0,2] = np.nan
    a[1,0] = np.nan

    with pytest.raises(ValueError):
       em.em(a)
   
    ## dataframe with less than 2 non-missing
    
    d = pd.DataFrame(data=({'col1': [1,None,None], 'col2': ['a',None,None]}))
    with pytest.raises(ValueError):
       mmm.mmm(d,method = "mean")
    with pytest.raises(ValueError):
       mmm.mmm(d,method = "median")
    with pytest.raises(ValueError):
       mmm.mmm(d,method ="mode")       
        
       
def method_check():
    
    """
    Error check if method in mmm is not in ("mean","median","mode")
    
    """
    
    d = pd.DataFrame(data=({'col1': [1,2,None], 'col2': ['a',None,'c']}))
    
    with pytest.raises(Exception):
       mmm.mmm(d,method ="max")
    with pytest.raises(Exception):
       mmm.mmm(d,"")
    with pytest.raises(Exception):
       mmm.mmm(d)   
    with pytest.raises(Exception):
       mmm.mmm(d,method = 1) 
       
def numeric_col() :
    
    """
    
    Checks if dataframe given to mean and median imputation has numeric column
    
    Mean and Median only work with numeric columns, dataframe with non-numeric columns should be invalid
    
    """
    
    d = pd.DataFrame(data=({'col1': [True,False,None], 'col2': ['a',None,'c']}))
    e = pd.DataFrame(data=({'col2': ['a',None,'c']}))
    
    with pytest.raises(Exception):
       mmm.mmm(d,method = "mean")
    with pytest.raises(Exception):
       mmm.mmm(d,method = "median")
       
    with pytest.raises(Exception):
       mmm.mmm(e,method = "mean")
    with pytest.raises(Exception):
       mmm.mmm(e,method = "median")
       
def outputs():
    
    """
    check if EM and mmm return expected output
    
    """
    
    
    ## check for EM
    a = np.array([[1, np.nan, 3], [4, 5, np.nan]])
    e = em.em(a)
    b = np.array([[1, 5, 3], [4, 5, 3]])
    
    assert np.array_equal(e,b)
    
    ## check for mmm
    
    df = pd.DataFrame(data=({'v_num': [4,np.nan,5,6,7,np.nan,9]}))
    df2 = pd.DataFrame(data=({'v_char': ['one','two',None,'two','two','two']}))
    
    mean_out = mmm.mmm(df,method="mean")
    df_mean = pd.DataFrame(data=({'v_num': [4,6.2,5,6,7,6.2,9]}))
    assert np.array_equal(mean_out,df_mean)
    
    med_out = mmm.mmm(df,method="median")
    df_med = pd.DataFrame(data=({'v_num': [4,6,5,6,7,6,9]}))
    assert np.array_equal(med_out,df_med)
    
    mod_out = mmm.mmm(df2,method="mode")
    df_mod = pd.DataFrame(data=({'v_char': ['one','two','two','two','two','two']}))
    assert np.array_equal(mod_out,df_mod)
    
    
    
    
    
    
    
    

    
    
     
            
    
    
    