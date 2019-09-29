
class Buff(object):
    '''
    在这里填写你的政策和照片加成
    '''
    Policy = {
        'Global': 1,
        'Online': 1,
        'Offline': 1,
        'Residence': 1,
        'Commercial': 1,
        'Industry': 1,
        'JiaGuoZhiGuang': 1
    }

    Photos = {
        'Global': 1,
        'Online': 1,
        'Offline': 1,
        'Residence': 1,
        'Commercial': 1,
        'Industry': 1
    }

    '''
    已有建筑填写
    '''
    residence = '木屋 居民楼 钢结构房 平房 人才公寓'.split()
    commercial = '服装店 五金店 菜市场 学校 图书城 民食斋'.split()
    industry = '木材厂 食品厂 造纸厂 电厂 钢铁厂 纺织厂 零件厂 企鹅机械'.split()

    '''
    已有等级填写
    '''
    OneStars = '零件厂 民食斋 人才公寓 企鹅机械'.split()
    TwoStars = '居民楼 图书城 钢铁厂 电厂'.split()
    TriStars = '平房 学校 五金店 菜市场 服装店 木屋 木材厂 造纸厂 钢结构房 食品厂 纺织厂'.split()
    QuaStars = ''.split()
    PenStars = ''.split()





class main(object):
    Policy_Global = ''
    Policy_Online = ''
    Policy_Offline = ''
    Policy_Residence = ''
    Policy_Commercial = ''
    Policy_Industry = ''
    Policy_JiaGuoZhiGuang = ''
    Photos_Global = ''
    Photos_Online = ''
    Photos_Offline = ''
    Photos_Residence = ''
    Photos_Commercial = ''
    Photos_Industry = ''
    OneStars = ''.split()
    TwoStars = ''.split()
    TriStars = ''.split()
    QuaStars = ''.split()
    PenStars = ''.split()
