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


def hierachy_bottom_up(data, classes, curr_k, k=2, ): #data is a dataframe
    print(classes)
    labels = np.zeros(len(data), dtype=int)
    if len(classes)==k:

        count = 0
        for c in classes:
            for i in c:
                labels[i - 1] = count
            count += 1
        print(labels)
        return labels

    # 计算每个类的均值：
    centroids = [get_centroid(data, classes[i]) for i in range(curr_k)]
    dis_mat = [[]]
    min_dis = 99999
    min_ix = [0,0] #存储下标
    for i in range(len(centroids)-1):
        for j in range(i+1,len(centroids)):
            curr_dis = utils.distance(centroids[i], centroids[j])
            if curr_dis<min_dis:
                min_dis=curr_dis
                min_ix=[i,j]
    classes[min_ix[0]].extend(classes[min_ix[1]])
    del classes[min_ix[1]]
    err_sum = 0
    # for c in range(k):
    #     for y in classes[c]:
    #         err_sum += utils.distance(data.ix[y], centroids[c])
    # print("err_sum" + "\t" + str(err_sum))
    hierachy_bottom_up(data, classes, curr_k - 1, k)

def hierachy_top_down(data, k=2, ): #data is a dataframe
    max_dis = 99999
    max_ix = [0, 0]  # 存储下标
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            curr_dis = utils.distance(data.loc[i+1,:], data.loc[j+1,:])
            if curr_dis < max_dis:
                max_dis = curr_dis
                max_ix = [i, j]
    labels = np.zeros(len(data),dtype=int)
    labels[max_ix[0]]=0
    labels[max_ix[1]]=1
    print(max_ix)
    for i in range(len(data)):
        if i!=max_ix[0] and i!=max_ix[1]:
            print(i)
            if utils.distance(data.loc[i+1,:],data.loc[max_ix[0]+1,:])<utils.distance(data.loc[i+1,:],data.loc[max_ix[1]+1,:]):
                labels[i]=0
            else:
                labels[i]=1
    return labels


if __name__ == '__main__':
    data, label = utils.load_data()

    classes = [[i] for i in range(1,len(data)+1)]
    # plabels = hierachy_bottom_up(data, classes, len(classes), 2)
    plabels = hierachy_top_down(data,2)

    plabels = np.array(plabels)
    print(np.array(label))
    acc1 = accuracy_score(label, plabels)
    acc2 = accuracy_score(label, 1 - plabels)
    acc = acc1 if acc1 > acc2 else acc2
    print("acc = " + str(acc))
