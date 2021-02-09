# -*- coding: utf-8 -*-
import scrapy
import logging

class Step(scrapy.Item):
    name = scrapy.Field()
 
   
    
class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
       # 'http://quotes.toscrape.com/tag/love/',
       # 'https://www.flowersforeveryone.com.au/',
       # 'https://search.studyinaustralia.gov.au/course/search-results.html?qualificationid=11',
       # 'https://soyummy.com/breakfast/',
        'https://soyummy.com/recipe/glazed-lemon-poppy-seed-pastries/'
    ]
    

    def parse(self, response):
   #     quote = response.css("ul.single-recipe-page-steps-container")[0]
        text= response.css("ul.single-recipe-page-ingredients__list")[0]
       # content= response.css("div.content-container")[0]
        yield{
            'ingredients':text.css("li.single-recipe-page__ingredient::text").extract()
            
          #   'title': content.css("h1.content__title::text").extract(),
         #    'steps': content.css("div.single-recipe-page-step__title::text").extract(),
             'ingredients':text.css("li.single-recipe-page__ingredient::text").extract()
         }
        
        self.logger.info('A mmparse response from %s just arrived!', response.url)
        
 #       for quote in response.css("li.single-recipe-page-step"):
   #         step[name]=quote.css("div.single-recipe-page-step__title::text").extract_first()
   #         yield {      
 #               'author': quote.css("div.single-recipe-page-step__title::text").extract_first(),
  #          }
  #      for quote in response.css("li.single-recipe-page__ingredient"):
  #          ingredient= quote.css("li.single-recipe-page__ingredient::text").extract_first()
       #     yield{
         #       'text': quote.css("div.single-recipe-page-info-item_content > div::text").extract(),
     #           'ingredient': quote.css("li.single-recipe-page__ingredient::text").extract_first(),
       #         'text': quote.css("a::attr(href)").extract_first(),
       #         'author': quote.css("div.post-preview-box-title::text").extract_first(),
     #           'tags': quote.css("div.fl_w100 > span::text").extract()
     #       }
       
 #       next_page_url = response.css("li.next > a::attr(href)").extract_first()
 #       if next_page_url is not None:
 #           yield scrapy.Request(response.urljoin(next_page_url))

