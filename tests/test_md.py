import pytest
import tidyplusPy.md
import numpy as np
import pandas as pd
import sklearn.datasets.iris_load
from sklearn.linear_model import LinearRegression


# Input errors
def test_input():
	"""
 	Tests incorrect/unacceptable input data.
    	These should raise a type error.
    	check data type
    	"""
	# md_data
	with pytest.raises(TypeError):
        md.md_data( data = 'some string' )

   	 with pytest.raises(TypeError):
        md.md_data( data = False )

    	with pytest.raises(TypeError):
        md.md_data( data = 2 )

    	with pytest.raises(TypeError):
        md.md_data( data = np.array([0, np.nan, 2]) )
	
	# md_new
	with pytest.raises(TypeError):
        md.md_new( ncol = 'some string', nrow = 'some string' )

   	with pytest.raises(TypeError):
        md.md_new( ncol = False, nrow = True )

    	with pytest.raises(TypeError):
        md.md_new( ncol = np.array([0, np.nan, 2]), nrow = np.array([3,2,1]) )
	
	# md_reg
	with pytest.raises(TypeError):
        md.md_reg( x = 'some string' )

    	with pytest.raises(TypeError):
        md.md_reg( x = False )

    	with pytest.raises(TypeError):
        md.md_reg( x = 2 )

    	with pytest.raises(TypeError):
        md.md_reg( x = np.array([0, np.nan, 2]) )


# Output errors
def test_output()
	df = load_iris()
	lr = LinearRegression()
	lr.fit(df['Sepal.Width'], df['Sepal.Length'])
	assert (md.md_new(ncol = 2, nrow = 2) == "|   |   |
                             			  |:--|:--|
                               			  |   |   |
                             			  |   |   |") 
	assert (md.md_data(data = head(iris) == 
"| Sepal.Length| Sepal.Width| Petal.Length| Petal.Width|Species |
|------------:|-----------:|------------:|-----------:|:-------|
|          5.1|         3.5|          1.4|         0.2|setosa  |
|          4.9|         3.0|          1.4|         0.2|setosa  |
|          4.7|         3.2|          1.3|         0.2|setosa  |
|          4.6|         3.1|          1.5|         0.2|setosa  |
|          5.0|         3.6|          1.4|         0.2|setosa  |
|          5.4|         3.9|          1.7|         0.4|setosa  |")

	assert (md.md_reg(lr ,type = "weight") == "
	            |term        |   estimate| 
                    |-----------:|:----------|
                    |w0          |  6.5262226|
                    |w1          | -0.2233611|")
