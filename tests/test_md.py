#!/usr/bin/env python

import pytest
from tidyplusPy import md

class Test_md:

	def test_input1(self):
		"""
		Raise TypeError if ncol and nrow are not integer
	    """
		with pytest.raises(TypeError):
			md.md_new( ncol = 'some string', nrow = 3 )
		with pytest.raises(TypeError):
			md.md_new( ncol = 3, nrow = 'some string' )

	def test_input2(self):
		"""
		Raise InputError if ncol and nrow are not positive
	    """
		with pytest.raises(Exception):
			md.md_new(-1,-1)

	def test_input3(self):
		"""
		Raise TypeError if align is not a string
		"""
		with pytest.raises(TypeError):
			md.md_new(align = False)
		with pytest.raises(TypeError):
			md.md_new(align = 2)
		with pytest.raises(TypeError):
			md.md_new(align = ["d","r"])

	def test_input4(self):
		"""
		Raise InputError if 'align' is none of 'l', 'c', or 'r'
		"""
		with pytest.raises(Exception):
			md.md_new(align = "q")

	def test_input5(self):
		"""
		Raise InputError if len(align) !=1
		"""
		with pytest.raises(Exception):
			md.md_new(align = "rrr")

	def test_input6(self):
		"""
		Raise TypeError if header is not a list
		"""
		with pytest.raises(TypeError):
			md.md_new(header = "df")
		with pytest.raises(TypeError):
			md.md_new(header = (1,2,3))

	def test_input7(self):
		"""
		Raise TypeError if the element of header is not a strings
		"""
		with pytest.raises(TypeError):
			md.md_new(header = ["df",123,True])

	def test_input8(self):
		"""
		Raise InputError if 'len(header) != ncol'
		"""
		with pytest.raises(Exception):
			md.md_new(ncol = 5, header = ['foo','boo','laa'])

	# Output errors
	def test_output1(self):
		"""
		Test if md_new() give  correct result
		"""
		assert md.md_new() == '|    |    |\n|:---|:---|\n|    |    |\n|    |    |' # a printed markdown source code will also be printed out

	def test_output2(self):
		"""
		Test if md_new() give  correct result
		"""
		assert md.md_new(3,3) == '|    |    |    |\n|:---|:---|:---|\n|    |    |    |\n|    |    |    |\n|    |    |    |'

	def test_output3(self):
		"""
		Test if md_new() give  correct result
		"""
		assert md.md_new(3,3, align= "c") == '|    |    |    |\n|:--:|:--:|:--:|\n|    |    |    |\n|    |    |    |\n|    |    |    |'

	def test_output4(self):
		"""
		Test if md_new() give  correct result
		"""
		assert md.md_new(align ="c", header = ["foo","boo"]) == '| foo| boo|\n|:--:|:--:|\n|    |    |\n|    |    |'
