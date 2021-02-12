# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "item-test"
    start_urls = [
        'https://search.studyinaustralia.gov.au/course/search-results.html?qualificationid=9',
    ]

    def parse(self, response):
        content= response.xpath('//div[@class="brd_btm"]')[0]
      #  fee= response.xpath('//div[@id="ctl00_cphDefaultPage_courseDetail_trTuition"]')[0]
        yield {
            'title': content.xpath('//h2[@class="univ_tit"]/text()').extract_first(),
     #       'tuition_fee': fee.xpath('//span[@id="ctl00_cphDefaultPage_courseDetail_lblTuition"]/text()').extract_first(),
            
        }

#         next_page_url = response.css("li.next > a::attr(href)").extract_first()
#         if next_page_url is not None:
#             yield scrapy.Request(response.urljoin(next_page_url))

