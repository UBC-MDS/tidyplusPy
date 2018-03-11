import pytest
import pandas as pd
import numpy as np
from tidyplusPy import typemix, cleanmix

# prepare samples
sample=pd.read_csv("data/test_sample.csv")
cleanmix_e1=pd.read_csv("data/cleanmix_e1.csv")
cleanmix_e2=sample.copy()
cleanmix_e2.iloc[3,0]=float('nan')

# check inputs
def test_input():
    """
    Tests incorrect/unacceptable input data.
    These should raise a type error/warning.
    check input data type and value
    """

    with pytest.raises(TypeError) as e_info:
        cleanmix(sample,column=[1,2],type="logical")
        raise TypeError('The input should be a list of data frames')   
    assert e_info.value.message == 'The input should be a list of data frames' 
    
    with pytest.warns(UserWarning) as record:
        cleanmix(typemix(sample),column=4,type="logical")
        warnings.warn("A column deos not have type mixture", UserWarning)
    assert record[0].message.args[0] == "A column deos not have type mixture"

    with pytest.warns(UserWarning) as record:
        cleanmix(typemix(sample),column=1,type="logical")
        warnings.warn("The column deos not have the data type", UserWarning)
    assert record[0].message.args[0] == "The column deos not have the data type"
    
    
# check the code accuracy
def test_output():
    '''
    Check if the function gives us expected results.
    '''
    assert cleanmix(typemix(sample),column=[1,2],type=['number','characyer']) is cleanmix_e1
    assert cleanmix(typemix(sample),column=1,type="number") is cleanmix_e2
    assert cleanmix(typemix(sample),column=1,type="character",keep=FALSE) is cleanmix_e2
    