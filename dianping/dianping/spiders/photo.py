# coding=utf-8
import re
from urlparse import urlparse
from os.path import join, dirname, abspath, pardir
from BeautifulSoup import BeautifulSoup

from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from scrapy.exceptions import IgnoreRequest

from dianping.items import DianpingImageItem
from dianping import settings

class ShopImageSpider(CrawlSpider):
    image_list_url_pattern = re.compile(r'http://www\.dianping\.com/shop/(\d+).+')
    name = 'photo'
    allowed_domains = ['dianping.com', 'i1.dpfile.com','i2.dpfile.com','i3.dpfile.com']
    rules = (
        Rule(SgmlLinkExtractor(allow=('shop/\d+/photos(\?pg=\d+)*'), restrict_xpaths="//a[@class='NextPage']", unique=True), callback="parse_image_list_page"), # page list page & next page
        #Rule(SgmlLinkExtractor(allow=('photos/\d+'), restrict_xpaths="//div[@class='gallery-list-wrapper page-block']", unique=True), callback="extract_image"), # photo page
        Rule(SgmlLinkExtractor(allow=('.+\d+p\d+(n\d+)?/?.*$'), restrict_xpaths="//a[@class='NextPage']", unique=True)), # next page
    )

    start_urls = ['http://www.dianping.com/shop/2830624/photos',]

    def start_requests(self):
        if 'SEEDS' in settings.__dict__.keys():
            for seed in settings.SEEDS[self.name]:
                yield Request(seed, dont_filter=True)
        elif 'SEED_FILE' in settings.__dict__.keys():
            # Each line represents a start up urls. Lines starts with '#' are comments. Empty lines are ignored.
            for line in open(settings.SEED_FILE,'r').readlines():
                if line.startswith('#'): continue
                yield Request(line.strip(), dont_filter=True)
        else:
            raise KeyError('neither SEEDS nor SEED_FILE defined in settings.py')

    def parse_image_list_page(self, response):
        hxs = HtmlXPathSelector(response)
        selector = SgmlLinkExtractor(allow=('photos/\d+'), restrict_xpaths="//div[@class='gallery-list-wrapper page-block']", unique=True)
        next_page_link = SgmlLinkExtractor(allow=('shop/\d+/photos(\?pg=\d+)*'), restrict_xpaths="//a[@class='NextPage']", unique=True)
        match = self.image_list_url_pattern.match(response.url)
        if match:
            shop_id = match.group(1)

        # Prepare cookies
        cookies = {}
        if 'Set-Cookie' in response.headers:
            for eq in response.headers['Set-Cookie'].split(';'):
                k,v = eq.strip().split('=')
                cookies[k] = v

        # follow next-page
        for link in next_page_link.extract_links(response):
            yield Request(link.url, cookies=cookies, callback=self.parse_image_list_page)

        # follow image link
        for link in selector.extract_links(response):
            img_name = hxs.select('//a[@href="%s"]/img/../../../..//strong/@title' %urlparse(link.url).path).extract()[0]
            yield Request(link.url, headers={'Shop-Id':shop_id, "Image-Name":img_name}, cookies=cookies, callback=self.extract_image)

    def extract_image(self, response):
        shop_id = response.headers.get("Shop-Id",'')
        img_name = response.headers.get("Image-Name",'')
        if len(shop_id) <= 0 or len(img_name) <= 0:
            raise IgnoreRequest
        item = DianpingImageItem()
        item["shop_id"] = shop_id
        item['image_name'] = img_name
        body = str(response.body).decode(response.encoding)
        img_url = ""
        for l in body.split('\n'):
            if l.strip().startswith("pi: "):
                img_url = l.strip().split()[1].strip(",'")

        item['image_urls'] = [img_url, ]
        return item
