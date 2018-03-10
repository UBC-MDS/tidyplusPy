""" tidyplusPy.md"""

def md_new(ncol = 2, nrow = 2, align = NULL, header = NA):
	'''
	Creates a bare bone for generating a markdown table. Alignments and size of the table can be input by users.
	
	Parameters:
		ncol, nrow : the number of columns and row for the markdown table
		align	   : Column alignment: a character vector consisting of 'l' (left), 'c' (center) and/or 'r' (right). If align = 'l', all columns are left aligned. e.t.c.
		header	   : A character vector of length = ncol to be used for the header of the table. Default NA.
	Return: 
		a string of the markdown source code
	
	'''


def md_data(data, row.index = NA, col.index = NA, row.names = NA, header = NA, align = NULL)
	'''	
	Converts a pandas.DataFrame or matrix into a markdown table format.
	
	Parameters:
		data: a pandas dataframe
		row.index,col.index: A numeric vector correspond to the index position of the rows/columns to be included. By default, all columns and rows are included.
		header: A string of length = ncol to be used for the header of the table. If provided, the original header will be replaced.
		align : column alignment: a string consisting of 'l' (left), 'c' (center) and/or 'r' (right). By default or if align = NULL, numeric columns are right-aligned, and other columns are left-aligned. If align = 'l', all columns are left aligned. e.t.c.
	Return: 
		a string of the markdown source code
	'''

def md_reg(x, type = "weight")
	'''
	Converts a regression model result into a nice-formatted markdown table.
	
	Parameters:
		x: a regression model class from sklearn
		type: the type of output 
			- weight: the parameters/weights of the model
			- fit : the score of the model
	Return: 
		a string of the markdown source code
	'''
