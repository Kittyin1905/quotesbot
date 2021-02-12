# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "item-test"
    start_urls = [
        'https://cricos.education.gov.au/Course/CourseDetails.aspx?CourseId=97668/',
    ]

    def parse(self, response):
        content= response.xpath('//div[@id="Content"]')[0]
        fee= response.xpath('//div[@id="ctl00_cphDefaultPage_courseDetail_trTuition"]')[0]
        yield {
            'title': content.xpath('//h1/text()').extract_first(),
            'tuition_fee': fee.xpath('//span[@id="ctl00_cphDefaultPage_courseDetail_lblTuition"]/text()').extract_first(),
            
        }

#         next_page_url = response.css("li.next > a::attr(href)").extract_first()
#         if next_page_url is not None:
#             yield scrapy.Request(response.urljoin(next_page_url))

