import pytest
import numpy as np
import pandas as pd
#from tidyplus import em
import em


    # Input Errors:

    def test_input_as_dataframe(self):
        with pytest.raises(TypeError('`data` must be a dataframe.')):
            summary_cv(data = pd.DataFrame(data={'a' :[1,2,3],'b' :['a','b','']}))


    # Output Errors


    def test_as_dataframe(self):
        assert isinstance(data, np.dataframe)

