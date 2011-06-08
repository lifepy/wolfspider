# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DianpingShopItem(Item):
    link_url = Field()
    
    name = Field()
    n_rating = Field()
    rating = Field()
    taste_rating = Field()
    service_rating = Field()
    atmosphere_rating = rating = Field()

    address = Field()
    tel = Field()
    category = Field()
    city = Field()

    avg_cost = Field()
    bread_crumb = Field()
    description = Field()

    recommend_list = Field()
    atmosphere_list = Field()
    feature_list = Field()
    landmark_bread_crumb = Field()
    hours = Field()
    transport = Field()

    def __repr__(self):
        result = "\n"
        for k,v in self.__dict__['_values'].items():
            if type(v) == str:
                result += "%s %s\n" % (k,v)
            elif type(v) == unicode:
                result += "%s %s\n" % (k, v.encode('utf-8'))
            elif type(v) == int:
                result += "%s %d\n" % (k, v)
            elif type(v) == list and len(v)>0:
                if type(v[0]) == str:
                    result += "%s %s\n" % (k, ','.join(v))
                elif type(v[0]) == unicode:
                    result += "%s %s\n" % (k, ','.join([x.encode('utf-8') for x in v]))
                elif type(v[0]) == tuple and type(v[0][0]) == unicode:
                    result += "%s %s\n" % (k, ','.join(['%s (%d)' % (name.encode('utf-8'),count) for name, count in v]))
            else:
                result += `k`+' '+`v`+'\n'

        return result

