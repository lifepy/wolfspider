# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import log
from dianping.db import get_connection

class DianpingPipeline(object):
    def __init__(self):
        self.db = get_connection()
        
    def process_item(self, item, spider):
        val_dict = item.__dict__['_values']
        shop_obj = self.db.shops.find_one({'link_url':val_dict['link_url']})
        if shop_obj:
            log.msg('Update: '+shop_obj['link_url'], log.INFO)
            for k,v in val_dict.items():
                shop_obj[k] = v
            self.db.shops.save(shop_obj)
        else:
            self.db.shops.save(val_dict)
            #self.db.visited.save(val_dict['link_url'])
        return item       
