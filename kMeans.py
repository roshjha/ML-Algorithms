import numpy as N
import math
import pandas as P


def Euclidean_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))

def Init_Centroid():
    cx1=DataSet[0][0]
    cy1=DataSet[0][1]
    cx2=DataSet[len(DataSet)/2][0]
    cy2=DataSet[len(DataSet)/2][1]
    
    return cx1, cy1, cx2, cy2

def Init_Clusters(cx1, cy1, cx2, cy2):
    for i in range(0, len(DataSet)):
        if DataSet[i][0]==cx1 and DataSet[i][1]==cy1:
            Cluster[i]=1
        elif DataSet[i][0]==cx2 and DataSet[i][1]==cy2:
            Cluster[i]=2          
    return 

def Assign_Clusters(cx1, cy1, cx2, cy2):
    for i in range(0, len(DataSet)):
        if (DataSet[i][0]!=cx1 and DataSet[i][1]!=cy1) or (DataSet[i][0]!=cx2 and DataSet[i][1]!=cy2):
            d_from1=Euclidean_distance(DataSet[i][0], DataSet[i][1], cx1, cy1)
            d_from2=Euclidean_distance(DataSet[i][0], DataSet[i][1], cx2, cy2)
            if d_from1<=d_from2:
                Cluster[i]=1
            else:
                Cluster[i]=2
    return Cluster

def find_Meanof(Cluster_k):
    count_Cluster=0
    Sumx, Sumy=0, 0
    for i in range(0, len(DataSet)):
        if Cluster[i]==Cluster_k:
            Sumx+=DataSet[i][0]
            Sumy+=DataSet[i][1]
            count_Cluster+=1
    Sumx/=count_Cluster
    Sumy/=count_Cluster
    return Sumx, Sumy

def is_SameCluster(Cluster1, Cluster2):
    if N.array_equal(Cluster1, Cluster2):
        return True
    else:
        return False
    
def Print_Clusters():
    for i in range (0, len(DataSet)): 
        print DataSet[i], "---->", int(Cluster[i])
        
def Main():
    #print DataSet
    cx1, cy1, cx2, cy2=Init_Centroid()
    #print cx1, cy1, cx2, cy2
    
    Cluster=N.zeros(len(DataSet))
    Init_Clusters(cx1, cy1, cx2, cy2)
    #print Cluster
    
    Cluster=Assign_Clusters(cx1, cy1, cx2, cy2)
    #print Cluster
    
    Cx1, Cy1 = find_Meanof(1)
    Cx2, Cy2 = find_Meanof(2)
    #print Cx1, Cy1
    #print Cx2, Cy2
    
    tempCluster=N.zeros(len(DataSet))
    for i in range(1, Max_Iterations):
        Cluster=Assign_Clusters(Cx1, Cy1, Cx2, Cy2)
        if is_SameCluster(tempCluster, Cluster):
            break
        Cx1, Cy1 = find_Meanof(1)
        Cx2, Cy2 = find_Meanof(2)
        tempCluster=Cluster
    #print Cluster
    Print_Clusters()
    
def Read_Input():
    
    df=P.read_table('inputKmeans.txt', delim_whitespace=True, header=None)
    df=df[[1, 2]] #Skip first Column
    DataSet=N.zeros(df.shape)
    
    for i, row in df.iterrows():
        DataSet[i]=[row[1], row[2]]
        #print row[1], row[2]
    return DataSet

DataSet=Read_Input()
Cluster=N.zeros(len(DataSet))

k=2
Max_Iterations=100

Main()
