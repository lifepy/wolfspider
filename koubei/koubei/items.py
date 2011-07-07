# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class KoubeiStoreItem(Item):
    link_url = Field()

    bread_crumb = Field(default="")
    name = Field(default="")
    category = Field(default="")

    rating = Field(default=-1)
    n_rating = Field(default=0)
    avg_cost = Field(default="")

    url = Field(default="")
    tel = Field(default="")
    city = Field()
    address = Field(default="")
    description = Field(default="")

    tag_list = Field(default="")
    impress_list = Field(default="")
    promote_list = Field(default="")

    city = Field()

    def __repr__(self):
        return self.simple_repr()

    def simple_repr(self):
        return self['name']+'| '+self['city'] +' | ' +self['bread_crumb']

    def full_repr(self):
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
