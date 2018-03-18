#!/usr/bin/env python

import pytest
import pandas as pd
import numpy as np
import os
from tidyplusPy.typemix import typemix

# prepare samples
# for typemix function
fname = os.path.join(os.path.dirname(__file__), 'data/test_sample.csv')
sample=pd.read_csv(fname)
fname = os.path.join(os.path.dirname(__file__), "data/typemix_output2.csv")
typemix_output2=pd.read_csv(fname)
fname = os.path.join(os.path.dirname(__file__), "data/typemix_output3.csv")
typemix_output3=pd.read_csv(fname)

# check typemix:
# check inputs
def test_input():
    """
    Tests incorrect/unacceptable input data.
    These should raise a type error.
    check input data type
    """
    with pytest.raises(TypeError):
        typemix(df = [1,2,3,"do"])
        
    with pytest.raises(TypeError):
        typemix(df = np.array([1,2,3,"do"]))
        
    with pytest.raises(TypeError):
        typemix(df = np.matrix([1,2,3,"do"]))

# check the code accuracy
def test_output():
    '''
    Check if the function gives us expected results.
    '''
    assert typemix(sample)[0] is sample
    assert pd.DataFrame.equals(typemix_output2, typemix(sample)[1])
    assert pd.DataFrame.equals(typemix(sample)[2], typemix_output3)
