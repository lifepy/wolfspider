import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from daodao.items import DDAttractionInfoItem

class InfoSpider(CrawlSpider):
    name = 'info'
    allowed_domains = ['www.daodao.com']
    start_urls = ['http://www.www.daodao.com/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = DDAttractionInfoItem()

        
        # Number of Comments
        n_comments_elem = hxs.select('//strong[@property="v:count"]/text()').extract()
        item['n_comments'] = int(n_comments_elem[0])

        # Rating
        rating_elem = hxs.select('//div[@class="ar-detail"]/li/strong/text()').extract()
        if rating_elem:
            item['rating'] = float(rating_elem[0])

        # Longtitude / Latitude


        # Grade
        grade_elem = hxs.select('//span[@class="ar-grade"]/text()').extract()
        if grade_elem:
            item['grade'] = grade_elem[0]

        # Introduction
        intro_elem = hxs.select('//div[@class="review-intro"]/').extract()
        return item
