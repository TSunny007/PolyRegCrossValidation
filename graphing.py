import pandas as pd
import numpy as np
import scipy.spatial
import random
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(precision=3)

sns.set_style("darkgrid")
plt.plot(np.array([1,2,3,4,5,6,7,8,9,10]), 
np.array([ 0.0024, 0.00072,0.00061,0.00063,0.00061,0.00065, 0.00062, 0.00066, 0.00065, 0.00070]))
plt.title("Comparision of SSE vs degrees of regression on dataset D3.csv")
plt.xlabel("Degree")
plt.ylabel("SSE")
plt.ylim([0,0.0025])
plt.xlim([0,5.5])
plt.show()
            