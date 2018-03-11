import pytest
import pandas as pd
import numpy as np
from tidyplusPy import typemix

# prepare samples
# for typemix function
sample=pd.read_csv("data/test_sample.csv")
typemix_output2=pd.read_csv("data/typemix_output2.csv")
typemix_output3=pd.read_csv("data/typemix_output3.csv")

# check typemix:
# check inputs
def test_input():
    """
    Tests incorrect/unacceptable input data.
    These should raise a type error.
    check input data type
    """

    with pytest.raises(TypeError) as e_info:
        typemix(df = [1,2,3,"do"])
        raise TypeError('The input should be a data frame')   
    assert e_info.value.message == 'The input should be a data frame' 

    with pytest.raises(TypeError) as e_info:
        typemix(df = np.array([1,2,3,"do"]))
        raise TypeError('The input should be a data frame')   
    assert e_info.value.message == 'The input should be a data frame' 
        
    with pytest.raises(TypeError) as e_info:
        typemix(df = np.matrix([1,2,3,"do"]))
        raise TypeError('The input should be a data frame')   
    assert e_info.value.message == 'The input should be a data frame' 

# check the code accuracy
def test_output():
    '''
    Check if the function gives us expected results.
    '''
    assert typemix(sample)[1] is sample
    assert typemix(sample)[2] is typemix_output2
    assert typemix(sample)[3] is typemix_output3
 