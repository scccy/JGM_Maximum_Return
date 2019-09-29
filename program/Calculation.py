from program import Buff_List
from program import States

class Calculation(object):
    startDict = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
    star = dict()
    start = dict()
    '''
    取值BUFF
    '''
    States = States.Buff()
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

    def adjustment(self, star_name, star_nb):
	    self.start[star_name] *= star_nb
