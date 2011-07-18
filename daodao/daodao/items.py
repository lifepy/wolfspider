# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DDAttractionInfoItem(Item):
    name = Field()
    rating = Field()
    category = Field() 
    grade = Field() 
    n_comments = Field() 

    country = Field()
    locality = Field()
    street_addr = Field()

    phone = Field()
    url = Field()
    hours = Field()
    price = Field()

    latitude = Field()
    longtitude = Field()

    rss_url = Field()
    link_url = Field()

    def __repr__(self):
        return self.get('name','NO_NAME') +" | "+ self.get('link_url','NO_URL')
