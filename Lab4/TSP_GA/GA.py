from Life import *
import random
#遗传算法类
class GA(object):
    def __init__(self, data, N, mating_rate=0.7, variation_rate=0.02):
        self.scale_N = N #群体规模N
        self.mating_rate = mating_rate
        self.variation_rate = variation_rate

        self.city_count = len(data)
        self.data = data
        self.lives = []
        self.generation = 0
        self.sum_score = 0
        self.init_group()

    #初始化种群群体
    def init_group(self):
        self.lives = []
        chromosome = [x for x in range(self.city_count)]
        for i in range(self.scale_N):
            random.shuffle(chromosome)  #随机打乱染色体顺序
            chromosome_cpy = chromosome[:]
            life = Life(chromosome_cpy, self.data)
            self.lives.append(life)
        self.sum_score = sum([life.adaptive_score for life in self.lives])

    def pick_one(self):
        #以概率pi选择种群中的一个个体
        r = random.uniform(0, self.sum_score)
        for life in self.lives:
            r -= life.adaptive_score
            if r <= 0:
                return life

    def mating(self, father, mother):
        #交配
        index1 = random.randint(0, self.city_count - 1)
        index2 = random.randint(index1, self.city_count - 1)
        chromosomePiece = father.chromosome[index1:index2]
        newchromosome = []
        fatherIndex = 0
        for g in mother.chromosome:
            if fatherIndex == index1:
                #插入基因
                newchromosome.extend(chromosomePiece)
                fatherIndex += 1
            if g not in chromosomePiece:
                newchromosome.append(g)
                fatherIndex += 1
        return newchromosome

    def variation(self, chromosome):
        """突变"""
        index1 = random.randint(0, self.city_count - 1)
        index2 = random.randint(0, self.city_count - 1)

        copy = chromosome[:]
        copy[index1], copy[index2] = copy[index2], copy[index1]
        return copy


    def newChild(self):
            #以交配概率mating_rate交配产生新的后代
            father = self.pick_one()
            rate = random.random()

            # 按概率交配
            if rate < self.mating_rate:
                mother = self.pick_one()
                chromosome = self.mating(father, mother)
            else:
                #没有交配权的加入新群体，等待基因突变
                chromosome = father.chromosome

            # 按概率突变
            rate = random.random()
            if rate < self.variation_rate:
                chromosome = self.variation(chromosome)

            return Life(chromosome, self.data)

    def get_best_life(self):
        #得到当前种群中最佳的个体
        self.best_life=self.lives[0]

        for life in self.lives:
            if self.best_life.adaptive_score < life.adaptive_score:
                self.best_life = life


    def new_generation(self):
        #产生下一个群体，数量为N
        newLives = []
        # 把最好的个体加入下一代
        self.get_best_life()
        newLives.append(self.best_life)
        while len(newLives) <= self.scale_N:
            newLives.append(self.newChild())
        self.lives = newLives
        self.sum_score = sum([life.adaptive_score for life in self.lives])
        self.generation += 1
