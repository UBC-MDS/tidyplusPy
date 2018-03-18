#!/usr/bin/env python

import pytest
import pandas as pd
import numpy as np
import os
from tidyplusPy.typemix import typemix
from tidyplusPy.cleanmix import cleanmix

# prepare samples
fname = os.path.join(os.path.dirname(__file__), 'data/test_sample.csv')
sample=pd.read_csv(fname)
fname = os.path.join(os.path.dirname(__file__), 'data/cleanmix_e1.csv')
cleanmix_e1=pd.read_csv(fname)
cleanmix_e1.iloc[3,0]=float('nan')
cleanmix_e2=sample.copy()
cleanmix_e2.iloc[3,0]=float('nan')
result=typemix(sample)

# check inputs
def test_input():
    """
    Tests incorrect/unacceptable input data.
    These should raise a type error/warning.
    check input data type and value
    """

    with pytest.raises(TypeError):
        cleanmix(sample,column=[1,2],type="logical")
    
    with pytest.warns(UserWarning):
        cleanmix(result,column=4,type="logical")

    with pytest.warns(UserWarning):
        cleanmix(result,column=0,type="logical")

    with pytest.warns(UserWarning):
        cleanmix(result,column=[4],type=["logical"])
    
    with pytest.warns(UserWarning):
        cleanmix(result,column=[0],type=["logical"])

    
# check the code accuracy
def test_output():
    '''
    Check if the function gives us expected results.
    '''
    assert pd.DataFrame.equals(cleanmix(result,column=[0,1],type=['number','character']), cleanmix_e1)
    assert pd.DataFrame.equals(cleanmix(result,column=0,type="number"), cleanmix_e2)
    assert pd.DataFrame.equals(cleanmix(result,column=0,type="character",keep=False), cleanmix_e2)
    assert pd.DataFrame.equals(cleanmix(result,column=[0],type=["character"],keep=False), cleanmix_e2)

    
