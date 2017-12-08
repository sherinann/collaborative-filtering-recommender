#collaborative filtering to find out who has most similar preferences in movies to user 1 using manhatten distance

import pandas as pd
import sys
import numpy as np
import Models
class SimilarityMeasures:

    def getRow(self,data):
        return len(list(data))

    def getColoumn(self,data):
        return len(data[0])

    def manhattenDistance(col,row,data):
        val = sys.maxsize
        for j in range(2,col):
            s = 0
            for i in range(1,row):
                if(int(data[1][i])==0 or int(data[j][i])==0):
                    continue
                s=s+abs(int(data[1][i])-int(data[j][i]))
            if s<val:
                val=s
                ind=j
        return ind

    def pearsonCorrelation_k_nearest(row,col,data):
        #3 neighbours
        arr=[]
        r1={}
        for j in range(2,col):
            p1 = 0
            count = 0
            p2 = 0
            p3 = 0
            p5 = 0
            p6 = 0
            for i in range(1,row):
                if (int(data[1][i]) == 0 or int(data[j][i]) == 0):
                    continue
                p1=p1+int(data[1][i])*int(data[j][i])
                count=count+1
                p2=int(p2+int(data[1][i]))
                p3=int(p3+int(data[j][i]))
                p5 = int(p5 + int(data[1][i]) * int(data[1][i]))
                p6 = int(p6 + int(data[j][i]) * int(data[j][i]))
            if count>0:
                p4=p2*p3/count
                p1=p1-p4
                p2=p2*p2/count
                p3=p3*p3/count
                k1=np.sqrt(p5-p2)
                k2=np.sqrt(p6-p3)
                r=p1/(k1*k2)
                if  len(arr)>=3 :
                    if r>arr[2]:
                        arr.append(r)
                        r1.update({r:j})
                        arr.sort(reverse=True)
                        arr.pop()
                else:
                    arr.append(r)
                    r1.update({r:j})
                    arr.sort(reverse=True)
        sum=arr[0]+arr[1]+arr[2]
        k1=arr[0]/sum
        k2=arr[1]/sum
        k3=arr[2]/sum
        Models.k_near_recommend(k1,k2,k3,r1[arr[0]],r1[arr[1]],r1[arr[2]],row)
        return



    def cosineSimilarity(row,col,data):
        r1=-1
        for j in range(2,col):
            xy=0
            x1=0
            y1=0
            for i in range(1,row):
                xy=xy+int(data[1][i])*int(data[j][i])
                x1=x1+int(data[1][i])*int(data[1][i])
                y1=y1+int(data[j][i])*int(data[j][i])
            r=xy/(np.sqrt(x1)*np.sqrt(y1))
            if r>r1:
                r1=r
                ind=j
        return ind




