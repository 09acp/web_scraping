# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:28:24 2020

@author: 09ale
"""


import pandas as pd 
import numpy as np
import scrapy 
from scrapy.crawler import CrawlerProcess 

class Spider_1 (scrapy.Spider):
    name = 'test_spidur'
    
    def start_requests(self):
        urls = ['https://www.digicom-eshop.com/collections/batteries', # ~330 comments
                ]
        for url in urls:
            yield scrapy.Request(url=url,
                                 callback=self.parse)
            
    def parse(self, response):
        digi_dic = {}
        # prices = response.css('div.product-item--price text-center>div>p>small::text').extract()
        titles = response.css('p.h6::text')
        print('TITLES',titles)
        """
        titles_c = [t.strip() for t in titles.extract()]
        links = response.css('div.grid-item>a::attr(href)')
        links_c = [link for link in links.extract()]
        digi_dic[titles_c] = links_c
        """
        
        
        
        #html_file = 'digi_prices.html'
        #csv_file = ('%s_toy_dates.csv'%(name))
        #csv_file = ('digi_prices.csv')
        #print(len(prices))
        #with open(csv_file, 'wb') as f:
            #f.write(response.body)
            #f.writelines([price+'/n' for price in prices])
            
            
process = CrawlerProcess()
process.crawl(Spider_1)
process.start()

# In[] 




