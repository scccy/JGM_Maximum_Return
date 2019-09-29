from program import Buff_List
from program import States
import numpy as np
from tqdm import tqdm
import itertools
from queue import PriorityQueue as PQ
from scipy.special import comb


class Result(object):
    def __init__(self, priority, builds):
        self.priority = priority
        self.builds = builds

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority


class Calculation(object):
    startDict = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
    star = dict()
    start = dict()
    results = PQ()
    cdict = dict()
    '''
    取值BUFF
    '''
    States = States.Buff()
    Item = Buff_List.Item()
    OneStars = States.OneStars
    TwoStars = States.TwoStars
    TriStars = States.TriStars
    QuaStars = States.QuaStars
    PenStars = States.PenStars
    Policy = States.Policy
    Photos = States.Photos
    residence = States.residence
    commercial = States.commercial
    industry = States.industry


    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    '''
    调整基础数据
    '''

    def dict_list(self):
        for item in self.OneStars:
            self.star[item] = 1
        for item in self.TwoStars:
            self.star[item] = 2
        for item in self.TriStars:
            self.star[item] = 3
        for item in self.QuaStars:
            self.star[item] = 4
        for item in self.PenStars:
            self.star[item] = 5

        for item in self.residence:  # 住宅
            self.start[item] = self.startDict[self.star[item]] * \
                          (1 + self.Policy['Global'] + self.Policy['Online'] + self.Policy['Residence']
                           + self.Policy['JiaGuoZhiGuang']) * \
                          (1 + self.Photos['Global'] + self.Photos['Online'] + self.Photos['Residence'])
        for item in self.commercial:  # 商业
            self.start[item] = self.startDict[self.star[item]] * \
                          (1 + self.Policy['Global'] + self.Policy['Online'] + self.Policy['Commercial']
                           + self.Policy['JiaGuoZhiGuang']) * \
                          (1 + self.Photos['Global'] + self.Photos['Online'] + self.Photos['Commercial'])
        for item in self.industry:  # 工业
            self.start[item] = self.startDict[self.star[item]] * \
                          (1 + self.Policy['Global'] + self.Policy['Online'] + self.Policy['Industry']
                           + self.Policy['JiaGuoZhiGuang']) * \
                          (1 + self.Photos['Global'] + self.Photos['Online'] + self.Photos['Industry'])

    '''
    正常调整倍数
    '''
    def adjustment(self, star_name, star_nb):
        self.start[star_name] *= star_nb

    def calculateComb(self, buildings):
        self.dict_list()
        buildtuple = buildings[0] + buildings[1] + buildings[2]
        starts = [self.start[x] for x in buildtuple]
        results = [1] * 9
        for item in buildtuple:
            if item in self.Item.buffs_100:
                for buffed in self.Item.buffs_100[item]:
                    if buffed in buildtuple:
                        results[buildtuple.index(buffed)] += self.star[item]
            if item in self.Item.buffs_50:
                for buffed in self.Item.buffs_50[item]:
                    if buffed in buildtuple:
                        results[buildtuple.index(buffed)] += self.star[item] * 0.5
            if item in self.Item.buffs_com:
                results[0:3] = np.add(results[0:3], self.Item.buffs_com[item][self.star[item] - 1])
            if item in self.Item.buffs_ind:
                results[3:6] = np.add(results[3:6], self.Item.buffs_ind[item][self.star[item] - 1])
            if item in self.Item.buffs_res:
                results[6:9] = np.add(results[6:9], self.Item.buffs_res[item][self.star[item] - 1])
        return (np.sum([v * results[i] for i, v in enumerate(starts)]),
                [v * results[i] / self.startDict[self.star[buildtuple[i]]] for i, v in enumerate(starts)])



    def bset(self):
        print('==============')
        Rec = self.results.get()
        print('最优策略：', Rec.builds[0])
        print('总加成倍率',
              np.round(sum([x * self.startDict[self.star[Rec.builds[0][i // 3][i % 3]]] for i, x in enumerate(Rec.builds[1])]),
                       2))
        print('各建筑加成倍率', np.round(Rec.builds[1], 2))
        print('升级优先级',
              np.round([x * self.startDict[self.star[Rec.builds[0][i // 3][i % 3]]] for i, x in enumerate(Rec.builds[1])], 2))

    def better(self):
        print('==============')
        Rec = self.results.get()
        print('次优策略：', Rec.builds[0])
        print('总加成倍率',
              np.round(sum([x * self.startDict[self.star[Rec.builds[0][i // 3][i % 3]]] for i, x in enumerate(Rec.builds[1])]),
                       2))
        print('各建筑加成倍率', np.round(Rec.builds[1], 2))
        print('升级优先级',
              np.round([x * self.startDict[self.star[Rec.builds[0][i // 3][i % 3]]] for i, x in enumerate(Rec.builds[1])], 2))

    def mian(self):
        result = comb(len(self.commercial), 3) * comb(len(self.industry), 3) * comb(len(self.residence), 3)
        print('Total iterations:', result)
        for item in tqdm(itertools.product(itertools.combinations(self.commercial, 3),
                                           itertools.combinations(self.industry, 3),
                                           itertools.combinations(self.residence, 3))):
            prod = self.calculateComb(item)
            self.results.put(Result(-prod[0], (item, prod[1])))
        self.bset()
        self.better()