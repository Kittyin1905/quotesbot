# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'cricos_edu'
    allowed_domains = ['cricos.education.gov.au']
    start_urls = ['https://cricos.education.gov.au/Institution/InstitutionSearch.aspx?StateId=QLD/']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('cricos.education.gov.au/Institution/InstitutionDetails.aspx?ProviderID=', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('cricos.education.gov.au/Course/CourseDetails.aspx?CourseId=', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        content= response.xpath('//div[@id="Content"]')[0]
        fee= response.xpath('//div[@id="ctl00_cphDefaultPage_courseDetail_trTuition"]')[0]
        temp= response.url

        yield {            
            'title': content.xpath('.//h1/text()').extract_first(),
            'tuition_fee': content.xpath('.//span[@id="ctl00_cphDefaultPage_courseDetail_lblTuition"]/text()').extract_first(),
            'source_url': temp
        }
        
#         item = scrapy.Item()
#         item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
#         item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
#         item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
#         item['link_text'] = response.meta['link_text']
#         url = response.xpath('//td[@id="additional_data"]/@href').get()
#         return response.follow(url, self.parse_additional_page, cb_kwargs=dict(item=item))

#     def parse_additional_page(self, response, item):
#         item['additional_data'] = response.xpath('//p[@id="additional_data"]/text()').get()
#         return item
