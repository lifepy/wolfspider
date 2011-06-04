# coding=utf-8
import re
from os.path import dirname, abspath, join, pardir
from BeautifulSoup import BeautifulSoup

from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from koubei.items import KoubeiStoreItem

class StoreDetailSpider(CrawlSpider):
    name = 'store'
    allowed_domains = ['koubei.com']
    rules = (
        Rule(SgmlLinkExtractor(allow=('.*store/detail--storeId-[0-9a-z]+.*')), callback='parse_store_detail'), # store detail information page
        Rule(SgmlLinkExtractor(allow=('.+&page=\d+.+')), follow=True), # next page
    )
    city_pattern = re.compile(r'http://([^.]+)\.koubei\.com/.+')
    # start_urls = ['http://beijing.koubei.com/store/detail--storeId-132c86562acb4384acd45230ade1f44d?ad_id=&am_id=&cm_id=&pm_id=',]

    def start_requests(self):
        seed_file = join(dirname(abspath(__file__)), pardir, 'seeds','koubei.txt')
        for line in open(seed_file, 'r').readlines():
            url = line.strip().split(',')[1]
            print url
            yield Request(url, dont_filter=True) 

    def parse_store_detail(self, response):
        hxs = HtmlXPathSelector(response)

        item = KoubeiStoreItem()
        # Url
        item['link_url'] = response.url
        match = self.city_pattern.match(response.url)
        if match:
            item['city'] = match.group(1)

        # Name
        name_elem = hxs.select("//input[@id='store-full-name']/@value").extract()
        if name_elem:
            item['name'] = name_elem[0]

        # Address
        address_elem = hxs.select("//input[@id='store-address']/@value").extract()
        if address_elem:
            item['address'] = address_elem[0]

        # Telephone
        tel_elem = hxs.select("//input[@id='store-tel']/@value").extract()
        if tel_elem:
            item['tel'] = tel_elem[0]
        
        # Average Cost
        avg_elem = hxs.select("//div[@class='store-info-card']//li/text()").extract()
        for text in avg_elem:
            if text.startswith("人均".decode('utf-8')):
                item['avg_cost'] = text.split(u'\uff1a')[1]
                break

        # Rating
        rating_elem = hxs.select("//div[@class='store-free-title k2-fix-float']/p/b/text()").extract()
        if rating_elem:
            item['rating'] = rating_elem[0]
            item['n_rating'] = int(rating_elem[1])

        # Detail
        detail_elem = hxs.select("//div[@class='detail-main']/ul/li").extract()
        for elem in detail_elem:
            text = BeautifulSoup(elem).find('label').text
            if text.startswith('网站地址'.decode('utf-8')):
                item['url'] = text.split(u'\uff1a')[1].strip()
            if text.startswith('店铺标签'.decode('utf-8')):
                item['tag_list'] = [a.text for a in BeautifulSoup(elem).findAll('a')]
            
        # Description
        desc_elem = hxs.select("//div[@class='detail-intro']/div/text()").extract()
        if desc_elem:
            item['description'] = desc_elem[0].strip()

        # Promote
        promote_elems= hxs.select("//div[@id='promote-more']//p").extract()
        promotes = []
        for elem in promote_elems:
            name = BeautifulSoup(elem).find('a').text.strip()
            count = int(BeautifulSoup(elem).find('span').text[1:-1])
            promotes.append((name, count))
        if promotes != []:
            item['promote_list'] = promotes
            
        # Impress
        impress_elems = hxs.select("//div[@id='impress-more']//span/text()").extract()
        if impress_elems:
            item['impress_list'] = [imp.strip() for imp in impress_elems]

        print "PARSING : %s | %s | %s | %s" % (item['name'], item['tel'], item['address'], item['avg_cost'])
        return item
