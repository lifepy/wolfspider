# coding=utf-8


BOT_NAME = 'dianping'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dianping.spiders']
NEWSPIDER_MODULE = 'dianping.spiders'
DEFAULT_ITEM_CLASS = 'dianping.items.DianpingShopItem'
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
LOG_ENABLED = True
LOG_FILE = "/tmp/scrapy.dianping.shop.log"
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

from fixtures import *
TARGET_PROVINCE = huanan+huazhong
cities = set()
for p in TARGET_PROVINCE:
    cities = cities.union(province_dict[p])

# SEED that the spider starts with
SEEDS= [ 'http://www.dianping.com/'+ city for city in cities ]
# SEED_FILE=join(dirname(__file__), 'seeds', 'major-cities.txt')
