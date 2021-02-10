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
        temp= response.css("div.single-recipe-page-info-item")

        yield {
            'title': content.css("h1.content__title::text").extract_first(),
            'subtitle': content.css("div.content__category::text").extract_first(),
            'description': content.css("div.description-container::text").extract_first(),
            'serves': temp[3].css("div.single-recipe-page-info-item__text::text").extract_first(),
            'prep_time': temp[0].css("div.single-recipe-page-info-item__text::text").extract_first(),
            'cooking_time': temp[1].css("div.single-recipe-page-info-item__text::text").extract_first(),
            'complexity': temp[2].css("div.single-recipe-page-info-item__text::text").extract_first(),
            'ingredients': text.css("li.single-recipe-page__ingredient::text").extract(),
            'steps_title': content.css("div.single-recipe-page-step__title::text").extract(),
            'steps_text': content.css("div.single-recipe-page-step__text::text").extract()
        }

#             for element in content.css("li.single-recipe-page-step"):
#                 'step[title]': content.css("div.single-recipe-page-step__title::text").extract()
#                 'step[text]': content.css("div.single-recipe-page-step__text span::text").extract()
#             'steps':"title:" + content.css("div.single-recipe-page-step__title::text").extract()+
#             "text:" + content.css("div.single-recipe-page-step__text::text").extract()+
        
        
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
        
        
