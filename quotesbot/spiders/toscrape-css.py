# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
       # 'http://quotes.toscrape.com/tag/love/',
        'https://www.flowersforeveryone.com.au/',
    ]

    def parse(self, response):
        for quote in response.css("div.card"):
            yield {
                'text': quote.css("span.product-name::text").extract_first(),
    #            'author': quote.css("small.author::text").extract_first(),
    #            'tags': quote.css("div.tags > a.tag::text").extract()
            }

 #       next_page_url = response.css("li.next > a::attr(href)").extract_first()
 #       if next_page_url is not None:
 #           yield scrapy.Request(response.urljoin(next_page_url))

