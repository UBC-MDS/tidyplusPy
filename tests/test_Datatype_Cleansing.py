import pytest
import pandas as pd
import numpy as np
from tidyplusPy import typemix, cleanmix

# prepare samples
# for typemix function
sample=pd.read_csv("data/test_sample.csv")
typemix_output2=read.csv("data/typemix_output2.csv")
typemix_output3=read.csv("data/typemix_output3.csv")
# for cleanmix function
cleanmix_e1=pd.read_csv("data/cleanmix_e1.csv")
cleanmix_e2=read.csv("data/cleanmix_e2.csv")
cleanmix_e3=read.csv("data/cleanmix_e3.csv")

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
 

 
# check cleanmix:
# check inputs
def test_input():
    """
    Tests incorrect/unacceptable input data.
    These should raise a type error/warning.
    check input data type and value
    """

    with pytest.raises(TypeError) as e_info:
        cleanmix(sample,column=[1,2],type,keep)
        raise TypeError('The input should be a list of data frames')   
    assert e_info.value.message == 'The input should be a list of data frames' 
    
    with pytest.warns(UserWarning) as record:
        cleanmix(typemix(sample),column=[1,4],type,keep)
        warnings.warn("A column deos not have type mixture", UserWarning)
    assert record[0].message.args[0] == "A column deos not have type mixture"

    with pytest.warns(UserWarning) as record:
        cleanmix(typemix(sample),column=[1],type="logical",keep)
        warnings.warn("The column deos not have the data type", UserWarning)
    assert record[0].message.args[0] == "The column deos not have the data type"
    
    
# check the code accuracy
def test_output():
    '''
    Check if the function gives us expected results.
    '''
    assert cleanmix(typemix(sample),column=[1,2],type,keep) is cleanmix_e1
    assert cleanmix(typemix(sample),column=[1,2],type="number",keep) is cleanmix_e2
    assert cleanmix(typemix(sample),column=[1,2],type="character",keep=FALSE) is cleanmix_e3
    
