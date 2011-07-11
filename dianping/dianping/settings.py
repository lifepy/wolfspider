# coding=utf-8

BOT_NAME = 'dianping'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dianping.spiders']
NEWSPIDER_MODULE = 'dianping.spiders'
DEFAULT_ITEM_CLASS = 'dianping.items.DianpingShopItem'

# --- User Agent ---
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'

# --- Log ---
LOG_ENABLED = True
#LOG_FILE = "/tmp/scrapy.dianping.shop.log"
LOG_LEVEL = 'DEBUG'

# --- Cache ---
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = '/tmp/scrapy/cache/'

# --- Middlewares ---
DOWNLOADER_MIDDLEWARES = [ 
    'dianping.middlewares.ShopIdMiddleware',
    'dianping.middlewares.IgnoreVisitedUrlMiddleware',
    'dianping.middlewares.IgnoreExistingURLMiddleware',
    'dianping.middlewares.RateLimitMiddleware',
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware',
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware',
]

# --- Pipelines ---
IMAGES_STORE = '/tmp/images/'
ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline','dianping.pipelines.DianpingPipeline']

# --- Depth limit ---
# DEPTH_LIMIT=10

# --- Concurrent ---
#CONCURRENT_REQUESTS_PER_SPIDER=1
CONCURRENT_SPIDERS=4

# --- Delay ---
DOWNLOAD_DELAY = 2
DOWNLOAD_TIMEOUT = 20
RANDOMIZE_DOWNLOAD_DELAY = True

# --- Fixtures & Seeds for 'shop' ---
from fixtures import *
provinces = huadong
cities = set()
for p in provinces:
    cities = cities.union(province_dict[p])

SEEDS = {}
SEEDS['shop'] = [ 'http://www.dianping.com/'+ city for city in cities ]

# --- Fixtures & Seeds for 'photo' ---
import re
from geos import cities_in
from db import get_connection
db = get_connection().shops
shop_url_pattern = re.compile(r'http://www\.dianping\.com/shop/(\d+).*')

provinces = north
cities = set()
for p in provinces:
    if p not in municipalities:
        cities = cities.union([c['name'] for c in cities_in(p)])
    else:
        cities.add(p)

urls = []
for c in cities:
    for shop in db.find({'city':c}):
        match = shop_url_pattern.match(shop['link_url'])
        if match:
            shop_id = match.group(1)
            urls.append('http://www.dianping.com/shop/%s/photos' % shop_id)
print len(urls)
SEEDS['photo'] = urls
# SEED_FILE=join(dirname(__file__), 'seeds', 'major-cities.txt')
