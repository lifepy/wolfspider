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
DEFAULT_ITEM_CLASS = 'daodao.items.DaodaoItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

