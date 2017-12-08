import pandas as pd
import sys
import numpy as np
from SimilarityMeasures import SimilarityMeasures
def recommend(ind,row):
    print(data[ind][0])
    for i in range(1, row):
        if (int(data[ind][i]) >= 3 and int(data[1][i] == 0)):
            print(data[0][i])


data = pd.read_csv('Movie_Ratings.csv', header=None)
data = data.replace(np.nan, 0)
try:

    col = len(data[0])
    row = len(list(data))
    # ind=manhatten(col,row)
    k=SimilarityMeasures()
    dis=k.cosineSimilarity(data,1)
    print(dis)
    #distance=k.manhattenDistance(1,data)
    #print(distance)
    # k.pearsonCorrelation_k_nearest(data)
    # k.pearson_correlation_k_nearest(row, col, data)
    # ind=cosine_similarity(row,col)
    # print(data[ind][0])
    # recommend(ind,row)
except KeyError:
    print("keyError")
