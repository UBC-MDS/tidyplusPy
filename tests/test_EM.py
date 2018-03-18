#!/usr/bin/env python

import numpy as np
import pytest
import pandas as pd
import tidyplusPy
from tidyplusPy import EM as em


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

empty_array = np.array([])

# Array should have more than 1 row
a = np.random.rand(1,3)
a[0,0] = None
a[0,2] = np.nan
a[0,0] = np.nan



a1 = np.random.rand(2,5)
a1[0,0] = None
a1[0,2] = np.nan
a1[1,0] = np.nan


a2 = np.array([[1, np.nan, 3], [4, 5, np.nan]])
e = em.em(a2)
b = np.array([[1, 5, 3], [4, 5, 3]])





def test_input():
    """
    Tests incorrect/unacceptable input data for both em 
    These should raise a type error.
    
    For EM datatype should be numpy nd array

    
    check data type
    """

    # Check EM datatypes other than numpy nd.array
    with pytest.raises(TypeError):
        em.em('some string')


    with pytest.raises(TypeError):
        em.em(2)

    with pytest.raises(TypeError):
        em.em(False)

    with pytest.raises(TypeError):
        em.em((0, np.nan, 2))
        

        
def test_row_input():
    
    """
    Checks row input in nd array and dataframe
    
    nd array need more than 1 rows to estimate missing
    
    """
    

    
    with pytest.raises(TypeError):
       em.em(a)
       

       

def test_more_missing():
    
    """
    Checks if array columns have atleast 2 non-missing for imputing
    
    EMneed atleast two not null values to estimate missing
    """
    
    # Array with less than 2 non - missing

    with pytest.raises(ValueError):
       em.em(a1)
   

       

       
def test_outputs():
    
    """
    check if EM return expected output
    
    """
    
    
    # check for EM

    
    assert np.array_equal(e,b)
