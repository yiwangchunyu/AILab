import numpy as np
import pandas as pd
import random

from sklearn.metrics import accuracy_score

import utils
import pyprind

PARAMETER_K=2

def get_centroid(data, points):
    df = data.loc[points,:]
    mean = df.mean()
    return np.array(mean)


def kmeans(data,k=2): #data is a dataframe
    classes=[]
    #初始化
    randdiff = random.sample(range(1,len(data)+1),k)
    classes = [[randdiff[i]] for i in range(k)]
    # 将其他数据分类
    for i in range(1,len(data)+1):
        # 计算每个类的均值：
        centroids = [get_centroid(data, classes[i]) for i in range(k)]
        class_flat = []
        for x in classes:
            class_flat.extend(x)

        if i not in class_flat:
            min = 0
            mindis=9999
            for index, centroid in enumerate(centroids):
                dis  = utils.distance(data.ix[i].values, centroid)
                if dis<mindis:
                    mindis=dis
                    min=index
            classes[min].append(i)
    for c in classes:
        c.sort()
    print(classes)

    #调整

    n=100
    bar = pyprind.ProgPercent(n)
    while n>0:
        #连续迭代N次;
        err_list=[]
        #对于每个样本，计算要不要交换
        for i in range(1,len(data)+1):

            #计算每个类的均值：
            centroids = [get_centroid(data, classes[i]) for i in range(k)]
            #计算误差平方和：
            err_sum=0
            for c in range(k):
                for y in classes[c]:
                    err_sum+=utils.distance(data.ix[y],centroids[c])
            print("err_sum"+"\t"+str(err_sum))
            err_list.append(err_sum)

            curr_label = -1
            for index, points in enumerate(classes):
                if i in points:
                    curr_label = index
                    break
            if len(classes[curr_label])==1: continue

            pi = len(classes[curr_label])/(len(classes[curr_label])+1)*utils.distance(data.ix[i], centroids[curr_label])
            bestj = -1
            for j in range(k):
                if j!=curr_label:
                    pj = len(classes[j])/(len(classes[j])+1)*utils.distance(data.ix[i], centroids[j])
                    if pj<=pi:
                        bestj = j
            #print(bestj)
            if bestj!=-1:
                classes[curr_label].remove(i)
                classes[bestj].append(i)

        if np.array(err_list).var()<=0.0000000000001:
            break
        n-=1
        bar.update()
    for c in classes:
        c.sort()
    print(classes)

    labels = [0 for i in range(len(data))]
    count=0
    for c in classes:
        for i in c:
            labels[i-1]=count
        count+=1
    return labels




if __name__ == '__main__':
    data, label = utils.load_data()
    #kmeans(data,2)
    #print(get_centroid(data,[1,2,3,4,5]))
    k_labels = kmeans(data,2)
    print(k_labels)
    acc = accuracy_score(label,k_labels)
    print("acc = "+str(acc))
