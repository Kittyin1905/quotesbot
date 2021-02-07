# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
       # 'http://quotes.toscrape.com/tag/love/',
       # 'https://www.flowersforeveryone.com.au/',
       # 'https://search.studyinaustralia.gov.au/course/search-results.html?qualificationid=11',
        'https://soyummy.com/breakfast/',
    ]

    def parse(self, response):
        for quote in response.css("div.post-preview-box"):
            yield {
                'text': quote.css("a::attr(href)").extract_first(),
                'author': quote.css("div.post-preview-box-title::text").extract_first(),
     #           'tags': quote.css("div.fl_w100 > span::text").extract()
            }

 #       next_page_url = response.css("li.next > a::attr(href)").extract_first()
 #       if next_page_url is not None:
 #           yield scrapy.Request(response.urljoin(next_page_url))

