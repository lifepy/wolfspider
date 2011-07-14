# Scrapy settings for koubei project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'koubei'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['koubei.spiders']
NEWSPIDER_MODULE = 'koubei.spiders'
DEFAULT_ITEM_CLASS = 'koubei.items.KoubeiStoreItem'
USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
# USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = '/tmp/scrapy/cache/koubei/'
DOWNLOADER_MIDDLEWARES = [ 
    'koubei.middlewares.IgnoreVisitedUrlMiddleware',
    'koubei.middlewares.IgnoreExistingURLMiddleware',
    # 'koubei.middlewares.RateLimitMiddleware',
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware',
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware',
]

# project specific
ITEM_PIPELINES = [ 'koubei.pipelines.KoubeiPipeline', ]

LOG_ENABLED = True
#LOG_FILE = "/tmp/scrapy.koubei.store.log"
LOG_LEVEL = 'DEBUG'

# Depth limit
## DEPTH_LIMIT=10
#
#CONCURRENT_REQUESTS_PER_SPIDER=1
CONCURRENT_SPIDERS=4

DOWNLOAD_DELAY = 2
DOWNLOAD_TIMEOUT = 20
RANDOMIZE_DOWNLOAD_DELAY = True

#from fixtures import *
#SEEDS= [ 'http://www.dianping.com/'+ city for city in cities ]
# SEED_FILE=join(dirname(__file__), 'seeds', 'major-cities.txt')
