# coding=utf-8
from scrapy import log
from scrapy.http import Request
from scrapy.project import crawler
from scrapy.item import BaseItem
from scrapy.utils.request import request_fingerprint
from scrapy.exceptions import IgnoreRequest

from dianping.items import DianpingShopItem
from dianping.db import get_connection

class RateLimitMiddleware(object):
    limit_indicators = (
        '对不起，你访问的太快了',
        #'发布的所有内容，未经许可，不得转载',
    )
    def process_response(self, request, response, spider):
        # log.msg('Response: %s'%response.url, log.INFO)
        for indicator in self.limit_indicators:
            if indicator in response.body:
                log.msg('Toooooo FAST!', log.WARNING)
                crawler.engine.close_spider(spider, 'over the limit')
                raise IgnoreRequest

        return response

class IgnoreExistingURLMiddleware(object):

    db = get_connection()

    def process_request(self, request, spider):
        if self.db.shops.find_one({'link_url':request.url}):
            log.msg('Ignore: %s'%request.url, log.WARNING)
            raise IgnoreRequest
        # log.msg('Request: %s'%request.url, log.INFO)
        return None

class IgnoreVisitedUrlMiddleware(object):
    """Middleware to ignore re-visiting item pages if they were already visited
    before. The requests to be filtered by have a meta['filter_visited'] flag
    enabled and optionally define an id to use for identifying them, which
    defaults the request fingerprint, although you'd want to use the item id,
    if you already have it beforehand to make it more robust.
    """

    FILTER_VISITED = 'filter_visited'
    VISITED_ID = 'visited_id'
    CONTEXT_KEY = 'visited_ids'

    def process_spider_output(self, response, result, spider):
        log.msg("IGNORE REVIESITED!", log.WARNING)
        context = getattr(spider, 'context', {})
        visited_ids = context.setdefault(self.CONTEXT_KEY, {})
        ret = {}
        for x in result:
            visited = False
            if isinstance(x, Request):
                if self.FILTER_VISITED in x.meta:
                    visit_id = self._visited_id(x)
                    if visit_id in visited_ids:
                        log.msg('Ignore: %s' %x.url, level=log.INFO, spider=spider)
                        visited = True
            elif isinstance(x, BaseItem):
                visit_id = self._visited_id(response.request)
                if visit_id:
                    visited_ids[visit_id] = True
                    x['visit_id'] = visit_id
                    x['visit_status'] = 'new'
            if visited:
                ret.append(DianpingShopItem(visit_id=visit_id, visit_status='old'))
            else:
                ret.append(x)
        return ret
    
    def _visited_id(self, request):
        return request.meta.get(self.VISITED_ID) or request_fingerprint(request)
