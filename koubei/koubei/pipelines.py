# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from koubei.db import get_connection

class KoubeiPipeline(object):
    def __init__(self):
        self.db = get_connection()
        
    def process_item(self, item, spider):
        val_dict = item.__dict__['_values']
        store_obj = self.db.stores.find_one({'link_url':val_dict['link_url']})
        if store_obj:
            print 'UPDATING', store_obj['link_url']
            for k,v in val_dict.items():
                store_obj[k] = v
            self.db.stores.save(store_obj)
        else:
            self.db.stores.save(val_dict)
        return item   
