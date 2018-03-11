import numpy as np
import pytest
import pandas as pd

d = {'v_num': [4.1,np.nan,12.2,11,3.4,1.6,3.3,5.5], 'v_char': ['one','two','','two','two','one','two','two']}
data = pd.DataFrame(data=d)
col = list(data["v_num"])
def test_input():
    """
    Tests incorrect/unacceptable input data.
    These should raise a type error.
    check data type
    """

    with pytest.raises(TypeError):
        mmm( data = 'some string' )

    with pytest.raises(TypeError):
        mmm( data = False )

    with pytest.raises(TypeError):
        mmm( data = 2 )

    with pytest.raises(TypeError):
        mmm( data = np.array([0, np.nan, 2]) )


def missings():
    """
    Check the missing values
    These should raise a value error.
    """

    empty_array = np.array([])

    with pytest.raises(ValueError):
        mmm( data = empty_array )
        
    
    assert isinstance(data, pd.DataFrame)
    assert isinstance(list(data["v_num"]),list)
    assert isinstance(data.v_char[1],str)
    assert sum(data.v_num.isnull()) > 0
    assert sum(data.v_char=='') > 0

#### New tests


### Check for inputes for both MMM
    
def mmm_df_match():
    with pytest.raises(TypeError("Input for MMM can only be dataframe")):
        mmm(dat, method= "mean")
        
def check_method():
    with pytest.raises(TypeError("Method can only be mean, median or mode")):
        mmm(data, method= "max")
    
    


