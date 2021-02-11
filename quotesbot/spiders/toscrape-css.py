# -*- coding: utf-8 -*-
import scrapy
import logging
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor

# class MySpider(CrawlSpider):
#     name = 'soyummy.com'
#     allowed_domains = ['soyummy.com']
#     start_urls = ['https://soyummy.com/breakfast/']

#     rules = (
#         # Extract links matching 'category.php' (but not matching 'subsection.php')
#         # and follow links from them (since no callback means follow=True by default).
#         Rule(LinkExtractor(allow=('page', ), deny=('subsection\.php', ))),

#         # Extract links matching 'item.php' and parse them with the spider's method parse_item
#         Rule(LinkExtractor(allow=('recipe', )), callback='parse_item'),
#     )

#     def parse_item(self, response):
#         self.logger.info('Hi, this is an item page! %s', response.url)
#         content= response.css("div.content-container")[0]
#         text= response.css("ul.single-recipe-page-ingredients__list")[0]
#         temp= response.css("div.single-recipe-page-info-item")

#         yield {
#             'title': content.css("h1.content__title::text").extract_first(),
#             'subtitle': content.css("div.content__category::text").extract_first(),
#             'description': content.css("div.description-container::text").extract_first(),
#             'serves': temp[3].css("div.single-recipe-page-info-item__text::text").extract_first(),
#             'prep_time': temp[0].css("div.single-recipe-page-info-item__text::text").extract_first(),
#             'cooking_time': temp[1].css("div.single-recipe-page-info-item__text::text").extract_first(),
#             'complexity': temp[2].css("div.single-recipe-page-info-item__text::text").extract_first(),
#             'ingredients': text.css("li.single-recipe-page__ingredient::text").extract(),
#             'steps_title': content.css("div.single-recipe-page-step__title::text").extract(),
#             'steps_text': content.css("div.single-recipe-page-step__text span::text").extract()
#         }

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

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'https://soyummy.com/breakfast/',
    ]
    
    def parse(self,response):
        for item_url in response.css('a[href*=recipe]::attr(href)').getall():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_item)
            
        next_page_url = response.css("div.title-with-link__link a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
        
    def parse_item(self, response):
        content= response.css("div.content-container")[0]
        text= response.css("ul.single-recipe-page-ingredients__list")[0]
     #   temp= response.css("div.single-recipe-page-info-item")

        yield {            
            'title': content.css("h1.content__title::text").extract_first(),
            'subtitle': content.css("div.content__category::text").extract_first(),
            'description': content.css("div.description-container::text").extract_first(),
            'info_title': content.css("div.single-recipe-page-info-item__title::text").extract(),
            'info_text': content.css("div.single-recipe-page-info-item__text::text").extract(),
            'ingredients': text.css("li.single-recipe-page__ingredient::text").extract(),
            'steps_title': content.css("div.single-recipe-page-step__title::text").extract(),
            'steps_text': content.css("div.single-recipe-page-step__text span::text").extract()
        }
       

        
        
