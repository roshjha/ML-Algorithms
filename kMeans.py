import numpy as N
import math

k=2
Max_Iterations=100
DataSet = [[1.0, 1.0], [1.5, 2.0], [3.0, 4.0], [5.0, 7.0], [3.5, 5.0], [4.5, 5.0], [3.5, 4.5]]
DataSet=N.array(DataSet)
Cluster=N.zeros(len(DataSet))

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
def main():
    
    cx1, cy1, cx2, cy2=Init_Centroid()
    print cx1, cy1, cx2, cy2
    
    Cluster=N.zeros(len(DataSet))
    Init_Clusters(cx1, cy1, cx2, cy2)
    print Cluster
    
    Cluster=Assign_Clusters(cx1, cy1, cx2, cy2)
    print Cluster
    
    Cx1, Cy1 = find_Meanof(1)
    Cx2, Cy2 = find_Meanof(2)
    print Cx1, Cy1
    print Cx2, Cy2
    
    tempCluster=N.zeros(len(DataSet))
    for i in range(1, Max_Iterations):
        Cluster=Assign_Clusters(Cx1, Cy1, Cx2, Cy2)
        if is_SameCluster(tempCluster, Cluster):
            print i, "hello"
            break
        Cx1, Cy1 = find_Meanof(1)
        Cx2, Cy2 = find_Meanof(2)
        tempCluster=Cluster
    print Cluster
    
main()
