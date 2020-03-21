# -*- coding: utf-8 -*-
"""
Scrape DC course directory for titles 

Created on Sat Mar  9 17:28:24 2020

@author: 09ale
"""

import pandas as pd 
import numpy as np
import scrapy 
from scrapy.crawler import CrawlerProcess 

def run_spider(class_spider):
    process = CrawlerProcess()
    process.crawl(class_spider)
    process.start()

# In[]  TEXT FILE HAS SAVES ALL HTML - CANNOT FIND COURSE TITLES!
class Spider_1 (scrapy.Spider):
    name = 'titles_spidur_1'
    def start_requests(self):
        urls = ['https://learn.datacamp.com/courses/all',
                ]
        for url in urls:
            yield scrapy.Request(url=url,
                                 callback=self.parse) 
            
    def parse(self, response):
        txt_file = 'titles_spider_1.txt'   # cant read html
        with open(txt_file, 'wb') as f:
            f.write( response.body )  # get entire body of html
        
run_spider(Spider_1) # function to run spider
# In[] SAVE TITLE TO CSV - EMPTY CSV!
class Spider_2 (scrapy.Spider):
    name = 'titles_spidur_2'
    def start_requests(self):
        urls = ['https://learn.datacamp.com/courses/all',
                ]
        for url in urls:
            yield scrapy.Request(url=url,
                                 callback=self.parse)
    
    def parse(self, response):
        #txt_file = 'titles_spider_2.txt'   # name of txt
        txt_file = 'titles_spider_2.csv'
        titles = response.css('h4.course-block__title::text').extract() # retrieve titles only
        with open(txt_file, 'wb') as f:
            #f.write( titles )
            f.writelines( [title+'\n' for title in titles] ) # list comprehension save 
        
run_spider(Spider_2) # function to run spider
# In[]







# In[]

















