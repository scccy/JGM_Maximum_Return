
class Item(object):
    buffs_100 = {
            '木屋': ['木材厂'],
            '居民楼': ['便利店'],
            '钢结构房': ['钢铁厂'],
            '花园洋房': ['商贸中心'],
            '空中别墅': ['民食斋'],

            '便利店': ['居民楼'],
            '五金店': ['零件厂'],
            '服装店': ['纺织厂'],
            '菜市场': ['食品厂'],
            '学校':  ['图书城'],
            '图书城': ['学校', '造纸厂'],
            '商贸中心': ['花园洋房'],

            '木材厂': ['木屋'],
            '食品厂': ['菜市场'],
            '造纸厂': ['图书城'],
            '钢铁厂': ['钢结构房'],
            '纺织厂': ['服装店'],
            '零件厂': ['五金店'],
            '企鹅机械':['零件厂'],
            '人民石油':['加油站']
            }
    buffs_50 = {'零件厂': ['企鹅机械'],'加油站': ['人民石油']}
    bufflist_258 = [.2, .5, .8, 1.1, 1.4]
    bufflist_246 = [.2, .4, .6, .8, 1.0]
    bufflist_015 = [0.75 * x for x in [.2, .4, .6, .8, 1.0]]
    bufflist_010 = [0.5 * x for x in [.2, .4, .6, .8, 1.0]]
    bufflist_005 = [0.25 * x for x in [.2, .4, .6, .8, 1.0]]
    bufflist_035 = [2.25 * x for x in [.2, .4, .6, .8, 1.0]]
    buffs_com = {
        '媒体之声': bufflist_005,
        '企鹅机械': bufflist_015,
        '民食斋': bufflist_246,
        '纺织厂': bufflist_015,
        '人才公寓': bufflist_246,
        '中式小楼': bufflist_246,
        '空中别墅': bufflist_258,
        '电厂': bufflist_258
    }
    buffs_ind = {
        '媒体之声': bufflist_005,
        '钢铁厂': bufflist_015,
        '中式小楼': bufflist_246,
        '民食斋': bufflist_246,
        '空中别墅': bufflist_258,
        '电厂': bufflist_258,
        '企鹅机械': bufflist_258,
        '人才公寓': bufflist_035
    }
    buffs_res = {
        '媒体之声': bufflist_005,
        '企鹅机械': bufflist_010,
        '民食斋': bufflist_246,
        '人才公寓': bufflist_246,
        '平房': bufflist_246,
        '空中别墅': bufflist_258,
        '电厂': bufflist_258,
        '中式小楼': bufflist_035
    }