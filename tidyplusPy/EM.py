#!/usr/bin/env python

import numpy as np
# import pandas as pd
import random


def em(data):
    """ Imputes data using expectation maximization.
    E-step: Calculates the expected value of missing data  based on log likelihood ratio.
    M-step: Finds the parameters that maximize the log likelihood function

    @param
      data: numpy.nd.array : Data to impute.
      loops: int : Number of em iterations to run before breaking.
      Returns : numpy.nd.array, Imputed data.
      
    Attribution : https://github.com/eltonlaw/impyute
    
    @example :
        ## dummy data
        
         matrix= np.random.rand(5,4)
         matrix[1,0] = np.nan
         matrix[2,1] = np.nan
         matrix[4,2] = np.nan
         matrix[3,3] = np.nan
        
         
        ## Usage
        
        em(matrix,loops = 20)
        
    """
    if type(data) is not np.ndarray :
        raise TypeError('datatype for input data can only be numpy.ndarray')
    if  data.shape[0] < 2 :
        raise TypeError('array should have more than one row')
    for i in range(0,data.shape[1]):
        if np.count_nonzero(~np.isnan(data[:,i])) < 1:
            raise ValueError('array should have atleast two not-null value in each column')
    while len(np.argwhere(np.isnan(data))) > 0: # run this step to update all columns in the matrix
        em_run(data)
    return data


def em_run(data, loops=20):
    """ Utility function for em
    
    E-step: Calculates the expected value of missing data  based on log likelihood ratio.
    M-step: Finds the parameters that maximize the log likelihood function

    @param
      data: numpy.nd.array : Data to impute.
      loops: int : Number of em iterations to run before breaking.
    
    Runs em function in loop mnetioned by the user
    
    See em documentations as help(em)
    

        
    """
    null_xy = np.argwhere(np.isnan(data)) # check indices of all missing value
    for x_i, y_i in null_xy:
        col = data[:, int(y_i)]
        mu = col[~np.isnan(col)].mean() # get col means
        std = col[~np.isnan(col)].std() # get col standard deviation
        col[x_i] = random.gauss(mu, std) # create gaussian distribution of mu and std
        previous, i = 1, 1
        for i in range(loops):
            # Expectation
            mu = col[~np.isnan(col)].mean()
            std = col[~np.isnan(col)].std()
            # Maximization
            col[x_i] = random.gauss(mu, std) # update parameters to maximize
            delta = (col[x_i]-previous)/previous  # record change in parameters
            if i > 5 and delta < 0.1:
                data[x_i][y_i] = col[x_i]
                break  # break when likelihood doesn't change at least 10%
            data[x_i][y_i] = col[x_i]
            previous = col[x_i]
        return data
    else:
        raise Exception("Other dtypes not supported yet.")
    


