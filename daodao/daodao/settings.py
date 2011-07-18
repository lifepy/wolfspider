# Scrapy settings for daodao project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'daodao'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['daodao.spiders']
NEWSPIDER_MODULE = 'daodao.spiders'
DEFAULT_ITEM_CLASS = 'daodao.items.DDAttractionInfoItem'

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
#    'scrapy.contrib.spidermiddleware.referer.RefererMiddleware', # add 'Referer' to request based on response
#    'dianping.middlewares.RefererMiddleware', # update 'Referer' field on response based on request
#    'dianping.middlewares.IgnoreVisitedUrlMiddleware', # prevent re-visit a url
#    'dianping.middlewares.IgnoreExistingURLMiddleware', # prevent re-visit a url based on database
#    'dianping.middlewares.RateLimitMiddleware', # prevent over limit
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware', # Cache
    #'scrapy.contrib.spidermiddleware.depth.DepthMiddleware', # depth control
]

# --- Pipelines ---
IMAGES_STORE = '/tmp/images/'
ITEM_PIPELINES = [
#    'scrapy.contrib.pipeline.images.ImagesPipeline',
    'daodao.pipelines.DaodaoPipeline'
]
# --- Concurrent ---
#CONCURRENT_REQUESTS_PER_SPIDER=1
CONCURRENT_SPIDERS=4

# --- Delay ---
DOWNLOAD_DELAY = 2
DOWNLOAD_TIMEOUT = 20
RANDOMIZE_DOWNLOAD_DELAY = True

