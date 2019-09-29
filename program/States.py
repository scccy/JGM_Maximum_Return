
# class Buff(object):
#     '''
#     在这里填写你的政策和照片加成
#     '''
#     Policy = {
#         'Global': 1,
#         'Online': 1,
#         'Offline': 1,
#         'Residence': 1,
#         'Commercial': 1,
#         'Industry': 1,
#         'JiaGuoZhiGuang': 1
#     }
#
#     Photos = {
#         'Global': 1,
#         'Online': 1,
#         'Offline': 1,
#         'Residence': 1,
#         'Commercial': 1,
#         'Industry': 1
#     }
#
#     '''
#     已有建筑填写
#     '''
#     commercial = '便利店 五金店 服装店 菜市场 学校 图书城 商贸中心 加油站 民食斋 媒体之声'
#     residence = '木屋 居民楼 钢结构房 平房 小型公寓 人才公寓 花园洋房 中式小楼 空中别墅 复兴公馆'
#     industry = '木材厂 食品厂 造纸厂 水厂 电厂 钢铁厂 纺织厂 零件厂 企鹅机械 人民石油'
#
#     '''
#     已有等级填写
#     '''
#     OneStars = '零件厂 民食斋 人才公寓 企鹅机械'.split()
#     TwoStars = '居民楼 图书城 钢铁厂 电厂'.split()
#     TriStars = '平房 学校 五金店 菜市场 服装店 木屋 木材厂 造纸厂 钢结构房 食品厂 纺织厂'.split()
#     QuaStars = ''.split()
#     PenStars = ''.split()


from collections import defaultdict


class Buff(object):

    commercial = '便利店 五金店 服装店 菜市场 学校 图书城 商贸中心 加油站 民食斋 媒体之声'
    residence = '木屋 居民楼 钢结构房 平房 小型公寓 人才公寓 花园洋房 中式小楼 空中别墅 复兴公馆'
    industry = '木材厂 食品厂 造纸厂 水厂 电厂 钢铁厂 纺织厂 零件厂 企鹅机械 人民石油'
    Policy = defaultdict(list)
    Photos = defaultdict(list)

    def __int__(self,Policy_Global, Policy_Online, Policy_Offline, Policy_Residence,Policy_Commercial,Policy_Industry,
                Policy_JiaGuoZhiGuang, Photos_Global, Photos_Online, Photos_Offline, Photos_Residence, Photos_Commercial,
                Photos_Industry):
        self.Policy_Global = '1'
        self.Policy_Online = '1'
        self.Policy_Offline = '1'
        self.Policy_Residence = '1'
        self.Policy_Commercial = '1'
        self.Policy_Industry = '1'
        self.Policy_JiaGuoZhiGuang = '1'

        self.Photos_Global = '1'
        self.Photos_Online = '1'
        self.Photos_Offline = '1'
        self.Photos_Residence = '1'
        self.Photos_Commercial = '1'
        self.Photos_Industry = '1'
        #
        # self.OneStars = ''.split()
        # self.TwoStars = ''.split()
        # self.TriStars = ''.split()
        # self.QuaStars = ''.split()
        # self.PenStars = ''.split()

    def dick(self):
        self.Policy['Global'] = self.Policy_Global
        self.Policy['Online'] = self.Policy_Online
        self.Policy['Offline'] = self.Policy_Offline
        self.Policy['Residence'] = self.Policy_Residence
        self.Policy['Commercial'] = self.Policy_Commercial
        self.Policy['Industry'] = self.Policy_Industry
        self.Policy['JiaGuoZhiGuang'] = self.Policy_JiaGuoZhiGuang

        self.Photos['Global'] = self.Photos_Global
        self.Photos['Online'] = self.Photos_Online
        self.Photos['Offline'] = self.Photos_Offline
        self.Photos['Residence'] = self.Photos_Residence
        self.Photos['Commercial'] = self.Photos_Commercial
        self.Photos['Industry'] = self.Photos_Industry
        return self.Policy

a = Buff()
a.Policy_Global = 1
Policy =a.dick()
print(Policy)