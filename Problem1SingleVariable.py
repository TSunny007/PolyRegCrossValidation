import math
import matplotlib as mpl

mpl.use('PDF')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from numpy import linalg as LA
from numpy import polyval
from scipy import polyfit
import random

#You can adjust your column names by tinkering with the names array
df = pd.read_csv('D3.csv', names = ['x0','x1','x2','y'])
# x0 is the only explanatory variable needed for this regression
xColumn = df['x0']
# the fourth column
yColumn = df['y']

######### used for Cross validation
def CalculateSSE(xTrain,yTrain,xE,yE,p,Sum): 
    coefs = sp.polyfit(xTrain,yTrain,p)
    ffit = np.poly1d(coefs)
    resid = ffit(xE)
    RMSE = LA.norm(resid-yE)
    SSE = RMSE * RMSE
    Sum.append(SSE)

p_vals = [1,2,3,4,5]#These are the degrees of regression we are interested in fitting to our data
for r in p_vals: 
    Sum = []
    # we will try each regression 50 times with random texting (10 entries~ 10.2% of data) 
    # and training data (88 entries~ 89.8% of data) 
    for i in range(0, 50):
        xTrain = []
        yTrain = []
        xTest = []
        yTest = []
        rands = set()
        while len(rands) < 10:
            # The 98 here is needs to be changed based on data becasue the provided data has only 
            # 98 data points
            newRand = random.randint(0,98)
            # shouldn't have repitions of data...
            if newRand not in rands:
                rands.add(newRand)
        randsCopy = rands.copy()
        # This is going to destry the rands object in order to fill our test data.
        # that is why we have a copy of the rands object
        for x in range(0, 10, 1):
            d = rands.pop()
            xTest.append(xColumn[d])
            yTest.append(yColumn[d])
        # Now we iterate through our entire data and check that we don't have any of our test data 
        # in our training data.
        for x in range(0, len(xColumn), 1):
            if x not in randsCopy:
                xTrain.append(xColumn[x])
                yTrain.append(yColumn[x])
        # This method as of now calculates the sum of error. The formula can easily be changed
        # to accomodate residual or logistical difference.
        CalculateSSE(np.asarray(xTrain),np.asarray(yTrain), 
        np.asarray(xTest), np.asarray(yTest), r, Sum) 
    # Prints the average SSE by averaging every run's SSE
    print("the average sum of square error for degree %s is  %s " 
    %(r,sum(Sum) / float(len(Sum))))
            