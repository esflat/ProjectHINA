# XX01 : データ同士の距離
# 
# データマイイニングでは、データ同士の距離を使い、データ同士の似ている度合いを測ります

import numpy as np
import scipy as sp
from scipy.stats import pearsonr

def euclidean_distance(x,y):
    return np.linalg.norm(x-y)

def pearsonr_distance(x,y):
    return pearsonr(x,y)
    
def tanimoto_distance(x,y):
    c = [v for v in x if v in y]
    return float(len(c))/(len(x)+len(y)-len(c))

x = np.array([1,2])
y = np.array([2,3])
print(euclidean_distance(x,y))
print(pearsonr_distance(x,y))
print(tanimoto_distance(x,y))