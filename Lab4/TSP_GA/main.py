from TravelingSalesman import *
import data_handler
import utils
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd
def parameter_selection(data):
    res = []
    mating_rate=0.8
    variation_rate=0.1
    N=10
    n=100
    #bar = pyprind.ProgBar(19)
    f = open('data/performence.csv','w+')
    f.write('mating_rate,variation_rate,N,performance,time\n')
    for N in range(10,200,5):
        start = time.time()
        ts = TravelingSalesman(data, N, mating_rate, variation_rate)
        ts.travel_start(n)
        distance = utils.get_distance_all(ts.ga.best_life.chromosome, data)
        end = time.time()
        res.append([mating_rate, variation_rate, N, distance])
        f.write(str(mating_rate) + ',' + str(variation_rate) + ',' + str(N) + ',' + str(distance) +',' + str(end-start) +  '\n')
        #bar.update()
    f.close()
    return res
if __name__ == '__main__':
    #群体规模N
    N=25
    #交配概率
    mating_rate = 0.8
    #变异概率
    variation_rate = 0.1
    #加载数据
    data = data_handler.load_data('data/cn144_location2.txt')

    ts = TravelingSalesman(data, N, mating_rate, variation_rate)

    ts.travel_start(200000)

    print('result:')
    sequence = ts.ga.best_life.chromosome
    print(sequence)
    distance = utils.get_distance_all(ts.ga.best_life.chromosome, data)
    print(distance)
    data_handler.draw_path(sequence, data)


    # res = parameter_selection(data)
    # res = np.array(res)
    # print(res)
