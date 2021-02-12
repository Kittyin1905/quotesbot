# -*- coding: utf-8 -*-
import scrapy
import logging

class ToScrapeCSSSpider(scrapy.Spider):
    name = "study_au"
    start_urls = [
        'https://search.studyinaustralia.gov.au/course/search-results.html?qualificationid=9&locationid=4/',
    ]
  #      for item_url in response.css('a[href*=recipe]::attr(href)').getall():   
    def parse(self,response):
        for item_url in response.css('a.al_crs::attr(href)').getall():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_item)
     
        next_page_url = response.css("li.nxt a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
        
    def parse_item(self, response):
        tuition= response.css("div.tb_cl div.fl_w100")[3]
        univ= response.css("h2.univ_tit").extract_first()
        temp= response.url
        
        for content in response.css("div.rs_cnt"):
            yield {
            'uni_title': univ,
            'crs_title': content.css("h3.crs_tit ::text").extract_first(),
            'fee': tuition.css("span::text").extract_first(),
            'url':temp
            }
       
