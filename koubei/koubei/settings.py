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
DEFAULT_ITEM_CLASS = 'koubei.items.KoubeiItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
HTTPCACHE_ENABLED = True
DOWNLOADER_MIDDLEWARES = [ 
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware',
    'koubei.middlewares.IgnoreVisitedUrlMiddleware',
]

# project specific
ITEM_PIPELINES = [ 'koubei.pipelines.KoubeiPipeline', ]
LOG_LEVEL='INFO'
