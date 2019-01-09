import random
import utils
import pyprind

from GA import GA


class TravelingSalesman(object):

    def __init__(self, data, N, mating_rate=0.7, variation_rate=0.02):
        self.data = data
        self.scale_N = N  # 群体规模N
        self.mating_rate = mating_rate
        self.variation_rate = variation_rate
        self.ga = GA(data, N, mating_rate, variation_rate)
        self.distance = 0

    def travel_start(self, n=100):
        bar = pyprind.ProgBar(n)
        while n > 0:
            self.ga.new_generation()
            #print(n, self.ga.best_life.adaptive_score)
            #print([life.chromosome for life in self.ga.lives])
            #print(self.data)
            self.distance = utils.get_distance_all(self.ga.best_life.chromosome, self.data)
            n -= 1
            bar.update()