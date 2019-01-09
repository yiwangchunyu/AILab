import utils

class Life(object):
    def __init__(self, chromosome,data):
        self.chromosome = [] #染色体序列
        self.adaptive_score = 0   #适应值
        self.update(chromosome, data)

    def update(self, chromosome, data):
        self.chromosome = chromosome
        self.adaptive_score = utils.get_adaptive_score(chromosome, data)