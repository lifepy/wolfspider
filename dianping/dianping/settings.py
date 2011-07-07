# coding=utf-8

province_dict = {
    # 华东地区：山东、江苏、浙江、安徽、江西、福建、台湾
    'shandong':( # 山东
        # 济南市 青岛市 淄博市 枣庄市 东营市 烟台市
        'jinan', 'zibo', 'zaozhuang', 'dongying', 'yantai',
        # 潍坊市 济宁市 泰安市 威海市 日照市 莱芜市 临沂市
        'weifang', 'jining', 'taian','weihai','rizhao','laiwu','linyi'
        # 德州市 聊城市 滨州市 菏泽市
        'dezhou', 'liaocheng', 'binzhou','heze'),

    'jiangsu': ( # 江苏
        # 南京市 无锡市 徐州市 常州市 苏州市 南通市
        'nanjing', 'wuxi', 'xuzhou', 'changzhou', 'nantong',
        # 连云港市 淮安市 盐城市 扬州市 镇江市 泰州市 宿迁市
        'lianyungang', 'huaian', 'yancheng', 'zhenjiang', 'taizhou', 'suqian'),

    'shanghai':('shanghai',),

    'zhejiang': ( # 浙江
        # 杭州市 宁波市 温州市 嘉兴市 湖州市 绍兴市
        'hangzhou','ningbo','wenzhou','jiaxing','huzhou','shaoxing',
        # 金华市 衢州市 舟山市 *台州市 丽水市
        'jinhua','quzhou','zhoushan','zhejiangtaizhou','lishui'),
    
    'anhui':( #安徽
        # 合肥市 芜湖市 蚌埠市 淮南市 马鞍山市 淮北市 
        'hefei','wuhu','bangbu','huainan','maanshan','huaibei',
        # 铜陵市 安庆市 黄山市 滁州市 阜阳市 *宿州市 
        'tongling','anqing','huangshan','chuzhou','buyang','anhuisuzhou',
        # 巢湖市 六安市 亳州市(点评不存在) 池州市 宣城市
        'chaohu','liuan','haozhou','chizhou','xuancheng'),

    'jiangxi':( #江西
        # 南昌市 景德镇市 萍乡市 九江市 新余市 鹰潭市 
        'nanchang','jingdezhen','pingxiang','jiujiang','xinyu','yingtan',
        # 赣州市 吉安市 *宜春市 *抚州市 上饶市
        'ganzhou','jian','jiangxiyichun','jiangxifuzhou','shangrao'),

    'fujian':( # 福建
        # 福州市 厦门市 莆田市 三明市 泉州市 漳州市
        'fuzhou', 'xiamen' 'putian', 'sanming', 'quanzhou','zhangzhou'
        # 南平市 龙岩市 宁德市
        'nanping', 'longyan', 'ningde'),

     'taiwan':( 'taiwan', ), # 台湾

     # 华南地区
    'guangdong':(# 广东
         # 广州市 韶关市 深圳市 珠海市 汕头市 佛山市 
         'guangzhou','shaoguan','shenzhen','zhuhai','shantou','foshan',
         # 江门市 湛江市 茂名市 肇庆市 惠州市 梅州市 
         'jiangmen','zhanjiang','maoming','zhaoqing','huizhou','meizhou',
         # 汕尾市 河源市 阳江市 清远市 东莞市 中山市
         'shanwei','heyuan','yangjiang','qingyuan','dongguan','zhongshan'
         # 潮州市 揭阳市 云浮市
         'chaozhou','jieyang','yunfu'),

    'hainan':(# 海南
        # 海口市 三亚市
        'haikou','sanya'),

    'guangxi':( # 广西
        # 南宁市 柳州市 桂林市 梧州市 北海市 防城港市
        'nanning', 'liuzhou', 'guilin' 'wuzhou', 'beihai', 'fangchenggang',
        # 钦州市 贵港市 玉林市 百色市 贺州市 河池市
        'qinzhou', 'guigang', 'yulin', 'baise','hezhou','hechi',
        # 来宾市 崇左市
        'laibin', 'chongzuo'),

    # 华中地区：河南、湖北、湖南
    'henan':(# 河南
        # 郑州市 开封市 洛阳市 平顶山市 安阳市 鹤壁市 
        'zhengzhou','kaifeng','luoyang','pingdingshan','anyang','hebi'
        # 新乡市 焦作市 濮阳市 许昌市 漯河市 三门峡市 
        'xinxiang','jiaozuo','puyang','xuchang','luohe','sanmenxia',
        # 南阳市 商丘市 信阳市 周口市 驻马店市
        'nanyang','shangqiu','yinyang','zhoukou','zhumadian'),

    # 直辖市
    'beijing':('beijing',),
    'chongqing':('chongqing',),
    'tianjin':('tianjing',),
}

BOT_NAME = 'dianping'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dianping.spiders']
NEWSPIDER_MODULE = 'dianping.spiders'
DEFAULT_ITEM_CLASS = 'dianping.items.DianpingShopItem'
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
LOG_LEVEL = 'DEBUG'

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = '/tmp/scrapy/cache/'
DOWNLOADER_MIDDLEWARES = [ 
    'dianping.middlewares.IgnoreVisitedUrlMiddleware',
    'dianping.middlewares.IgnoreExistingURLMiddleware',
    'dianping.middlewares.RateLimitMiddleware',
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware',
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware',
]

# Depth limit
# DEPTH_LIMIT=10

#CONCURRENT_REQUESTS_PER_SPIDER=1
CONCURRENT_SPIDERS=4

DOWNLOAD_DELAY = 2
DOWNLOAD_TIMEOUT = 20
RANDOMIZE_DOWNLOAD_DELAY = True

# LOG_FILE = 'crawl.log'
ITEM_PIPELINES = ['dianping.pipelines.DianpingPipeline']

TARGET_PROVINCE = ['jiangsu','zhejiang','shanghai','shandong','anhui','fujian','jiangxi','taiwan',]
cities = set()
for p in TARGET_PROVINCE:
    cities = cities.union(province_dict[p])

# SEED that the spider starts with
SEEDS= [ 'http://www.dianping.com/'+ city for city in cities ]
# SEED_FILE=join(dirname(__file__), 'seeds', 'major-cities.txt')
