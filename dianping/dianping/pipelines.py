# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import log
from os.path import join
from scrapy.exceptions import DropItem
import gridfs

from dianping.db import get_connection
from dianping.settings import IMAGES_STORE

from dianping.items import DianpingShopItem, DianpingImageItem

class DianpingPipeline(object):
    def __init__(self):
        self.db = get_connection()
        self.fs = gridfs.GridFS(self.db, collection="images")
        
    def process_item(self, item, spider):
        if isinstance(item, DianpingShopItem):
            return self.process_detail_item(item, spider)

        if isinstance(item, DianpingImageItem):
            return self.process_image_item(item, spider)

    def process_detail_item(self, item, spider):
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
    
    def process_image_item(self, item, spider):
        try:
            assert len(item['image_urls']) > 0
            assert len(item['images']) > 0
            assert len(item['image_name']) > 0
        except:
            raise DropItem
       
        # drop existing images
        if self.fs.exists({'url':item['images'][0]['url']}):
            raise DropItem

        file = open(join(IMAGES_STORE, item['images'][0]['path']),'r')
        self.fs.put(file, filename=item['image_name']+'.jpg', shop_id=item['shop_id'], url=item['images'][0]['url'])
        return item
