# -*- coding: utf-8 -*-
import scrapy
import logging

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
       # 'http://quotes.toscrape.com/tag/love/',
       # 'https://www.flowersforeveryone.com.au/',
        'https://soyummy.com/recipe/glazed-lemon-poppy-seed-pastries/',
      #  'https://search.studyinaustralia.gov.au/course/search-results.html?qualificationid=11',
    ]

    def parse(self, response):
        content= response.css("div.content-container")[0]
        text= response.css("ul.single-recipe-page-ingredients__list")[0]
        yield {
            'title': content.css("h1.content__title::text").extract(),
            'ingredients': text.css("li.single-recipe-page__ingredient::text").extract(),
            'steps': content.css("div.single-recipe-page-step__title::text").extract()
        }
        
# class Step(scrapy.Item):
#     name = scrapy.Field()
     
# class ToScrapeCSSSpider(scrapy.Spider):
#     name = "toscrape-css"
#     start_urls = [
#         'https://soyummy.com/recipe/glazed-lemon-poppy-seed-pastries/',
#     ]
  
        
#     def parse(self, response):
#         self.logger.info('A parse1 response from %s just arrived!', response.url)
#         text= response.css("ul.single-recipe-page-ingredients__list")[0]
#         yield {
#             'ingredients': text.css("li.single-recipe-page__ingredient::text").extract()
#         }
        
        
